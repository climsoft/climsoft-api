import logging

import backoff
from functools import wraps
import fastapi
import sqlalchemy.exc
from sqlalchemy.orm import Session
from fastapi import Depends
from climsoft_api.api import deps
from climsoft_api.utils.response import get_error_response


logger = logging.getLogger("RootExcHandler")
logging.basicConfig(level=logging.INFO)


def handle_exceptions(func):
    @wraps(func)
    @backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
    def wrapper(
        *args,
        db_session: Session = Depends(deps.get_session),
        **kwargs
    ):
        """A wrapper function"""
        try:
            return func(*args, db_session=db_session, **kwargs)
        except fastapi.HTTPException:
            raise
        except sqlalchemy.exc.IntegrityError as e:
            db_session.rollback()
            logger.exception(e)
            if hasattr(e, "orig") and type(e.orig.args) == tuple and len(
                e.orig.args
            ) >= 2:
                error_message = e.orig.args[1].split("(")[0]
            else:
                error_message = e.__cause__
            return get_error_response(
                message=str(error_message).strip()
            )
        except Exception as e:
            logger.exception(e)
            return get_error_response(message="An unknown error occurred.")

    return wrapper
