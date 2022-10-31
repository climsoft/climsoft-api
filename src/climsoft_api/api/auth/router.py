import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text as sa_text
from climsoft_api.api.schema import TokenSchema, PasswordRequestForm
from climsoft_api.db import get_session
from climsoft_api.config import settings
from jose import jwt
from datetime import datetime, timedelta
from uuid import uuid4

router = APIRouter()


@router.post("/token", response_model=TokenSchema)
def authenticate(
    payload: PasswordRequestForm = Depends(),
):
    if payload.scope:
        deployment_key = next(
            filter(lambda x: x.startswith("deployment_key"), payload.scope)
        ).split(":")[1]
    else:
        deployment_key = None

    session: Session = get_session(deployment_key)

    try:
        user = session.execute(
            sa_text(
                f"""
                    SELECT User
                    FROM mysql.user 
                    WHERE User="{payload.username}" AND Password=password("{payload.password}")
                """
            )
        ).all()

        if not user:
            raise HTTPException(400, "Invalid login credentials")

        user = user[0]

        access_token = jwt.encode(
            {
                "sub": user["User"],
                "exp": datetime.utcnow() + timedelta(hours=24),
                "token_type": "access",
                "jti": str(uuid4()),
                "deployment_key": deployment_key,
            },
            key=settings.SECRET_KEY,
        )
        return TokenSchema(access_token=access_token, username=user["User"])
    except Exception as e:
        logging.exception(e)
    finally:
        session.close()
