from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bus_timetable import BusTimetable
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aclconsumer_key: str,
    id: Union[Unset, str] = UNSET,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: str,
    odptbusroute_pattern: Union[Unset, str] = UNSET,
    dctitle: Union[Unset, str] = UNSET,
    odptcalendar: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["acl:consumerKey"] = aclconsumer_key

    params["@id"] = id

    params["owl:sameAs"] = owlsame_as

    params["odpt:operator"] = odptoperator

    params["odpt:busroutePattern"] = odptbusroute_pattern

    params["dc:title"] = dctitle

    params["odpt:calendar"] = odptcalendar

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/odpt:BusTimetable",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["BusTimetable"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BusTimetable.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["BusTimetable"]]]:
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
    id: Union[Unset, str] = UNSET,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: str,
    odptbusroute_pattern: Union[Unset, str] = UNSET,
    dctitle: Union[Unset, str] = UNSET,
    odptcalendar: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["BusTimetable"]]]:
    """バスの便の時刻表

    Args:
        aclconsumer_key (str): アクセストークン
        id (Union[Unset, str]): 固有識別子
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbusroute_pattern (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctitle (Union[Unset, str]):
        odptcalendar (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['BusTimetable']]]
    """

    kwargs = _get_kwargs(
        aclconsumer_key=aclconsumer_key,
        id=id,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptbusroute_pattern=odptbusroute_pattern,
        dctitle=dctitle,
        odptcalendar=odptcalendar,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    id: Union[Unset, str] = UNSET,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: str,
    odptbusroute_pattern: Union[Unset, str] = UNSET,
    dctitle: Union[Unset, str] = UNSET,
    odptcalendar: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["BusTimetable"]]]:
    """バスの便の時刻表

    Args:
        aclconsumer_key (str): アクセストークン
        id (Union[Unset, str]): 固有識別子
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbusroute_pattern (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctitle (Union[Unset, str]):
        odptcalendar (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['BusTimetable']]
    """

    return sync_detailed(
        client=client,
        aclconsumer_key=aclconsumer_key,
        id=id,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptbusroute_pattern=odptbusroute_pattern,
        dctitle=dctitle,
        odptcalendar=odptcalendar,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    id: Union[Unset, str] = UNSET,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: str,
    odptbusroute_pattern: Union[Unset, str] = UNSET,
    dctitle: Union[Unset, str] = UNSET,
    odptcalendar: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["BusTimetable"]]]:
    """バスの便の時刻表

    Args:
        aclconsumer_key (str): アクセストークン
        id (Union[Unset, str]): 固有識別子
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbusroute_pattern (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctitle (Union[Unset, str]):
        odptcalendar (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['BusTimetable']]]
    """

    kwargs = _get_kwargs(
        aclconsumer_key=aclconsumer_key,
        id=id,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptbusroute_pattern=odptbusroute_pattern,
        dctitle=dctitle,
        odptcalendar=odptcalendar,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    id: Union[Unset, str] = UNSET,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: str,
    odptbusroute_pattern: Union[Unset, str] = UNSET,
    dctitle: Union[Unset, str] = UNSET,
    odptcalendar: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["BusTimetable"]]]:
    """バスの便の時刻表

    Args:
        aclconsumer_key (str): アクセストークン
        id (Union[Unset, str]): 固有識別子
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbusroute_pattern (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctitle (Union[Unset, str]):
        odptcalendar (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['BusTimetable']]
    """

    return (
        await asyncio_detailed(
            client=client,
            aclconsumer_key=aclconsumer_key,
            id=id,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptbusroute_pattern=odptbusroute_pattern,
            dctitle=dctitle,
            odptcalendar=odptcalendar,
        )
    ).parsed
