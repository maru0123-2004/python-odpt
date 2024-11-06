from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.flight_information_departure import FlightInformationDeparture
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptairline: Union[Unset, str] = UNSET,
    odptflight_status: Union[Unset, str] = UNSET,
    odptdeparture_airport: Union[Unset, str] = UNSET,
    odptdeparture_airport_terminal: Union[Unset, str] = UNSET,
    odptdeparture_gate: Union[Unset, str] = UNSET,
    odptdestination_airport: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["acl:consumerKey"] = aclconsumer_key

    params["owl:sameAs"] = owlsame_as

    params["odpt:operator"] = odptoperator

    params["odpt:airline"] = odptairline

    params["odpt:flightStatus"] = odptflight_status

    params["odpt:departureAirport"] = odptdeparture_airport

    params["odpt:departureAirportTerminal"] = odptdeparture_airport_terminal

    params["odpt:departureGate"] = odptdeparture_gate

    params["odpt:destinationAirport"] = odptdestination_airport

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/odpt:FlightInformationDeparture",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["FlightInformationDeparture"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FlightInformationDeparture.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["FlightInformationDeparture"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptairline: Union[Unset, str] = UNSET,
    odptflight_status: Union[Unset, str] = UNSET,
    odptdeparture_airport: Union[Unset, str] = UNSET,
    odptdeparture_airport_terminal: Union[Unset, str] = UNSET,
    odptdeparture_gate: Union[Unset, str] = UNSET,
    odptdestination_airport: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["FlightInformationDeparture"]]]:
    """フライト出発情報の取得

    Args:
        aclconsumer_key (str): アクセストークン
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (Union[Unset, str]):
        odptairline (Union[Unset, str]):
        odptflight_status (Union[Unset, str]):
        odptdeparture_airport (Union[Unset, str]):
        odptdeparture_airport_terminal (Union[Unset, str]):
        odptdeparture_gate (Union[Unset, str]):
        odptdestination_airport (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['FlightInformationDeparture']]]
    """

    kwargs = _get_kwargs(
        aclconsumer_key=aclconsumer_key,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptairline=odptairline,
        odptflight_status=odptflight_status,
        odptdeparture_airport=odptdeparture_airport,
        odptdeparture_airport_terminal=odptdeparture_airport_terminal,
        odptdeparture_gate=odptdeparture_gate,
        odptdestination_airport=odptdestination_airport,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptairline: Union[Unset, str] = UNSET,
    odptflight_status: Union[Unset, str] = UNSET,
    odptdeparture_airport: Union[Unset, str] = UNSET,
    odptdeparture_airport_terminal: Union[Unset, str] = UNSET,
    odptdeparture_gate: Union[Unset, str] = UNSET,
    odptdestination_airport: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["FlightInformationDeparture"]]]:
    """フライト出発情報の取得

    Args:
        aclconsumer_key (str): アクセストークン
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (Union[Unset, str]):
        odptairline (Union[Unset, str]):
        odptflight_status (Union[Unset, str]):
        odptdeparture_airport (Union[Unset, str]):
        odptdeparture_airport_terminal (Union[Unset, str]):
        odptdeparture_gate (Union[Unset, str]):
        odptdestination_airport (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['FlightInformationDeparture']]
    """

    return sync_detailed(
        client=client,
        aclconsumer_key=aclconsumer_key,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptairline=odptairline,
        odptflight_status=odptflight_status,
        odptdeparture_airport=odptdeparture_airport,
        odptdeparture_airport_terminal=odptdeparture_airport_terminal,
        odptdeparture_gate=odptdeparture_gate,
        odptdestination_airport=odptdestination_airport,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptairline: Union[Unset, str] = UNSET,
    odptflight_status: Union[Unset, str] = UNSET,
    odptdeparture_airport: Union[Unset, str] = UNSET,
    odptdeparture_airport_terminal: Union[Unset, str] = UNSET,
    odptdeparture_gate: Union[Unset, str] = UNSET,
    odptdestination_airport: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["FlightInformationDeparture"]]]:
    """フライト出発情報の取得

    Args:
        aclconsumer_key (str): アクセストークン
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (Union[Unset, str]):
        odptairline (Union[Unset, str]):
        odptflight_status (Union[Unset, str]):
        odptdeparture_airport (Union[Unset, str]):
        odptdeparture_airport_terminal (Union[Unset, str]):
        odptdeparture_gate (Union[Unset, str]):
        odptdestination_airport (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['FlightInformationDeparture']]]
    """

    kwargs = _get_kwargs(
        aclconsumer_key=aclconsumer_key,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptairline=odptairline,
        odptflight_status=odptflight_status,
        odptdeparture_airport=odptdeparture_airport,
        odptdeparture_airport_terminal=odptdeparture_airport_terminal,
        odptdeparture_gate=odptdeparture_gate,
        odptdestination_airport=odptdestination_airport,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptairline: Union[Unset, str] = UNSET,
    odptflight_status: Union[Unset, str] = UNSET,
    odptdeparture_airport: Union[Unset, str] = UNSET,
    odptdeparture_airport_terminal: Union[Unset, str] = UNSET,
    odptdeparture_gate: Union[Unset, str] = UNSET,
    odptdestination_airport: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["FlightInformationDeparture"]]]:
    """フライト出発情報の取得

    Args:
        aclconsumer_key (str): アクセストークン
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (Union[Unset, str]):
        odptairline (Union[Unset, str]):
        odptflight_status (Union[Unset, str]):
        odptdeparture_airport (Union[Unset, str]):
        odptdeparture_airport_terminal (Union[Unset, str]):
        odptdeparture_gate (Union[Unset, str]):
        odptdestination_airport (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['FlightInformationDeparture']]
    """

    return (
        await asyncio_detailed(
            client=client,
            aclconsumer_key=aclconsumer_key,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptairline=odptairline,
            odptflight_status=odptflight_status,
            odptdeparture_airport=odptdeparture_airport,
            odptdeparture_airport_terminal=odptdeparture_airport_terminal,
            odptdeparture_gate=odptdeparture_gate,
            odptdestination_airport=odptdestination_airport,
        )
    ).parsed
