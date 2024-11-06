from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="StationTimetableObject")


@_attrs_define
class StationTimetableObject:
    """駅時刻表オブジェクト

    Attributes:
        odptarrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptdeparture_time (Union[Unset, str]): ISO8601 時刻形式
        odptorigin_station (Union[Unset, List[str]]): 始発駅を表すIDのリスト Example: ['odpt.Station:JR-East.ChuoRapid.Tokyo'].
        odptdestination_station (Union[Unset, List[str]]): 終着駅を表すIDのリスト Example: ['odpt.Station:JR-
            East.ChuoRapid.Takao'].
        odptvia_station (Union[Unset, List[str]]): 経由駅を表すIDのリスト Example:
            ['odpt.Station:TokyoMetro.Tozai.NishiFunabashi'].
        odptvia_railway (Union[Unset, List[str]]): 経由路線を表すIDのリスト Example: ['odpt.Railway:TokyoMetro.Tozai'].
        odpttrain (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_number (Union[Unset, str]): 列車番号 Example: 123M.
        odpttrain_type (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_name (Union[Unset, List['MultilingualTitle']]): 編成の名称・愛称のリスト Example: [{'ja': 'むさし', 'en':
            'Musashi'}].
        odpttrain_owner (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptis_last (Union[Unset, bool]): 最終電車かどうか Example: True.
        odptis_origin (Union[Unset, bool]): 始発駅かどうか Example: True.
        odptplatform_number (Union[Unset, str]): プラットフォームの番号 Example: 1.
        odptplatform_name (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptcar_composition (Union[Unset, int]): 車両数 Example: 8.
        odptnote (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    odptarrival_time: Union[Unset, str] = UNSET
    odptdeparture_time: Union[Unset, str] = UNSET
    odptorigin_station: Union[Unset, List[str]] = UNSET
    odptdestination_station: Union[Unset, List[str]] = UNSET
    odptvia_station: Union[Unset, List[str]] = UNSET
    odptvia_railway: Union[Unset, List[str]] = UNSET
    odpttrain: Union[Unset, str] = UNSET
    odpttrain_number: Union[Unset, str] = UNSET
    odpttrain_type: Union[Unset, str] = UNSET
    odpttrain_name: Union[Unset, List["MultilingualTitle"]] = UNSET
    odpttrain_owner: Union[Unset, str] = UNSET
    odptis_last: Union[Unset, bool] = UNSET
    odptis_origin: Union[Unset, bool] = UNSET
    odptplatform_number: Union[Unset, str] = UNSET
    odptplatform_name: Union[Unset, "MultilingualTitle"] = UNSET
    odptcar_composition: Union[Unset, int] = UNSET
    odptnote: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptarrival_time = self.odptarrival_time

        odptdeparture_time = self.odptdeparture_time

        odptorigin_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptorigin_station, Unset):
            odptorigin_station = self.odptorigin_station

        odptdestination_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptdestination_station, Unset):
            odptdestination_station = self.odptdestination_station

        odptvia_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_station, Unset):
            odptvia_station = self.odptvia_station

        odptvia_railway: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_railway, Unset):
            odptvia_railway = self.odptvia_railway

        odpttrain = self.odpttrain

        odpttrain_number = self.odpttrain_number

        odpttrain_type = self.odpttrain_type

        odpttrain_name: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.odpttrain_name, Unset):
            odpttrain_name = []
            for odpttrain_name_item_data in self.odpttrain_name:
                odpttrain_name_item = odpttrain_name_item_data.to_dict()
                odpttrain_name.append(odpttrain_name_item)

        odpttrain_owner = self.odpttrain_owner

        odptis_last = self.odptis_last

        odptis_origin = self.odptis_origin

        odptplatform_number = self.odptplatform_number

        odptplatform_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptplatform_name, Unset):
            odptplatform_name = self.odptplatform_name.to_dict()

        odptcar_composition = self.odptcar_composition

        odptnote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptnote, Unset):
            odptnote = self.odptnote.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if odptarrival_time is not UNSET:
            field_dict["odpt:arrivalTime"] = odptarrival_time
        if odptdeparture_time is not UNSET:
            field_dict["odpt:departureTime"] = odptdeparture_time
        if odptorigin_station is not UNSET:
            field_dict["odpt:originStation"] = odptorigin_station
        if odptdestination_station is not UNSET:
            field_dict["odpt:destinationStation"] = odptdestination_station
        if odptvia_station is not UNSET:
            field_dict["odpt:viaStation"] = odptvia_station
        if odptvia_railway is not UNSET:
            field_dict["odpt:viaRailway"] = odptvia_railway
        if odpttrain is not UNSET:
            field_dict["odpt:train"] = odpttrain
        if odpttrain_number is not UNSET:
            field_dict["odpt:trainNumber"] = odpttrain_number
        if odpttrain_type is not UNSET:
            field_dict["odpt:trainType"] = odpttrain_type
        if odpttrain_name is not UNSET:
            field_dict["odpt:trainName"] = odpttrain_name
        if odpttrain_owner is not UNSET:
            field_dict["odpt:trainOwner"] = odpttrain_owner
        if odptis_last is not UNSET:
            field_dict["odpt:isLast"] = odptis_last
        if odptis_origin is not UNSET:
            field_dict["odpt:isOrigin"] = odptis_origin
        if odptplatform_number is not UNSET:
            field_dict["odpt:platformNumber"] = odptplatform_number
        if odptplatform_name is not UNSET:
            field_dict["odpt:platformName"] = odptplatform_name
        if odptcar_composition is not UNSET:
            field_dict["odpt:carComposition"] = odptcar_composition
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        odptarrival_time = d.pop("odpt:arrivalTime", UNSET)

        odptdeparture_time = d.pop("odpt:departureTime", UNSET)

        odptorigin_station = cast(List[str], d.pop("odpt:originStation", UNSET))

        odptdestination_station = cast(List[str], d.pop("odpt:destinationStation", UNSET))

        odptvia_station = cast(List[str], d.pop("odpt:viaStation", UNSET))

        odptvia_railway = cast(List[str], d.pop("odpt:viaRailway", UNSET))

        odpttrain = d.pop("odpt:train", UNSET)

        odpttrain_number = d.pop("odpt:trainNumber", UNSET)

        odpttrain_type = d.pop("odpt:trainType", UNSET)

        odpttrain_name = []
        _odpttrain_name = d.pop("odpt:trainName", UNSET)
        for odpttrain_name_item_data in _odpttrain_name or []:
            odpttrain_name_item = MultilingualTitle.from_dict(odpttrain_name_item_data)

            odpttrain_name.append(odpttrain_name_item)

        odpttrain_owner = d.pop("odpt:trainOwner", UNSET)

        odptis_last = d.pop("odpt:isLast", UNSET)

        odptis_origin = d.pop("odpt:isOrigin", UNSET)

        odptplatform_number = d.pop("odpt:platformNumber", UNSET)

        _odptplatform_name = d.pop("odpt:platformName", UNSET)
        odptplatform_name: Union[Unset, MultilingualTitle]
        if isinstance(_odptplatform_name, Unset):
            odptplatform_name = UNSET
        else:
            odptplatform_name = MultilingualTitle.from_dict(_odptplatform_name)

        odptcar_composition = d.pop("odpt:carComposition", UNSET)

        _odptnote = d.pop("odpt:note", UNSET)
        odptnote: Union[Unset, MultilingualTitle]
        if isinstance(_odptnote, Unset):
            odptnote = UNSET
        else:
            odptnote = MultilingualTitle.from_dict(_odptnote)

        station_timetable_object = cls(
            odptarrival_time=odptarrival_time,
            odptdeparture_time=odptdeparture_time,
            odptorigin_station=odptorigin_station,
            odptdestination_station=odptdestination_station,
            odptvia_station=odptvia_station,
            odptvia_railway=odptvia_railway,
            odpttrain=odpttrain,
            odpttrain_number=odpttrain_number,
            odpttrain_type=odpttrain_type,
            odpttrain_name=odpttrain_name,
            odpttrain_owner=odpttrain_owner,
            odptis_last=odptis_last,
            odptis_origin=odptis_origin,
            odptplatform_number=odptplatform_number,
            odptplatform_name=odptplatform_name,
            odptcar_composition=odptcar_composition,
            odptnote=odptnote,
        )

        station_timetable_object.additional_properties = d
        return station_timetable_object

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
