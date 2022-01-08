from fastapi import APIRouter, Depends
from climsoft_api.services import flag_service
import climsoft_api.api.flag.schema as flag_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get("/", response_model=flag_schema.FlagResponse)
def get_flags(
    character_symbol: str = None,
    num_symbol: int = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        flags = flag_service.query(
            db_session=db_session,
            character_symbol=character_symbol,
            num_symbol=num_symbol,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response(result=flags, message="Successfully fetched flags.")
    except flag_service.FailedGettingFlagList as e:
        return get_error_response(message=str(e))


@router.get("/{character_symbol}", response_model=flag_schema.FlagResponse)
def get_flag_by_id(
    character_symbol: str, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                flag_service.get(
                    db_session=db_session, character_symbol=character_symbol
                )
            ],
            message="Successfully fetched flag.",
        )
    except flag_service.FailedGettingFlag as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=flag_schema.FlagResponse)
def create_flag(
    data: flag_schema.CreateFlag, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[flag_service.create(db_session=db_session, data=data)],
            message="Successfully created flag.",
        )
    except flag_service.FailedCreatingFlag as e:
        return get_error_response(message=str(e))


@router.put("/{character_symbol}", response_model=flag_schema.FlagResponse)
def update_flag(
    character_symbol: str,
    data: flag_schema.UpdateFlag,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                flag_service.update(
                    db_session=db_session,
                    character_symbol=character_symbol,
                    updates=data,
                )
            ],
            message="Successfully updated flag.",
        )
    except flag_service.FailedUpdatingFlag as e:
        return get_error_response(message=str(e))


@router.delete("/{character_symbol}", response_model=flag_schema.FlagResponse)
def delete_flag(character_symbol: str, db_session: Session = Depends(deps.get_session)):
    try:
        flag_service.delete(db_session=db_session, character_symbol=character_symbol)
        return get_success_response(result=[], message="Successfully deleted flag.")
    except flag_service.FailedDeletingFlag as e:
        return get_error_response(message=str(e))
