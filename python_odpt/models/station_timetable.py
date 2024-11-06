from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.station_timetable_type import StationTimetableType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle
    from ..models.station_timetable_object import StationTimetableObject


T = TypeVar("T", bound="StationTimetable")


@_attrs_define
class StationTimetable:
    """駅時刻表情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (StationTimetableType): クラス名 Example: odpt:StationTimetable.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrailway (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptstation_timetable_object (List['StationTimetableObject']): 出発時刻、終着(行先)駅等の組のリスト Example:
            [{'odpt:departureTime': '06:00'}, {'odpt:departureTime': '07:00'}].
        dctissued (Union[Unset, str]): ISO8601 日付形式
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptrailway_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptstation (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptstation_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptrail_direction (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptcalendar (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptnote (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    context: str
    id: str
    type: StationTimetableType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptrailway: str
    odptstation_timetable_object: List["StationTimetableObject"]
    dctissued: Union[Unset, str] = UNSET
    dctvalid: Union[Unset, str] = UNSET
    odptrailway_title: Union[Unset, "MultilingualTitle"] = UNSET
    odptstation: Union[Unset, str] = UNSET
    odptstation_title: Union[Unset, "MultilingualTitle"] = UNSET
    odptrail_direction: Union[Unset, str] = UNSET
    odptcalendar: Union[Unset, str] = UNSET
    odptnote: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptrailway = self.odptrailway

        odptstation_timetable_object = []
        for odptstation_timetable_object_item_data in self.odptstation_timetable_object:
            odptstation_timetable_object_item = odptstation_timetable_object_item_data.to_dict()
            odptstation_timetable_object.append(odptstation_timetable_object_item)

        dctissued = self.dctissued

        dctvalid = self.dctvalid

        odptrailway_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptrailway_title, Unset):
            odptrailway_title = self.odptrailway_title.to_dict()

        odptstation = self.odptstation

        odptstation_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptstation_title, Unset):
            odptstation_title = self.odptstation_title.to_dict()

        odptrail_direction = self.odptrail_direction

        odptcalendar = self.odptcalendar

        odptnote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptnote, Unset):
            odptnote = self.odptnote.to_dict()

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
                "odpt:railway": odptrailway,
                "odpt:stationTimetableObject": odptstation_timetable_object,
            }
        )
        if dctissued is not UNSET:
            field_dict["dct:issued"] = dctissued
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptrailway_title is not UNSET:
            field_dict["odpt:railwayTitle"] = odptrailway_title
        if odptstation is not UNSET:
            field_dict["odpt:station"] = odptstation
        if odptstation_title is not UNSET:
            field_dict["odpt:stationTitle"] = odptstation_title
        if odptrail_direction is not UNSET:
            field_dict["odpt:railDirection"] = odptrail_direction
        if odptcalendar is not UNSET:
            field_dict["odpt:calendar"] = odptcalendar
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle
        from ..models.station_timetable_object import StationTimetableObject

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = StationTimetableType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptrailway = d.pop("odpt:railway")

        odptstation_timetable_object = []
        _odptstation_timetable_object = d.pop("odpt:stationTimetableObject")
        for odptstation_timetable_object_item_data in _odptstation_timetable_object:
            odptstation_timetable_object_item = StationTimetableObject.from_dict(odptstation_timetable_object_item_data)

            odptstation_timetable_object.append(odptstation_timetable_object_item)

        dctissued = d.pop("dct:issued", UNSET)

        dctvalid = d.pop("dct:valid", UNSET)

        _odptrailway_title = d.pop("odpt:railwayTitle", UNSET)
        odptrailway_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptrailway_title, Unset):
            odptrailway_title = UNSET
        else:
            odptrailway_title = MultilingualTitle.from_dict(_odptrailway_title)

        odptstation = d.pop("odpt:station", UNSET)

        _odptstation_title = d.pop("odpt:stationTitle", UNSET)
        odptstation_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptstation_title, Unset):
            odptstation_title = UNSET
        else:
            odptstation_title = MultilingualTitle.from_dict(_odptstation_title)

        odptrail_direction = d.pop("odpt:railDirection", UNSET)

        odptcalendar = d.pop("odpt:calendar", UNSET)

        _odptnote = d.pop("odpt:note", UNSET)
        odptnote: Union[Unset, MultilingualTitle]
        if isinstance(_odptnote, Unset):
            odptnote = UNSET
        else:
            odptnote = MultilingualTitle.from_dict(_odptnote)

        station_timetable = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptrailway=odptrailway,
            odptstation_timetable_object=odptstation_timetable_object,
            dctissued=dctissued,
            dctvalid=dctvalid,
            odptrailway_title=odptrailway_title,
            odptstation=odptstation,
            odptstation_title=odptstation_title,
            odptrail_direction=odptrail_direction,
            odptcalendar=odptcalendar,
            odptnote=odptnote,
        )

        station_timetable.additional_properties = d
        return station_timetable

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
