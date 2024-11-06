from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dump_rdf_type import DumpRDFType
from ...models.dump_response import DumpResponse
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


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["DumpResponse"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DumpResponse.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["DumpResponse"]]]:
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
) -> Response[Union[Any, List["DumpResponse"]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['DumpResponse']]]
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
) -> Optional[Union[Any, List["DumpResponse"]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['DumpResponse']]
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
) -> Response[Union[Any, List["DumpResponse"]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['DumpResponse']]]
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
) -> Optional[Union[Any, List["DumpResponse"]]]:
    """データダンプAPI

    Args:
        rdf_type (DumpRDFType): データタンプAPI対象のデータ種別
        aclconsumer_key (str): アクセストークン

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['DumpResponse']]
    """

    return (
        await asyncio_detailed(
            rdf_type=rdf_type,
            client=client,
            aclconsumer_key=aclconsumer_key,
        )
    ).parsed
