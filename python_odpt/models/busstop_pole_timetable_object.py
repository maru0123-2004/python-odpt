from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusstopPoleTimetableObject")


@_attrs_define
class BusstopPoleTimetableObject:
    """バス停(標柱)時刻表の時分情報

    Attributes:
        odptdeparture_time (str): ISO8601 時刻形式
        odptarrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptdestination_busstop_pole (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptdestination_sign (Union[Unset, str]): 行先(方向幕)情報 Example: 南大沢駅.
        odptbusroute_pattern (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptbusroute_pattern_order (Union[Unset, int]): 系統パターン内の停留所(標柱)通過順。odpt:busroutePattern の示す odpt:BusroutePattern
            の odpt:busstopPoleOrder の odpt:index と同じ値。
        odptis_non_step_bus (Union[Unset, bool]): ノンステップバスの場合 true Example: True.
        odptis_midnight (Union[Unset, bool]): 深夜バスの場合 true Example: True.
        odptcan_get_on (Union[Unset, bool]): 乗車可能な場合 true Example: True.
        odptcan_get_off (Union[Unset, bool]): 降車可能な場合 true Example: True.
        odptnote (Union[Unset, str]): 注記 Example: 南大沢駅行.
    """

    odptdeparture_time: str
    odptarrival_time: Union[Unset, str] = UNSET
    odptdestination_busstop_pole: Union[Unset, str] = UNSET
    odptdestination_sign: Union[Unset, str] = UNSET
    odptbusroute_pattern: Union[Unset, str] = UNSET
    odptbusroute_pattern_order: Union[Unset, int] = UNSET
    odptis_non_step_bus: Union[Unset, bool] = UNSET
    odptis_midnight: Union[Unset, bool] = UNSET
    odptcan_get_on: Union[Unset, bool] = UNSET
    odptcan_get_off: Union[Unset, bool] = UNSET
    odptnote: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptdeparture_time = self.odptdeparture_time

        odptarrival_time = self.odptarrival_time

        odptdestination_busstop_pole = self.odptdestination_busstop_pole

        odptdestination_sign = self.odptdestination_sign

        odptbusroute_pattern = self.odptbusroute_pattern

        odptbusroute_pattern_order = self.odptbusroute_pattern_order

        odptis_non_step_bus = self.odptis_non_step_bus

        odptis_midnight = self.odptis_midnight

        odptcan_get_on = self.odptcan_get_on

        odptcan_get_off = self.odptcan_get_off

        odptnote = self.odptnote

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odpt:departureTime": odptdeparture_time,
            }
        )
        if odptarrival_time is not UNSET:
            field_dict["odpt:arrivalTime"] = odptarrival_time
        if odptdestination_busstop_pole is not UNSET:
            field_dict["odpt:destinationBusstopPole"] = odptdestination_busstop_pole
        if odptdestination_sign is not UNSET:
            field_dict["odpt:destinationSign"] = odptdestination_sign
        if odptbusroute_pattern is not UNSET:
            field_dict["odpt:busroutePattern"] = odptbusroute_pattern
        if odptbusroute_pattern_order is not UNSET:
            field_dict["odpt:busroutePatternOrder"] = odptbusroute_pattern_order
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
        odptdeparture_time = d.pop("odpt:departureTime")

        odptarrival_time = d.pop("odpt:arrivalTime", UNSET)

        odptdestination_busstop_pole = d.pop("odpt:destinationBusstopPole", UNSET)

        odptdestination_sign = d.pop("odpt:destinationSign", UNSET)

        odptbusroute_pattern = d.pop("odpt:busroutePattern", UNSET)

        odptbusroute_pattern_order = d.pop("odpt:busroutePatternOrder", UNSET)

        odptis_non_step_bus = d.pop("odpt:isNonStepBus", UNSET)

        odptis_midnight = d.pop("odpt:isMidnight", UNSET)

        odptcan_get_on = d.pop("odpt:canGetOn", UNSET)

        odptcan_get_off = d.pop("odpt:canGetOff", UNSET)

        odptnote = d.pop("odpt:note", UNSET)

        busstop_pole_timetable_object = cls(
            odptdeparture_time=odptdeparture_time,
            odptarrival_time=odptarrival_time,
            odptdestination_busstop_pole=odptdestination_busstop_pole,
            odptdestination_sign=odptdestination_sign,
            odptbusroute_pattern=odptbusroute_pattern,
            odptbusroute_pattern_order=odptbusroute_pattern_order,
            odptis_non_step_bus=odptis_non_step_bus,
            odptis_midnight=odptis_midnight,
            odptcan_get_on=odptcan_get_on,
            odptcan_get_off=odptcan_get_off,
            odptnote=odptnote,
        )

        busstop_pole_timetable_object.additional_properties = d
        return busstop_pole_timetable_object

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
