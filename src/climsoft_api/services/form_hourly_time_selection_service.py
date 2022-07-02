import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_hourly_time_selection import schema as form_hourly_time_selection_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFormHourlyTimeSelectionService")
logging.basicConfig(level=logging.INFO)


def search(
    db_session: Session,
    _query: str,
    offset: int = 0,
    limit: int = 50
) -> List[form_hourly_time_selection_schema.FormHourlyTimeSelection]:
    results = (
        db_session.query(models.FormHourlyTimeSelection)
        .filter(
            models.FormHourlyTimeSelection.hh == int(_query)
        ).offset(offset).limit(limit).all()
    )

    return [
        form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(r)
        for r in results
    ]


def get_or_404(
    db_session: Session, 
    hh: int
):
    form_hourly_time_selection = (
        db_session.query(models.FormHourlyTimeSelection)
        .filter_by(hh=hh)
        .first()
    )

    if not form_hourly_time_selection:
        raise HTTPException(
            status_code=404,
            detail=_("FormHourlyTimeSelection does not exist.")
        )

    return form_hourly_time_selection


def create(
    db_session: Session,
    data: form_hourly_time_selection_schema.CreateFormHourlyTimeSelection
) -> form_hourly_time_selection_schema.FormHourlyTimeSelection:
    form_hourly_time_selection = models.FormHourlyTimeSelection(**data.dict())
    db_session.add(form_hourly_time_selection)
    db_session.commit()
    return form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(form_hourly_time_selection)


def get(
    db_session: Session,
    hh: int
) -> form_hourly_time_selection_schema.FormHourlyTimeSelection:
    form_hourly_time_selection = get_or_404(
        db_session,
        hh
    )
    return form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(form_hourly_time_selection)


def query(
    db_session: Session,
    hh: int = None,
    hh_selection: int = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_hourly_time_selection_schema.FormHourlyTimeSelection]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_hourly_time_selection` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormHourlyTimeSelection)

    if hh is not None:
        q = q.filter_by(hh=hh)

    if hh_selection is not None:
        q = q.filter_by(hh_selection=hh_selection)

    return (
        get_count(q),
        [
            form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(s) for s in q.offset(
                offset
            ).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    hh: int,
    updates: form_hourly_time_selection_schema.UpdateFormHourlyTimeSelection
) -> form_hourly_time_selection_schema.FormHourlyTimeSelection:
    get_or_404(db_session, hh)
    db_session.query(models.FormHourlyTimeSelection).filter_by(
        hh=hh
    ).update(updates.dict())
    db_session.commit()
    updated_form_hourly_time_selection = (
        db_session.query(models.FormHourlyTimeSelection)
        .filter_by(
            hh=hh
        ).first()
    )
    return form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(updated_form_hourly_time_selection)


def delete(
    db_session: Session,
    hh: int
) -> bool:
    get_or_404(
        db_session,
        hh
    )
    db_session.query(models.FormHourlyTimeSelection).filter_by(
        hh=hh
    ).delete()
    db_session.commit()
    return True
