from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.busstop_pole_type import BusstopPoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="BusstopPole")


@_attrs_define
class BusstopPole:
    """バス停情報 odpt:BusstopPoleは、バス停(標柱)の情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (BusstopPoleType): バス停 (標柱) のクラス名、"odpt:BusstopPole"が入る Example: odpt:BusstopPole.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dcdate (str): ISO8601 日付時刻形式
        dctitle (str): バス停名 Example: 中里.
        odptoperator (List[str]): 入線するバスの運営会社を表すID (odpt:Operatorのowl:sameAs) のリスト Example: ['odpt.Operator:OdakyuBus'].
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptkana (Union[Unset, str]): バス停名のよみがな Example: ナカザト.
        title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        geolong (Union[Unset, float]): 標柱の経度(WGS84) Example: 139.1234.
        geolat (Union[Unset, float]): 標柱の緯度(WGS84) Example: 35.1234.
        odptbusroute_pattern (Union[Unset, List[str]]): 入線する系統パターンのID (odpt:BusroutePatternのowl:sameAs) のリスト Example:
            ['odpt.BusroutePattern:OdakyuBus.Shimo61.20101.2'].
        odptbusstop_pole_number (Union[Unset, str]): 標柱番号。同一停留所の別標柱を区別するものであり、のりば番号とは一致する保証はない Example: 2.
        odptplatform_number (Union[Unset, str]): のりば番号 Example: 1.
        odptbusstop_pole_timetable (Union[Unset, List[str]]): バス停(標柱)時刻表のID (odpt:BusstopPoleTimetableのowl:sameAs) のリスト
    """

    context: str
    id: str
    type: BusstopPoleType
    owlsame_as: str
    dcdate: str
    dctitle: str
    odptoperator: List[str]
    dctvalid: Union[Unset, str] = UNSET
    odptkana: Union[Unset, str] = UNSET
    title: Union[Unset, "MultilingualTitle"] = UNSET
    geolong: Union[Unset, float] = UNSET
    geolat: Union[Unset, float] = UNSET
    odptbusroute_pattern: Union[Unset, List[str]] = UNSET
    odptbusstop_pole_number: Union[Unset, str] = UNSET
    odptplatform_number: Union[Unset, str] = UNSET
    odptbusstop_pole_timetable: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        dctitle = self.dctitle

        odptoperator = self.odptoperator

        dctvalid = self.dctvalid

        odptkana = self.odptkana

        title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        geolong = self.geolong

        geolat = self.geolat

        odptbusroute_pattern: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptbusroute_pattern, Unset):
            odptbusroute_pattern = self.odptbusroute_pattern

        odptbusstop_pole_number = self.odptbusstop_pole_number

        odptplatform_number = self.odptplatform_number

        odptbusstop_pole_timetable: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptbusstop_pole_timetable, Unset):
            odptbusstop_pole_timetable = self.odptbusstop_pole_timetable

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
            }
        )
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptkana is not UNSET:
            field_dict["odpt:kana"] = odptkana
        if title is not UNSET:
            field_dict["title"] = title
        if geolong is not UNSET:
            field_dict["geo:long"] = geolong
        if geolat is not UNSET:
            field_dict["geo:lat"] = geolat
        if odptbusroute_pattern is not UNSET:
            field_dict["odpt:busroutePattern"] = odptbusroute_pattern
        if odptbusstop_pole_number is not UNSET:
            field_dict["odpt:busstopPoleNumber"] = odptbusstop_pole_number
        if odptplatform_number is not UNSET:
            field_dict["odpt:platformNumber"] = odptplatform_number
        if odptbusstop_pole_timetable is not UNSET:
            field_dict["odpt:busstopPoleTimetable"] = odptbusstop_pole_timetable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = BusstopPoleType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date")

        dctitle = d.pop("dc:title")

        odptoperator = cast(List[str], d.pop("odpt:operator"))

        dctvalid = d.pop("dct:valid", UNSET)

        odptkana = d.pop("odpt:kana", UNSET)

        _title = d.pop("title", UNSET)
        title: Union[Unset, MultilingualTitle]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = MultilingualTitle.from_dict(_title)

        geolong = d.pop("geo:long", UNSET)

        geolat = d.pop("geo:lat", UNSET)

        odptbusroute_pattern = cast(List[str], d.pop("odpt:busroutePattern", UNSET))

        odptbusstop_pole_number = d.pop("odpt:busstopPoleNumber", UNSET)

        odptplatform_number = d.pop("odpt:platformNumber", UNSET)

        odptbusstop_pole_timetable = cast(List[str], d.pop("odpt:busstopPoleTimetable", UNSET))

        busstop_pole = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            dctitle=dctitle,
            odptoperator=odptoperator,
            dctvalid=dctvalid,
            odptkana=odptkana,
            title=title,
            geolong=geolong,
            geolat=geolat,
            odptbusroute_pattern=odptbusroute_pattern,
            odptbusstop_pole_number=odptbusstop_pole_number,
            odptplatform_number=odptplatform_number,
            odptbusstop_pole_timetable=odptbusstop_pole_timetable,
        )

        busstop_pole.additional_properties = d
        return busstop_pole

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
