import climsoft_api.api.data_form.schema as data_form_schema
from climsoft_api.api import deps
from climsoft_api.services import data_form_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.get(
    "/",
    response_model=data_form_schema.DataFormQueryResponse
)
def get_data_forms(
    order_num: int = None,
    table_name: str = None,
    form_name: str = None,
    description: str = None,
    selected: bool = None,
    val_start_position: int = None,
    val_end_position: int = None,
    elem_code_location: str = None,
    sequencer: str = None,
    entry_mode: bool = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, data_forms = data_form_service.query(
            db_session=db_session,
            order_num=order_num,
            table_name=table_name,
            form_name=form_name,
            description=description,
            selected=selected,
            val_start_position=val_start_position,
            val_end_position=val_end_position,
            elem_code_location=elem_code_location,
            sequencer=sequencer,
            entry_mode=entry_mode,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=data_forms,
            message=_("Successfully fetched data forms.")
        )
    except data_form_service.FailedGettingDataFormList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{form_name}",
    response_model=data_form_schema.DataFormResponse
)
def get_data_form_by_id(
    form_name: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[data_form_service.get(
                db_session=db_session,
                form_name=form_name
            )],
            message=_("Successfully fetched data form."),
        )
    except data_form_service.FailedGettingDataForm as e:
        return get_error_response(message=str(e))


@router.post(
    "/",
    response_model=data_form_schema.DataFormResponse
)
def create_data_form(
    data: data_form_schema.CreateDataForm,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[data_form_service.create(db_session=db_session, data=data)],
            message=_("Successfully created data form."),
        )
    except data_form_service.FailedCreatingDataForm as e:
        return get_error_response(message=str(e))


@router.put("/{form_name}", response_model=data_form_schema.DataFormResponse)
def update_data_form(
    form_name: str,
    data: data_form_schema.UpdateDataForm,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                data_form_service.update(
                    db_session=db_session,
                    form_name=form_name,
                    updates=data
                )
            ],
            message=_("Successfully updated data form."),
        )
    except data_form_service.FailedUpdatingDataForm as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{form_name}",
    response_model=data_form_schema.DataFormResponse
)
def delete_data_form(
    form_name: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        data_form_service.delete(db_session=db_session, form_name=form_name)
        return get_success_response(
            result=[],
            message=_("Successfully deleted data form.")
        )
    except data_form_service.FailedDeletingDataForm as e:
        return get_error_response(message=str(e))
