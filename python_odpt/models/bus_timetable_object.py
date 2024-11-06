from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusTimetableObject")


@_attrs_define
class BusTimetableObject:
    """バス時刻表時分情報

    Attributes:
        odptindex (int): 標柱通過順
        odptbusstop_pole (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptarrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptdeparture_time (Union[Unset, str]): ISO8601 時刻形式
        odptdestination_sign (Union[Unset, str]): 行先(方向幕)情報 Example: ( 桜ケ丘 経由 ) 横浜駅西口 行.
        odptis_non_step_bus (Union[Unset, bool]): ノンステップバスの場合 true Example: True.
        odptis_midnight (Union[Unset, bool]): 深夜バスの場合 true Example: True.
        odptcan_get_on (Union[Unset, bool]): 乗車可能な場合 true Example: True.
        odptcan_get_off (Union[Unset, bool]): 降車可能な場合 true Example: True.
        odptnote (Union[Unset, str]): 注記 Example: 蔵境駅南口:10140:3.
    """

    odptindex: int
    odptbusstop_pole: str
    odptarrival_time: Union[Unset, str] = UNSET
    odptdeparture_time: Union[Unset, str] = UNSET
    odptdestination_sign: Union[Unset, str] = UNSET
    odptis_non_step_bus: Union[Unset, bool] = UNSET
    odptis_midnight: Union[Unset, bool] = UNSET
    odptcan_get_on: Union[Unset, bool] = UNSET
    odptcan_get_off: Union[Unset, bool] = UNSET
    odptnote: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptindex = self.odptindex

        odptbusstop_pole = self.odptbusstop_pole

        odptarrival_time = self.odptarrival_time

        odptdeparture_time = self.odptdeparture_time

        odptdestination_sign = self.odptdestination_sign

        odptis_non_step_bus = self.odptis_non_step_bus

        odptis_midnight = self.odptis_midnight

        odptcan_get_on = self.odptcan_get_on

        odptcan_get_off = self.odptcan_get_off

        odptnote = self.odptnote

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odpt:index": odptindex,
                "odpt:busstopPole": odptbusstop_pole,
            }
        )
        if odptarrival_time is not UNSET:
            field_dict["odpt:arrivalTime"] = odptarrival_time
        if odptdeparture_time is not UNSET:
            field_dict["odpt:departureTime"] = odptdeparture_time
        if odptdestination_sign is not UNSET:
            field_dict["odpt:destinationSign"] = odptdestination_sign
        if odptis_non_step_bus is not UNSET:
            field_dict["odpt:isNonStepBus"] = odptis_non_step_bus
        if odptis_midnight is not UNSET:
            field_dict["odpt:isMidnight"] = odptis_midnight
        if odptcan_get_on is not UNSET:
            field_dict["odpt:canGetOn"] = odptcan_get_on
        if odptcan_get_off is not UNSET:
            field_dict["odpt:canGetOff"] = odptcan_get_off
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        odptindex = d.pop("odpt:index")

        odptbusstop_pole = d.pop("odpt:busstopPole")

        odptarrival_time = d.pop("odpt:arrivalTime", UNSET)

        odptdeparture_time = d.pop("odpt:departureTime", UNSET)

        odptdestination_sign = d.pop("odpt:destinationSign", UNSET)

        odptis_non_step_bus = d.pop("odpt:isNonStepBus", UNSET)

        odptis_midnight = d.pop("odpt:isMidnight", UNSET)

        odptcan_get_on = d.pop("odpt:canGetOn", UNSET)

        odptcan_get_off = d.pop("odpt:canGetOff", UNSET)

        odptnote = d.pop("odpt:note", UNSET)

        bus_timetable_object = cls(
            odptindex=odptindex,
            odptbusstop_pole=odptbusstop_pole,
            odptarrival_time=odptarrival_time,
            odptdeparture_time=odptdeparture_time,
            odptdestination_sign=odptdestination_sign,
            odptis_non_step_bus=odptis_non_step_bus,
            odptis_midnight=odptis_midnight,
            odptcan_get_on=odptcan_get_on,
            odptcan_get_off=odptcan_get_off,
            odptnote=odptnote,
        )

        bus_timetable_object.additional_properties = d
        return bus_timetable_object

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
