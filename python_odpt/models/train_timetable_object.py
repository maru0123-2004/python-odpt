from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="TrainTimetableObject")


@_attrs_define
class TrainTimetableObject:
    """列車時刻表オブジェクト

    Attributes:
        odptarrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptarrival_station (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptdeparture_time (Union[Unset, str]): ISO8601 時刻形式
        odptdeparture_station (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptplatform_number (Union[Unset, str]): プラットフォームの番号 Example: 1.
        odptplatform_name (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptnote (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    odptarrival_time: Union[Unset, str] = UNSET
    odptarrival_station: Union[Unset, str] = UNSET
    odptdeparture_time: Union[Unset, str] = UNSET
    odptdeparture_station: Union[Unset, str] = UNSET
    odptplatform_number: Union[Unset, str] = UNSET
    odptplatform_name: Union[Unset, "MultilingualTitle"] = UNSET
    odptnote: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptarrival_time = self.odptarrival_time

        odptarrival_station = self.odptarrival_station

        odptdeparture_time = self.odptdeparture_time

        odptdeparture_station = self.odptdeparture_station

        odptplatform_number = self.odptplatform_number

        odptplatform_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptplatform_name, Unset):
            odptplatform_name = self.odptplatform_name.to_dict()

        odptnote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptnote, Unset):
            odptnote = self.odptnote.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if odptarrival_time is not UNSET:
            field_dict["odpt:arrivalTime"] = odptarrival_time
        if odptarrival_station is not UNSET:
            field_dict["odpt:arrivalStation"] = odptarrival_station
        if odptdeparture_time is not UNSET:
            field_dict["odpt:departureTime"] = odptdeparture_time
        if odptdeparture_station is not UNSET:
            field_dict["odpt:departureStation"] = odptdeparture_station
        if odptplatform_number is not UNSET:
            field_dict["odpt:platformNumber"] = odptplatform_number
        if odptplatform_name is not UNSET:
            field_dict["odpt:platformName"] = odptplatform_name
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        odptarrival_time = d.pop("odpt:arrivalTime", UNSET)

        odptarrival_station = d.pop("odpt:arrivalStation", UNSET)

        odptdeparture_time = d.pop("odpt:departureTime", UNSET)

        odptdeparture_station = d.pop("odpt:departureStation", UNSET)

        odptplatform_number = d.pop("odpt:platformNumber", UNSET)

        _odptplatform_name = d.pop("odpt:platformName", UNSET)
        odptplatform_name: Union[Unset, MultilingualTitle]
        if isinstance(_odptplatform_name, Unset):
            odptplatform_name = UNSET
        else:
            odptplatform_name = MultilingualTitle.from_dict(_odptplatform_name)

        _odptnote = d.pop("odpt:note", UNSET)
        odptnote: Union[Unset, MultilingualTitle]
        if isinstance(_odptnote, Unset):
            odptnote = UNSET
        else:
            odptnote = MultilingualTitle.from_dict(_odptnote)

        train_timetable_object = cls(
            odptarrival_time=odptarrival_time,
            odptarrival_station=odptarrival_station,
            odptdeparture_time=odptdeparture_time,
            odptdeparture_station=odptdeparture_station,
            odptplatform_number=odptplatform_number,
            odptplatform_name=odptplatform_name,
            odptnote=odptnote,
        )

        train_timetable_object.additional_properties = d
        return train_timetable_object

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
