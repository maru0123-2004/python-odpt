from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptrailway: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["acl:consumerKey"] = aclconsumer_key

    params["owl:sameAs"] = owlsame_as

    params["odpt:operator"] = odptoperator

    params["odpt:railway"] = odptrailway

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/odpt:Train",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 500:
        return None
    if response.status_code == 503:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    odptrailway: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """列車情報(列車の位置情報)を取得する

    Args:
        aclconsumer_key (str): アクセストークン
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrailway (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        aclconsumer_key=aclconsumer_key,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptrailway=odptrailway,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    owlsame_as: Union[Unset, str] = UNSET,
    odptoperator: Union[Unset, str] = UNSET,
    odptrailway: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """列車情報(列車の位置情報)を取得する

    Args:
        aclconsumer_key (str): アクセストークン
        owlsame_as (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrailway (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        aclconsumer_key=aclconsumer_key,
        owlsame_as=owlsame_as,
        odptoperator=odptoperator,
        odptrailway=odptrailway,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
