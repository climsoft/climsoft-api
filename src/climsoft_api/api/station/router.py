import logging
import fastapi
from climsoft_api.api import deps
from climsoft_api.api.station import (
    schema as station_schema,
)
from climsoft_api.api.stationqualifier import (
    schema as station_qualifier_schema
)
from climsoft_api.api.stationelement import (
    station_element_with_children as station_element_with_children_schema
)
from climsoft_api.services import (
    station_service,
    stationelement_service,
    stationqualifier_service
)
from climsoft_api.utils.response import (
    get_success_response,
    get_error_response,
    get_success_response_for_query
)
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
from climsoft_api.utils.exception import handle_exceptions

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get("/stations")
@handle_exceptions
def get_stations(
    station_id: str = None,
    station_name: str = None,
    wmoid: str = None,
    icaoid: str = None,
    latitude: float = None,
    longitude: float = None,
    qualifier: str = None,
    elevation: str = None,
    geolocation_method: str = None,
    geolocation_accuracy: str = None,
    opening_datetime: str = None,
    closing_datetime: str = None,
    country: str = None,
    authority: str = None,
    admin_region: str = None,
    drainage_basin: str = None,
    waca_selection: bool = None,
    cpt_selection: bool = None,
    station_operational: bool = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, stations = station_service.query(
        db_session=db_session,
        station_id=station_id,
        station_name=station_name,
        wmoid=wmoid,
        icaoid=icaoid,
        latitude=latitude,
        longitude=longitude,
        qualifier=qualifier,
        elevation=elevation,
        geolocation_method=geolocation_method,
        geolocation_accuracy=geolocation_accuracy,
        opening_datetime=opening_datetime,
        closing_datetime=closing_datetime,
        country=country,
        authority=authority,
        admin_region=admin_region,
        drainage_basin=drainage_basin,
        waca_selection=waca_selection,
        cpt_selection=cpt_selection,
        station_operational=station_operational,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=stations,
        message=_("Successfully fetched stations."),
        schema=translate_schema(
            _,
            station_schema.StationQueryResponse.schema()
        )
    )


@router.get(
    "/stations/search"
)
@handle_exceptions
def search_stations(
    query: str,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, station_elements = station_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset,
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=station_elements,
        message=_("Successfully fetched stations."),
        schema=translate_schema(
            _,
            station_schema.StationQueryResponse.schema()
        )
    )


@router.get("/stations/{station_id}")
@handle_exceptions
def get_station_by_id(
    station_id: str,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[station_service.get(db_session=db_session,
                                    station_id=station_id)],
        message=_("Successfully fetched station."),
        schema=translate_schema(
            _,
            station_schema.StationResponse.schema()
        )
    )


@router.post("/stations")
@handle_exceptions
def create_station(
    data: station_schema.CreateStation,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[station_service.create(db_session=db_session, data=data)],
        message=_("Successfully created station."),
        schema=translate_schema(
            _,
            station_schema.StationResponse.schema()
        )
    )


@router.put("/stations/{station_id}")
@handle_exceptions
def update_station(
    station_id: str,
    data: station_schema.UpdateStation,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            station_service.update(
                db_session=db_session, station_id=station_id, updates=data
            )
        ],
        message=_("Successfully updated station."),
        schema=translate_schema(
            _,
            station_schema.StationResponse.schema()
        )
    )


@router.delete("/stations/{station_id}")
@handle_exceptions
def delete_station(
    station_id: str,
    db_session: Session = Depends(deps.get_session)
):
    station_service.delete(db_session=db_session, station_id=station_id)
    return get_success_response(
        result=[],
        message=_("Successfully deleted station."),
        schema=translate_schema(
            _,
            station_schema.StationResponse.schema()
        )
    )


@router.get(
    "/stations/{station_id}/station-elements"
)
@handle_exceptions
def get_station_with_elements(
    station_id: str,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session)
):
    total, elements = stationelement_service \
        .get_station_elements_with_obs_element(
            db_session=db_session,
            recorded_from=station_id,
            limit=limit,
            offset=offset
        )

    return get_success_response_for_query(
        schema=translate_schema(
            _,
            station_element_with_children_schema
            .StationElementWithObsElementQueryResponse.schema()
        ),
        result=elements,
        total=total,
        limit=limit,
        message=_("Successfully fetched station elements."),
        offset=offset
    )


@router.get(
    "/stations/{station_id}/station-qualifiers"
)
@handle_exceptions
def get_station_qualifiers(
    station_id: str,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session)
):
    total, qualifiers = stationqualifier_service \
        .query(
            db_session=db_session,
            belongs_to=station_id,
            limit=limit,
            offset=offset
        )

    return get_success_response_for_query(
        schema=translate_schema(
            _,
            station_qualifier_schema
            .StationQualifierQueryResponse.schema()
        ),
        result=qualifiers,
        total=total,
        limit=limit,
        message=_("Successfully fetched station qualifiers."),
        offset=offset
    )
