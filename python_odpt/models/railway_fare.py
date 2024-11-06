from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.railway_fare_type import RailwayFareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RailwayFare")


@_attrs_define
class RailwayFare:
    """2駅間の運賃情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (RailwayFareType): クラス名 Example: odpt:RailwayFare.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptfrom_station (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptto_station (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptticket_fare (int): 切符利用時の運賃 Example: 200.
        dctissued (Union[Unset, str]): ISO8601 日付形式
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptic_card_fare (Union[Unset, int]): ICカード利用時の運賃 Example: 196.
        odptchild_ticket_fare (Union[Unset, int]): 切符利用時の子供運賃 Example: 100.
        odptchild_ic_card_fare (Union[Unset, int]): ICカード利用時の子供運賃 Example: 98.
        odptvia_station (Union[Unset, List[str]]): 運賃計算上の経由駅を表すIDのリスト Example:
            ['odpt.Station:TokyoMetro.Tozai.NishiFunabashi'].
        odptvia_railway (Union[Unset, List[str]]): 運賃計算上の経由路線を表すIDのリスト Example: ['odpt.Railway:TokyoMetro.Tozai'].
        odptticket_type (Union[Unset, str]): チケット種別 Example: string.
        odptpayment_method (Union[Unset, List[str]]): 支払い方法のリスト Example: ['string'].
    """

    context: str
    id: str
    type: RailwayFareType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptfrom_station: str
    odptto_station: str
    odptticket_fare: int
    dctissued: Union[Unset, str] = UNSET
    dctvalid: Union[Unset, str] = UNSET
    odptic_card_fare: Union[Unset, int] = UNSET
    odptchild_ticket_fare: Union[Unset, int] = UNSET
    odptchild_ic_card_fare: Union[Unset, int] = UNSET
    odptvia_station: Union[Unset, List[str]] = UNSET
    odptvia_railway: Union[Unset, List[str]] = UNSET
    odptticket_type: Union[Unset, str] = UNSET
    odptpayment_method: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptfrom_station = self.odptfrom_station

        odptto_station = self.odptto_station

        odptticket_fare = self.odptticket_fare

        dctissued = self.dctissued

        dctvalid = self.dctvalid

        odptic_card_fare = self.odptic_card_fare

        odptchild_ticket_fare = self.odptchild_ticket_fare

        odptchild_ic_card_fare = self.odptchild_ic_card_fare

        odptvia_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_station, Unset):
            odptvia_station = self.odptvia_station

        odptvia_railway: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_railway, Unset):
            odptvia_railway = self.odptvia_railway

        odptticket_type = self.odptticket_type

        odptpayment_method: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptpayment_method, Unset):
            odptpayment_method = self.odptpayment_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:date": dcdate,
                "owl:sameAs": owlsame_as,
                "odpt:operator": odptoperator,
                "odpt:fromStation": odptfrom_station,
                "odpt:toStation": odptto_station,
                "odpt:ticketFare": odptticket_fare,
            }
        )
        if dctissued is not UNSET:
            field_dict["dct:issued"] = dctissued
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptic_card_fare is not UNSET:
            field_dict["odpt:icCardFare"] = odptic_card_fare
        if odptchild_ticket_fare is not UNSET:
            field_dict["odpt:childTicketFare"] = odptchild_ticket_fare
        if odptchild_ic_card_fare is not UNSET:
            field_dict["odpt:childIcCardFare"] = odptchild_ic_card_fare
        if odptvia_station is not UNSET:
            field_dict["odpt:viaStation"] = odptvia_station
        if odptvia_railway is not UNSET:
            field_dict["odpt:viaRailway"] = odptvia_railway
        if odptticket_type is not UNSET:
            field_dict["odpt:ticketType"] = odptticket_type
        if odptpayment_method is not UNSET:
            field_dict["odpt:paymentMethod"] = odptpayment_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = RailwayFareType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptfrom_station = d.pop("odpt:fromStation")

        odptto_station = d.pop("odpt:toStation")

        odptticket_fare = d.pop("odpt:ticketFare")

        dctissued = d.pop("dct:issued", UNSET)

        dctvalid = d.pop("dct:valid", UNSET)

        odptic_card_fare = d.pop("odpt:icCardFare", UNSET)

        odptchild_ticket_fare = d.pop("odpt:childTicketFare", UNSET)

        odptchild_ic_card_fare = d.pop("odpt:childIcCardFare", UNSET)

        odptvia_station = cast(List[str], d.pop("odpt:viaStation", UNSET))

        odptvia_railway = cast(List[str], d.pop("odpt:viaRailway", UNSET))

        odptticket_type = d.pop("odpt:ticketType", UNSET)

        odptpayment_method = cast(List[str], d.pop("odpt:paymentMethod", UNSET))

        railway_fare = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptfrom_station=odptfrom_station,
            odptto_station=odptto_station,
            odptticket_fare=odptticket_fare,
            dctissued=dctissued,
            dctvalid=dctvalid,
            odptic_card_fare=odptic_card_fare,
            odptchild_ticket_fare=odptchild_ticket_fare,
            odptchild_ic_card_fare=odptchild_ic_card_fare,
            odptvia_station=odptvia_station,
            odptvia_railway=odptvia_railway,
            odptticket_type=odptticket_type,
            odptpayment_method=odptpayment_method,
        )

        railway_fare.additional_properties = d
        return railway_fare

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
