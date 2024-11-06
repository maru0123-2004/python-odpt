from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.busstop_pole_timetable_type import BusstopPoleTimetableType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.busstop_pole_timetable_object import BusstopPoleTimetableObject


T = TypeVar("T", bound="BusstopPoleTimetable")


@_attrs_define
class BusstopPoleTimetable:
    """バス停(標柱)時刻表 odpt:busstopPole で示されたバス停(標柱)の時刻表

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (BusstopPoleTimetableType): バス停(標柱)時刻表のクラス名、"odpt:BusstopPoleTimetable"が入る Example:
            odpt:BusstopPoleTimetable.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dcdate (str): ISO8601 日付時刻形式
        odptbusstop_pole (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbus_direction (Union[List[str], str]): 方面を表すID。array となる場合もある。 Example:
            odpt.BusDirection:KeioBus.Minamioosawaeki.
        odptbusroute (Union[List[str], str]): 路線を表すID。array となる場合もある。(複数路線を含む時刻表の場合等) Example:
            ['odpt.Busroute:KeioBus.Sakura80', 'odpt.Busroute:KeioBus.Sakura88Fu', 'odpt.Busroute:KeioBus.Sakura84',
            'odpt.Busroute:KeioBus.Sakura88', 'odpt.Busroute:KeioBus.Sakura83'].
        odptoperator (Union[List[str], str]): 運行会社を表すID (odpt:Operatorのowl:sameAs) Example: odpt.Operator:KeioBus.
        odptcalendar (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctissued (Union[Unset, str]): ISO8601 日付形式
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): バス路線名称(系統名等) Example: 桜８０、桜８８-ふ、桜８４、桜８８、桜８３:東中野:京王堀之内駅・相模原駅・南大沢駅・由木折返場行:平日.
        odptbusstop_pole_timetable_object (Union[Unset, List['BusstopPoleTimetableObject']]): バス停(標柱)時刻表の時分情報 Example:
            [{'odpt:busroutePattern': 'odpt.BusroutePattern:KeioBus.Sakura80.699.1', 'odpt:departureTime': '06:30',
            'odpt:destinationBusstopPole': 'odpt.BusstopPole:KeioBus.Minamioosawaeki.1395.0', 'odpt:destinationSign':
            '南大沢駅', 'odpt:isMidnight': True, 'odpt:note': '南大沢駅行'}].
    """

    context: str
    id: str
    type: BusstopPoleTimetableType
    owlsame_as: str
    dcdate: str
    odptbusstop_pole: str
    odptbus_direction: Union[List[str], str]
    odptbusroute: Union[List[str], str]
    odptoperator: Union[List[str], str]
    odptcalendar: str
    dctissued: Union[Unset, str] = UNSET
    dctvalid: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odptbusstop_pole_timetable_object: Union[Unset, List["BusstopPoleTimetableObject"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        odptbusstop_pole = self.odptbusstop_pole

        odptbus_direction: Union[List[str], str]
        if isinstance(self.odptbus_direction, list):
            odptbus_direction = self.odptbus_direction

        else:
            odptbus_direction = self.odptbus_direction

        odptbusroute: Union[List[str], str]
        if isinstance(self.odptbusroute, list):
            odptbusroute = self.odptbusroute

        else:
            odptbusroute = self.odptbusroute

        odptoperator: Union[List[str], str]
        if isinstance(self.odptoperator, list):
            odptoperator = self.odptoperator

        else:
            odptoperator = self.odptoperator

        odptcalendar = self.odptcalendar

        dctissued = self.dctissued

        dctvalid = self.dctvalid

        dctitle = self.dctitle

        odptbusstop_pole_timetable_object: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.odptbusstop_pole_timetable_object, Unset):
            odptbusstop_pole_timetable_object = []
            for odptbusstop_pole_timetable_object_item_data in self.odptbusstop_pole_timetable_object:
                odptbusstop_pole_timetable_object_item = odptbusstop_pole_timetable_object_item_data.to_dict()
                odptbusstop_pole_timetable_object.append(odptbusstop_pole_timetable_object_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "dc:date": dcdate,
                "odpt:busstopPole": odptbusstop_pole,
                "odpt:busDirection": odptbus_direction,
                "odpt:busroute": odptbusroute,
                "odpt:operator": odptoperator,
                "odpt:calendar": odptcalendar,
            }
        )
        if dctissued is not UNSET:
            field_dict["dct:issued"] = dctissued
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if dctitle is not UNSET:
            field_dict["dc:title"] = dctitle
        if odptbusstop_pole_timetable_object is not UNSET:
            field_dict["odpt:busstopPoleTimetableObject"] = odptbusstop_pole_timetable_object

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.busstop_pole_timetable_object import BusstopPoleTimetableObject

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = BusstopPoleTimetableType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date")

        odptbusstop_pole = d.pop("odpt:busstopPole")

        def _parse_odptbus_direction(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                odptbus_direction_type_1 = cast(List[str], data)

                return odptbus_direction_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        odptbus_direction = _parse_odptbus_direction(d.pop("odpt:busDirection"))

        def _parse_odptbusroute(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                odptbusroute_type_1 = cast(List[str], data)

                return odptbusroute_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        odptbusroute = _parse_odptbusroute(d.pop("odpt:busroute"))

        def _parse_odptoperator(data: object) -> Union[List[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                odptoperator_type_1 = cast(List[str], data)

                return odptoperator_type_1
            except:  # noqa: E722
                pass
            return cast(Union[List[str], str], data)

        odptoperator = _parse_odptoperator(d.pop("odpt:operator"))

        odptcalendar = d.pop("odpt:calendar")

        dctissued = d.pop("dct:issued", UNSET)

        dctvalid = d.pop("dct:valid", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        odptbusstop_pole_timetable_object = []
        _odptbusstop_pole_timetable_object = d.pop("odpt:busstopPoleTimetableObject", UNSET)
        for odptbusstop_pole_timetable_object_item_data in _odptbusstop_pole_timetable_object or []:
            odptbusstop_pole_timetable_object_item = BusstopPoleTimetableObject.from_dict(
                odptbusstop_pole_timetable_object_item_data
            )

            odptbusstop_pole_timetable_object.append(odptbusstop_pole_timetable_object_item)

        busstop_pole_timetable = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            odptbusstop_pole=odptbusstop_pole,
            odptbus_direction=odptbus_direction,
            odptbusroute=odptbusroute,
            odptoperator=odptoperator,
            odptcalendar=odptcalendar,
            dctissued=dctissued,
            dctvalid=dctvalid,
            dctitle=dctitle,
            odptbusstop_pole_timetable_object=odptbusstop_pole_timetable_object,
        )

        busstop_pole_timetable.additional_properties = d
        return busstop_pole_timetable

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
