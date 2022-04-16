import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.instrument import schema as instrument_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftInstrumentService")
logging.basicConfig(level=logging.INFO)


def get_or_404(db_session: Session, instrument_id):
    instrument = (
        db_session.query(models.Instrument)
        .filter_by(instrumentId=instrument_id)
        .first()
    )

    if not instrument:
        raise HTTPException(
            status_code=404,
            detail=_("Instrument does not exist.")
        )

    return instrument


def create(
    db_session: Session, data: instrument_schema.CreateInstrument
) -> instrument_schema.Instrument:

    instrument = models.Instrument(**data.dict())
    db_session.add(instrument)
    db_session.commit()
    return instrument_schema.Instrument.from_orm(instrument)


def get(
    db_session: Session,
    instrument_id: str
) -> instrument_schema.Instrument:
    instrument = (
        db_session.query(models.Instrument)
            .filter_by(instrumentId=instrument_id)
            .options(joinedload("station"))
            .first()
    )

    if not instrument:
        raise HTTPException(
            status_code=404,
            detail=_("Instrument does not exist.")
        )

    return instrument_schema.InstrumentWithStation.from_orm(instrument)


def query(
    db_session: Session,
    instrument_id: str = None,
    instrument_name: str = None,
    serial_number: str = None,
    abbreviation: str = None,
    model: str = None,
    manufacturer: str = None,
    instrument_uncertainty: float = None,
    installation_datetime: str = None,
    uninstallation_datetime: str = None,
    height: str = None,
    station_id: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[instrument_schema.Instrument]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `instrument` row skipping
    `offset` number of rows

    :param db_session: database session
    :param instrument_id: compares with `instrumentId` column for exact match
    :param instrument_name: compares with `instrumentName` column for
                            exact match
    :param serial_number: compares with `serialNumber` column for exact match
    :param abbreviation: compares with `abbreviation` column for exact match
    :param model: checks if the model column contains given input
    :param manufacturer: checks if the manufacturer column contains given input
    :param instrument_uncertainty: returns items with lower or equal
                                    instrumentUncertainty
    :param installation_datetime: returns items with installationDatetime
                                    greater that given input
    :param uninstallation_datetime: returns items with
                                    deinstallationDatetime
                                    smaller than given input
    :param height: returns items with height greater that given input
    :param station_id: compares with installedAt column for exact match
    :param limit: takes first `limit` number of rows
    :param offset: skips first `offset` number of rows
    :return: list of `instrument`
    """
    q = db_session.query(models.Instrument)

    if instrument_id is not None:
        q = q.filter_by(instrumentId=instrument_id)

    if instrument_name is not None:
        q = q.filter_by(instrumentName=instrument_name)

    if serial_number is not None:
        q = q.filter_by(serialNumber=serial_number)

    if abbreviation is not None:
        q = q.filter_by(abbreviation=abbreviation)

    if model is not None:
        q = q.filter(models.Instrument.model.ilike(f"%{model}%"))

    if manufacturer is not None:
        q = q.filter(
            models.Instrument.manufacturer.ilike(f"%{manufacturer}%"))

    if instrument_uncertainty is not None:
        q = q.filter(
            models.Instrument.instrumentUncertainty <= instrument_uncertainty
        )

    if installation_datetime is not None:
        q = q.filter(
            models.Instrument.installationDatetime >= installation_datetime
        )

    if uninstallation_datetime is not None:
        q = q.filter(
            models.Instrument.deinstallationDatetime <= uninstallation_datetime
        )

    if height is not None:
        q = q.filter(models.Instrument.height > height)

    if station_id is not None:
        q = q.filter_by(installedAt=station_id)

    return (
        get_count(q),
        [
            instrument_schema.Instrument.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    instrument_id: str,
    updates: instrument_schema.UpdateInstrument
) -> instrument_schema.Instrument:
    get_or_404(db_session, instrument_id)
    db_session.query(models.Instrument).filter_by(
        instrumentId=instrument_id
    ).update(updates.dict())
    db_session.commit()
    updated_instrument = (
        db_session.query(models.Instrument)
            .filter_by(instrumentId=instrument_id)
            .first()
    )
    return instrument_schema.Instrument.from_orm(updated_instrument)


def delete(db_session: Session, instrument_id: str) -> bool:
    get_or_404(db_session, instrument_id)
    db_session.query(models.Instrument).filter_by(
        instrumentId=instrument_id
    ).delete()
    db_session.commit()
    return True


def search(
    db_session: Session,
    _query: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[instrument_schema.Instrument]]:

    q = db_session.query(models.Instrument)

    if _query:
        q = q.filter(
            models.Instrument.instrumentId.ilike(f"%{_query}%")
            | models.Instrument.instrumentName.ilike(f"%{_query}%")
        )

    return (
        get_count(q),
        [
            instrument_schema.Instrument.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )
