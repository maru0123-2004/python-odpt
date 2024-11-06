from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.busroute_pattern_type import BusroutePatternType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.busroute_pattern_ugregion import BusroutePatternUgregion
    from ..models.bussstop_pole_order import BussstopPoleOrder


T = TypeVar("T", bound="BusroutePattern")


@_attrs_define
class BusroutePattern:
    """バス路線の系統情報
    `odpt:busstopPoleOrder` が、運行するバスの停車する停留所 (標柱) の順序を表現している。
    バス路線 ('王５７'等) は、通常、複数の系統情報から構成される。
    (e.g. 往路、復路、異なる停留所通過順のバリエーション)

        Attributes:
            context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt_BusroutePattern.jsonld.
            id (str): 固有識別子
            type (BusroutePatternType): バス路線情報のクラス名、"odpt:BusroutePattern"が入る Example: odpt:BusroutePattern.
            owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            dcdate (str): ISO8601 日付時刻形式
            dctitle (str): バス路線名称(系統名・系統番号等) Example: 直通.
            odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptbusstop_pole_order (List['BussstopPoleOrder']): 停留所(標柱)の順序 Example: [{'odpt:busstopPole':
                'odpt.BusstopPole:NishiTokyoBus.JRHachiojiStationNorthExit.390.15', 'odpt:index': 1, 'odpt:openingDoorsToGetOn':
                ['odpt:OpeningDoor:FrontSide'], 'odpt:openingDoorsToGetOff': ['odpt:OpeningDoor:FrontSide']}].
            dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
            odptkana (Union[Unset, str]): バス路線名称のよみがな Example: ちょくつう.
            odptbusroute (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptpattern (Union[Unset, str]): 系統パターン Example: 500102.
            odptdirection (Union[Unset, str]): 方向 Example: 2.
            ugregion (Union[Unset, BusroutePatternUgregion]): GeoJSON形式による地物情報
            odptnote (Union[Unset, str]): 注記 Example: 036系統::03618.03_1.
            odptbus_location_url (Union[Unset, str]): バス位置情報を示すWebSiteのURL
    """

    context: str
    id: str
    type: BusroutePatternType
    owlsame_as: str
    dcdate: str
    dctitle: str
    odptoperator: str
    odptbusstop_pole_order: List["BussstopPoleOrder"]
    dctvalid: Union[Unset, str] = UNSET
    odptkana: Union[Unset, str] = UNSET
    odptbusroute: Union[Unset, str] = UNSET
    odptpattern: Union[Unset, str] = UNSET
    odptdirection: Union[Unset, str] = UNSET
    ugregion: Union[Unset, "BusroutePatternUgregion"] = UNSET
    odptnote: Union[Unset, str] = UNSET
    odptbus_location_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        dctitle = self.dctitle

        odptoperator = self.odptoperator

        odptbusstop_pole_order = []
        for odptbusstop_pole_order_item_data in self.odptbusstop_pole_order:
            odptbusstop_pole_order_item = odptbusstop_pole_order_item_data.to_dict()
            odptbusstop_pole_order.append(odptbusstop_pole_order_item)

        dctvalid = self.dctvalid

        odptkana = self.odptkana

        odptbusroute = self.odptbusroute

        odptpattern = self.odptpattern

        odptdirection = self.odptdirection

        ugregion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ugregion, Unset):
            ugregion = self.ugregion.to_dict()

        odptnote = self.odptnote

        odptbus_location_url = self.odptbus_location_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "dc:date": dcdate,
                "dc:title": dctitle,
                "odpt:operator": odptoperator,
                "odpt:busstopPoleOrder": odptbusstop_pole_order,
            }
        )
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptkana is not UNSET:
            field_dict["odpt:kana"] = odptkana
        if odptbusroute is not UNSET:
            field_dict["odpt:busroute"] = odptbusroute
        if odptpattern is not UNSET:
            field_dict["odpt:pattern"] = odptpattern
        if odptdirection is not UNSET:
            field_dict["odpt:direction"] = odptdirection
        if ugregion is not UNSET:
            field_dict["ug:region"] = ugregion
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote
        if odptbus_location_url is not UNSET:
            field_dict["odpt:busLocationURL"] = odptbus_location_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.busroute_pattern_ugregion import BusroutePatternUgregion
        from ..models.bussstop_pole_order import BussstopPoleOrder

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = BusroutePatternType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date")

        dctitle = d.pop("dc:title")

        odptoperator = d.pop("odpt:operator")

        odptbusstop_pole_order = []
        _odptbusstop_pole_order = d.pop("odpt:busstopPoleOrder")
        for odptbusstop_pole_order_item_data in _odptbusstop_pole_order:
            odptbusstop_pole_order_item = BussstopPoleOrder.from_dict(odptbusstop_pole_order_item_data)

            odptbusstop_pole_order.append(odptbusstop_pole_order_item)

        dctvalid = d.pop("dct:valid", UNSET)

        odptkana = d.pop("odpt:kana", UNSET)

        odptbusroute = d.pop("odpt:busroute", UNSET)

        odptpattern = d.pop("odpt:pattern", UNSET)

        odptdirection = d.pop("odpt:direction", UNSET)

        _ugregion = d.pop("ug:region", UNSET)
        ugregion: Union[Unset, BusroutePatternUgregion]
        if isinstance(_ugregion, Unset):
            ugregion = UNSET
        else:
            ugregion = BusroutePatternUgregion.from_dict(_ugregion)

        odptnote = d.pop("odpt:note", UNSET)

        odptbus_location_url = d.pop("odpt:busLocationURL", UNSET)

        busroute_pattern = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            dctitle=dctitle,
            odptoperator=odptoperator,
            odptbusstop_pole_order=odptbusstop_pole_order,
            dctvalid=dctvalid,
            odptkana=odptkana,
            odptbusroute=odptbusroute,
            odptpattern=odptpattern,
            odptdirection=odptdirection,
            ugregion=ugregion,
            odptnote=odptnote,
            odptbus_location_url=odptbus_location_url,
        )

        busroute_pattern.additional_properties = d
        return busroute_pattern

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
