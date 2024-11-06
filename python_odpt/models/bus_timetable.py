from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bus_timetable_type import BusTimetableType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bus_timetable_object import BusTimetableObject


T = TypeVar("T", bound="BusTimetable")


@_attrs_define
class BusTimetable:
    """バスの便の時刻表

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt_BusTimetable.jsonld.
        id (str): 固有識別子
        type (BusTimetableType): バス時刻表のクラス名、"odpt:BusTimetable"が入る Example: odpt:BusTimetable.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbusroute_pattern (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptcalendar (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbus_timetable_object (List['BusTimetableObject']): バス時刻表時分情報 Example: [{'odpt:note': '武蔵境駅南口:10140:3',
            'odpt:index': 0, 'odpt:canGetOn': True, 'odpt:canGetOff': False, 'odpt:isMidnight': False, 'odpt:arrivalTime':
            '12:36', 'odpt:busstopPole': 'odpt.BusstopPole:OdakyuBus.Musashisakaiekiminamiguchi.10140.3',
            'odpt:departureTime': '12:36'}].
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        dctissued (Union[Unset, str]): ISO8601 日付形式
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): バス路線名称(系統名等) Example: 境９１.
        odptkana (Union[Unset, str]): バス路線名称のよみがな Example: さかいきゅうじゅういち.
    """

    context: str
    id: str
    type: BusTimetableType
    owlsame_as: str
    odptoperator: str
    odptbusroute_pattern: str
    odptcalendar: str
    odptbus_timetable_object: List["BusTimetableObject"]
    dcdate: Union[Unset, str] = UNSET
    dctissued: Union[Unset, str] = UNSET
    dctvalid: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odptkana: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptbusroute_pattern = self.odptbusroute_pattern

        odptcalendar = self.odptcalendar

        odptbus_timetable_object = []
        for odptbus_timetable_object_item_data in self.odptbus_timetable_object:
            odptbus_timetable_object_item = odptbus_timetable_object_item_data.to_dict()
            odptbus_timetable_object.append(odptbus_timetable_object_item)

        dcdate = self.dcdate

        dctissued = self.dctissued

        dctvalid = self.dctvalid

        dctitle = self.dctitle

        odptkana = self.odptkana

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "odpt:operator": odptoperator,
                "odpt:busroutePattern": odptbusroute_pattern,
                "odpt:calendar": odptcalendar,
                "odpt:busTimetableObject": odptbus_timetable_object,
            }
        )
        if dcdate is not UNSET:
            field_dict["dc:date"] = dcdate
        if dctissued is not UNSET:
            field_dict["dct:issued"] = dctissued
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if dctitle is not UNSET:
            field_dict["dc:title"] = dctitle
        if odptkana is not UNSET:
            field_dict["odpt:kana"] = odptkana

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bus_timetable_object import BusTimetableObject

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = BusTimetableType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptbusroute_pattern = d.pop("odpt:busroutePattern")

        odptcalendar = d.pop("odpt:calendar")

        odptbus_timetable_object = []
        _odptbus_timetable_object = d.pop("odpt:busTimetableObject")
        for odptbus_timetable_object_item_data in _odptbus_timetable_object:
            odptbus_timetable_object_item = BusTimetableObject.from_dict(odptbus_timetable_object_item_data)

            odptbus_timetable_object.append(odptbus_timetable_object_item)

        dcdate = d.pop("dc:date", UNSET)

        dctissued = d.pop("dct:issued", UNSET)

        dctvalid = d.pop("dct:valid", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        odptkana = d.pop("odpt:kana", UNSET)

        bus_timetable = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptbusroute_pattern=odptbusroute_pattern,
            odptcalendar=odptcalendar,
            odptbus_timetable_object=odptbus_timetable_object,
            dcdate=dcdate,
            dctissued=dctissued,
            dctvalid=dctvalid,
            dctitle=dctitle,
            odptkana=odptkana,
        )

        bus_timetable.additional_properties = d
        return bus_timetable

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
