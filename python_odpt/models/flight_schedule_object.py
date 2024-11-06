from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="FlightScheduleObject")


@_attrs_define
class FlightScheduleObject:
    """フライトスケジュールオブジェクト

    Attributes:
        odptairline (str): エアラインの運行会社のID
        odptflight_number (List[str]): フライト番号のリスト
        odptorigin_time (str): ISO8601 時刻形式
        odptdestination_time (str): ISO8601 時刻形式
        odptorigin_day_difference (Union[Unset, int]): 出発日とカレンダー情報の日数差
        odptdestination_day_difference (Union[Unset, int]): 到着日とカレンダー情報の日数差
        odptvia_airport (Union[Unset, List[str]]): 経由地の空港を表すIDのリスト
        odptaircraft_type (Union[Unset, str]): 航空機の機種
        odptis_valid_from (Union[Unset, str]): ISO8601 日付時刻形式
        odptis_valid_to (Union[Unset, str]): ISO8601 日付時刻形式
        odptnote (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    odptairline: str
    odptflight_number: List[str]
    odptorigin_time: str
    odptdestination_time: str
    odptorigin_day_difference: Union[Unset, int] = UNSET
    odptdestination_day_difference: Union[Unset, int] = UNSET
    odptvia_airport: Union[Unset, List[str]] = UNSET
    odptaircraft_type: Union[Unset, str] = UNSET
    odptis_valid_from: Union[Unset, str] = UNSET
    odptis_valid_to: Union[Unset, str] = UNSET
    odptnote: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptairline = self.odptairline

        odptflight_number = self.odptflight_number

        odptorigin_time = self.odptorigin_time

        odptdestination_time = self.odptdestination_time

        odptorigin_day_difference = self.odptorigin_day_difference

        odptdestination_day_difference = self.odptdestination_day_difference

        odptvia_airport: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_airport, Unset):
            odptvia_airport = self.odptvia_airport

        odptaircraft_type = self.odptaircraft_type

        odptis_valid_from = self.odptis_valid_from

        odptis_valid_to = self.odptis_valid_to

        odptnote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptnote, Unset):
            odptnote = self.odptnote.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odpt:airline": odptairline,
                "odpt:flightNumber": odptflight_number,
                "odpt:originTime": odptorigin_time,
                "odpt:destinationTime": odptdestination_time,
            }
        )
        if odptorigin_day_difference is not UNSET:
            field_dict["odpt:originDayDifference"] = odptorigin_day_difference
        if odptdestination_day_difference is not UNSET:
            field_dict["odpt:destinationDayDifference"] = odptdestination_day_difference
        if odptvia_airport is not UNSET:
            field_dict["odpt:viaAirport"] = odptvia_airport
        if odptaircraft_type is not UNSET:
            field_dict["odpt:aircraftType"] = odptaircraft_type
        if odptis_valid_from is not UNSET:
            field_dict["odpt:isValidFrom"] = odptis_valid_from
        if odptis_valid_to is not UNSET:
            field_dict["odpt:isValidTo"] = odptis_valid_to
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        odptairline = d.pop("odpt:airline")

        odptflight_number = cast(List[str], d.pop("odpt:flightNumber"))

        odptorigin_time = d.pop("odpt:originTime")

        odptdestination_time = d.pop("odpt:destinationTime")

        odptorigin_day_difference = d.pop("odpt:originDayDifference", UNSET)

        odptdestination_day_difference = d.pop("odpt:destinationDayDifference", UNSET)

        odptvia_airport = cast(List[str], d.pop("odpt:viaAirport", UNSET))

        odptaircraft_type = d.pop("odpt:aircraftType", UNSET)

        odptis_valid_from = d.pop("odpt:isValidFrom", UNSET)

        odptis_valid_to = d.pop("odpt:isValidTo", UNSET)

        _odptnote = d.pop("odpt:note", UNSET)
        odptnote: Union[Unset, MultilingualTitle]
        if isinstance(_odptnote, Unset):
            odptnote = UNSET
        else:
            odptnote = MultilingualTitle.from_dict(_odptnote)

        flight_schedule_object = cls(
            odptairline=odptairline,
            odptflight_number=odptflight_number,
            odptorigin_time=odptorigin_time,
            odptdestination_time=odptdestination_time,
            odptorigin_day_difference=odptorigin_day_difference,
            odptdestination_day_difference=odptdestination_day_difference,
            odptvia_airport=odptvia_airport,
            odptaircraft_type=odptaircraft_type,
            odptis_valid_from=odptis_valid_from,
            odptis_valid_to=odptis_valid_to,
            odptnote=odptnote,
        )

        flight_schedule_object.additional_properties = d
        return flight_schedule_object

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
