from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dump_rdf_type import DumpRDFType
from ...models import Calendar, Operator, Station, StationTimetable, TrainTimetable, TrainType, \
                    RailDirection, Railway, RailwayFare, PassengerSurvey, BusTimetable, BusroutePattern, \
                    BusroutePatternFare, BusstopPole, BusstopPoleTimetable, Airport, AirportTerminal, \
                    FlightSchedule, FlightStatus, DumpRDFType
from ...types import UNSET, Response


def _get_kwargs(
    rdf_type: DumpRDFType,
    *,
    aclconsumer_key: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["acl:consumerKey"] = aclconsumer_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{rdf_type}.json",
        "params": params,
    }

    return _kwargs


OUTPUT_TYPES=Union["Calendar","Operator","Station","StationTimetable","TrainTimetable",
                   "TrainType","RailDirection","Railway","RailwayFare","PassengerSurvey",
                   "BusTimetable","BusroutePattern","BusroutePatternFare","BusstopPole",
                   "BusstopPoleTimetable","Airport","AirportTerminal","FlightSchedule","FlightStatus"]

def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List[Union[OUTPUT_TYPES]]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            if response_200_item_data["@type"] == DumpRDFType.ODPTCALENDAR:
                response_200_item = Calendar.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTOPERATOR:
                response_200_item = Operator.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTSTATION:
                response_200_item = Station.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTSTATIONTIMETABLE:
                response_200_item = StationTimetable.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTTRAINTIMETABLE:
                response_200_item = TrainTimetable.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTTRAINTYPE:
                response_200_item = TrainType.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTRAILDIRECTION:
                response_200_item = RailDirection.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTRAILWAY:
                response_200_item = Railway.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTRAILWAYFARE:
                response_200_item = RailwayFare.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTPASSENGERSURVEY:
                response_200_item = PassengerSurvey.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTBUSTIMETABLE:
                response_200_item = BusTimetable.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTBUSROUTEPATTERN:
                response_200_item = BusroutePattern.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTBUSROUTEPATTERNFARE:
                response_200_item = BusroutePatternFare.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTBUSSTOPPOLE:
                response_200_item = BusstopPole.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTBUSSTOPPOLETIMETABLE:
                response_200_item = BusstopPoleTimetable.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTAIRPORT:
                response_200_item = Airport.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTAIRPORTTERMINAL:
                response_200_item = AirportTerminal.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTFLIGHTSCHEDULE:
                response_200_item = FlightSchedule.from_dict(response_200_item_data)
            elif response_200_item_data["@type"] == DumpRDFType.ODPTFLIGHTSTATUS:
                response_200_item = FlightStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List[OUTPUT_TYPES]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rdf_type: DumpRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
) -> Response[Union[Any, List[OUTPUT_TYPES]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[OUTPUT_TYPES]]]
    """

    kwargs = _get_kwargs(
        rdf_type=rdf_type,
        aclconsumer_key=aclconsumer_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rdf_type: DumpRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
) -> Optional[Union[Any, List[OUTPUT_TYPES]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List[OUTPUT_TYPES]]
    """

    return sync_detailed(
        rdf_type=rdf_type,
        client=client,
        aclconsumer_key=aclconsumer_key,
    ).parsed


async def asyncio_detailed(
    rdf_type: DumpRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
) -> Response[Union[Any, List[OUTPUT_TYPES]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[OUTPUT_TYPES]]]
    """

    kwargs = _get_kwargs(
        rdf_type=rdf_type,
        aclconsumer_key=aclconsumer_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rdf_type: DumpRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
) -> Optional[Union[Any, List[OUTPUT_TYPES]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List[OUTPUT_TYPES]]
    """

    return (
        await asyncio_detailed(
            rdf_type=rdf_type,
            client=client,
            aclconsumer_key=aclconsumer_key,
        )
    ).parsed
