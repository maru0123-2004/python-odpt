from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.place_rdf_type import PlaceRDFType
from ...models.place_search_response import PlaceSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rdf_type: PlaceRDFType,
    *,
    aclconsumer_key: str,
    lat: float,
    lon: float,
    radius: int,
    predicate: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["acl:consumerKey"] = aclconsumer_key

    params["lat"] = lat

    params["lon"] = lon

    params["radius"] = radius

    params["PREDICATE"] = predicate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/places/{rdf_type}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["PlaceSearchResponse"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlaceSearchResponse.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["PlaceSearchResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rdf_type: PlaceRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    lat: float,
    lon: float,
    radius: int,
    predicate: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["PlaceSearchResponse"]]]:
    """地物情報検索API

    Args:
        rdf_type (PlaceRDFType): 地物情報検索対象のデータ種別
        aclconsumer_key (str): アクセストークン
        lat (float):
        lon (float):
        radius (int):
        predicate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['PlaceSearchResponse']]]
    """

    kwargs = _get_kwargs(
        rdf_type=rdf_type,
        aclconsumer_key=aclconsumer_key,
        lat=lat,
        lon=lon,
        radius=radius,
        predicate=predicate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rdf_type: PlaceRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    lat: float,
    lon: float,
    radius: int,
    predicate: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["PlaceSearchResponse"]]]:
    """地物情報検索API

    Args:
        rdf_type (PlaceRDFType): 地物情報検索対象のデータ種別
        aclconsumer_key (str): アクセストークン
        lat (float):
        lon (float):
        radius (int):
        predicate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['PlaceSearchResponse']]
    """

    return sync_detailed(
        rdf_type=rdf_type,
        client=client,
        aclconsumer_key=aclconsumer_key,
        lat=lat,
        lon=lon,
        radius=radius,
        predicate=predicate,
    ).parsed


async def asyncio_detailed(
    rdf_type: PlaceRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    lat: float,
    lon: float,
    radius: int,
    predicate: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["PlaceSearchResponse"]]]:
    """地物情報検索API

    Args:
        rdf_type (PlaceRDFType): 地物情報検索対象のデータ種別
        aclconsumer_key (str): アクセストークン
        lat (float):
        lon (float):
        radius (int):
        predicate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['PlaceSearchResponse']]]
    """

    kwargs = _get_kwargs(
        rdf_type=rdf_type,
        aclconsumer_key=aclconsumer_key,
        lat=lat,
        lon=lon,
        radius=radius,
        predicate=predicate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rdf_type: PlaceRDFType,
    *,
    client: Union[AuthenticatedClient, Client],
    aclconsumer_key: str,
    lat: float,
    lon: float,
    radius: int,
    predicate: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["PlaceSearchResponse"]]]:
    """地物情報検索API

    Args:
        rdf_type (PlaceRDFType): 地物情報検索対象のデータ種別
        aclconsumer_key (str): アクセストークン
        lat (float):
        lon (float):
        radius (int):
        predicate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['PlaceSearchResponse']]
    """

    return (
        await asyncio_detailed(
            rdf_type=rdf_type,
            client=client,
            aclconsumer_key=aclconsumer_key,
            lat=lat,
            lon=lon,
            radius=radius,
            predicate=predicate,
        )
    ).parsed
