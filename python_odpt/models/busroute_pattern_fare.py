from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.busroute_pattern_fare_type import BusroutePatternFareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BusroutePatternFare")


@_attrs_define
class BusroutePatternFare:
    """乗車バス停(標柱)、降車バス停(標柱)についての運賃情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (BusroutePatternFareType): バス運賃のクラス名、"odpt:BusroutePatternFare"が入る Example: odpt:BusroutePatternFare.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dcdate (str): ISO8601 日付時刻形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptfrom_busroute_pattern (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptfrom_busstop_pole_order (int): 乗車停留所の系統パターン内の停留所 (標柱) 通過順。odpt:fromBusroutePattern の示す odpt:BusroutePattern
            の、 odpt:busstopPoleOrder の odpt:index と同じ値。 Example: 25.
        odptfrom_busstop_pole (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptto_busroute_pattern (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptto_busstop_pole_order (int): 降車停留所の系統パターン内の停留所 (標柱) 通過順。odpt:toBusroutePattern の示す odpt:BusroutePattern の、
            odpt:busstopPoleOrder の odpt:index と同じ値。 Example: 27.
        odptto_busstop_pole (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptticket_fare (int): 切符利用時の運賃 (円) Example: 200.
        dctissued (Union[Unset, str]): ISO8601 日付形式
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptchild_ticket_fare (Union[Unset, int]): 切符利用時の子供運賃 (円) Example: 100.
        odptic_card_fare (Union[Unset, int]): ICカード利用時の運賃 (円) Example: 200.
        odptchild_ic_card_fare (Union[Unset, int]): ICカード利用時の子供運賃 (円) Example: 100.
    """

    context: str
    id: str
    type: BusroutePatternFareType
    owlsame_as: str
    dcdate: str
    odptoperator: str
    odptfrom_busroute_pattern: str
    odptfrom_busstop_pole_order: int
    odptfrom_busstop_pole: str
    odptto_busroute_pattern: str
    odptto_busstop_pole_order: int
    odptto_busstop_pole: str
    odptticket_fare: int
    dctissued: Union[Unset, str] = UNSET
    dctvalid: Union[Unset, str] = UNSET
    odptchild_ticket_fare: Union[Unset, int] = UNSET
    odptic_card_fare: Union[Unset, int] = UNSET
    odptchild_ic_card_fare: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        odptoperator = self.odptoperator

        odptfrom_busroute_pattern = self.odptfrom_busroute_pattern

        odptfrom_busstop_pole_order = self.odptfrom_busstop_pole_order

        odptfrom_busstop_pole = self.odptfrom_busstop_pole

        odptto_busroute_pattern = self.odptto_busroute_pattern

        odptto_busstop_pole_order = self.odptto_busstop_pole_order

        odptto_busstop_pole = self.odptto_busstop_pole

        odptticket_fare = self.odptticket_fare

        dctissued = self.dctissued

        dctvalid = self.dctvalid

        odptchild_ticket_fare = self.odptchild_ticket_fare

        odptic_card_fare = self.odptic_card_fare

        odptchild_ic_card_fare = self.odptchild_ic_card_fare

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "dc:date": dcdate,
                "odpt:operator": odptoperator,
                "odpt:fromBusroutePattern": odptfrom_busroute_pattern,
                "odpt:fromBusstopPoleOrder": odptfrom_busstop_pole_order,
                "odpt:fromBusstopPole": odptfrom_busstop_pole,
                "odpt:toBusroutePattern": odptto_busroute_pattern,
                "odpt:toBusstopPoleOrder": odptto_busstop_pole_order,
                "odpt:toBusstopPole": odptto_busstop_pole,
                "odpt:ticketFare": odptticket_fare,
            }
        )
        if dctissued is not UNSET:
            field_dict["dct:issued"] = dctissued
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptchild_ticket_fare is not UNSET:
            field_dict["odpt:childTicketFare"] = odptchild_ticket_fare
        if odptic_card_fare is not UNSET:
            field_dict["odpt:icCardFare"] = odptic_card_fare
        if odptchild_ic_card_fare is not UNSET:
            field_dict["odpt:childIcCardFare"] = odptchild_ic_card_fare

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = BusroutePatternFareType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date")

        odptoperator = d.pop("odpt:operator")

        odptfrom_busroute_pattern = d.pop("odpt:fromBusroutePattern")

        odptfrom_busstop_pole_order = d.pop("odpt:fromBusstopPoleOrder")

        odptfrom_busstop_pole = d.pop("odpt:fromBusstopPole")

        odptto_busroute_pattern = d.pop("odpt:toBusroutePattern")

        odptto_busstop_pole_order = d.pop("odpt:toBusstopPoleOrder")

        odptto_busstop_pole = d.pop("odpt:toBusstopPole")

        odptticket_fare = d.pop("odpt:ticketFare")

        dctissued = d.pop("dct:issued", UNSET)

        dctvalid = d.pop("dct:valid", UNSET)

        odptchild_ticket_fare = d.pop("odpt:childTicketFare", UNSET)

        odptic_card_fare = d.pop("odpt:icCardFare", UNSET)

        odptchild_ic_card_fare = d.pop("odpt:childIcCardFare", UNSET)

        busroute_pattern_fare = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            odptoperator=odptoperator,
            odptfrom_busroute_pattern=odptfrom_busroute_pattern,
            odptfrom_busstop_pole_order=odptfrom_busstop_pole_order,
            odptfrom_busstop_pole=odptfrom_busstop_pole,
            odptto_busroute_pattern=odptto_busroute_pattern,
            odptto_busstop_pole_order=odptto_busstop_pole_order,
            odptto_busstop_pole=odptto_busstop_pole,
            odptticket_fare=odptticket_fare,
            dctissued=dctissued,
            dctvalid=dctvalid,
            odptchild_ticket_fare=odptchild_ticket_fare,
            odptic_card_fare=odptic_card_fare,
            odptchild_ic_card_fare=odptchild_ic_card_fare,
        )

        busroute_pattern_fare.additional_properties = d
        return busroute_pattern_fare

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
