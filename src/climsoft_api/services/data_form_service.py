import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.data_form import schema as data_form_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftDataFormService")
logging.basicConfig(level=logging.INFO)


def get_or_404(db_session: Session, form_name: str):
    data_form = (
        db_session.query(models.DataForm).filter_by(
            form_name=form_name
        ).first()
    )

    if not data_form:
        raise HTTPException(
            status_code=404,
            detail=_("Data form does not exist.")
        )

    return data_form


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: data_form_schema.CreateDataForm
) -> data_form_schema.DataForm:
    data_form = models.DataForm(**data.dict())
    db_session.add(data_form)
    db_session.commit()
    return data_form_schema.DataForm.from_orm(data_form)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(db_session: Session, form_name: str) -> data_form_schema.DataForm:
    data_form = get_or_404(db_session, form_name)

    return data_form_schema.DataForm.from_orm(data_form)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
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
) -> Tuple[int, List[data_form_schema.DataForm]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `data_forms` row skipping
    `offset` number of rows

    """
    q = db_session.query(models.DataForm)

    if order_num is not None:
        q = q.filter_by(order_num=order_num)

    if table_name is not None:
        q = q.filter_by(table_name=table_name)

    if form_name is not None:
        q = q.filter_by(form_name=form_name)

    if description is not None:
        q = q.filter(models.DataForm.description.ilike(f"%{description}%"))

    if selected is not None:
        q = q.filter_by(selected=selected)

    if val_start_position is not None:
        q = q.filter_by(val_start_position=val_start_position)

    if val_end_position is not None:
        q = q.filter_by(val_end_position=val_end_position)

    if elem_code_location is not None:
        q = q.filter_by(elem_code_location=elem_code_location)

    if sequencer is not None:
        q = q.filter_by(sequencer=sequencer)

    if entry_mode is not None:
        q = q.filter(models.DataForm.entry_mode.ilike(f"%{entry_mode}%"))

    return (
        get_count(q),
        [
            data_form_schema.DataForm.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    form_name: str,
    updates: data_form_schema.UpdateDataForm
) -> data_form_schema.DataForm:
    get_or_404(db_session, form_name)
    db_session.query(models.DataForm).filter_by(form_name=form_name).update(
        updates.dict()
    )
    db_session.commit()
    updated_data_form = (
        db_session.query(models.DataForm).filter_by(
            form_name=form_name
        ).first()
    )
    return data_form_schema.DataForm.from_orm(updated_data_form)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, form_name: str) -> bool:
    get_or_404(db_session, form_name)
    db_session.query(models.DataForm).filter_by(
        form_name=form_name
    ).delete()
    db_session.commit()
    return True
