from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    file_path: str,
    *,
    aclconsumer_key: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["acl:consumerKey"] = aclconsumer_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/files/{file_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 302:
        return None
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
    file_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
) -> Response[Any]:
    """ファイルを取得する

    Args:
        file_path (str):
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        file_path=file_path,
        aclconsumer_key=aclconsumer_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    file_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
) -> Response[Any]:
    """ファイルを取得する

    Args:
        file_path (str):
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        file_path=file_path,
        aclconsumer_key=aclconsumer_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)