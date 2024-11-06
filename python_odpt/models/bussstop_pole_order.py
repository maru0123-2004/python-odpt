from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opening_door import OpeningDoor
from ..types import UNSET, Unset

T = TypeVar("T", bound="BussstopPoleOrder")


@_attrs_define
class BussstopPoleOrder:
    """停留所(標柱)の順序

    Attributes:
        odptbusstop_pole (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptindex (int): 停留所通過順。通過順の昇順の値となる Example: 1.
        odptopening_doors_to_get_on (Union[Unset, List[OpeningDoor]]): 乗車時に利用可能なドア Example:
            ['odpt:OpeningDoor:FrontSide'].
        odptopening_doors_to_get_off (Union[Unset, List[OpeningDoor]]): 降車時に利用可能なドア Example:
            ['odpt:OpeningDoor:FrontSide'].
        odptnote (Union[Unset, str]): 注記
    """

    odptbusstop_pole: str
    odptindex: int
    odptopening_doors_to_get_on: Union[Unset, List[OpeningDoor]] = UNSET
    odptopening_doors_to_get_off: Union[Unset, List[OpeningDoor]] = UNSET
    odptnote: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptbusstop_pole = self.odptbusstop_pole

        odptindex = self.odptindex

        odptopening_doors_to_get_on: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptopening_doors_to_get_on, Unset):
            odptopening_doors_to_get_on = []
            for odptopening_doors_to_get_on_item_data in self.odptopening_doors_to_get_on:
                odptopening_doors_to_get_on_item = odptopening_doors_to_get_on_item_data.value
                odptopening_doors_to_get_on.append(odptopening_doors_to_get_on_item)

        odptopening_doors_to_get_off: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptopening_doors_to_get_off, Unset):
            odptopening_doors_to_get_off = []
            for odptopening_doors_to_get_off_item_data in self.odptopening_doors_to_get_off:
                odptopening_doors_to_get_off_item = odptopening_doors_to_get_off_item_data.value
                odptopening_doors_to_get_off.append(odptopening_doors_to_get_off_item)

        odptnote = self.odptnote

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odpt:busstopPole": odptbusstop_pole,
                "odpt:index": odptindex,
            }
        )
        if odptopening_doors_to_get_on is not UNSET:
            field_dict["odpt:openingDoorsToGetOn"] = odptopening_doors_to_get_on
        if odptopening_doors_to_get_off is not UNSET:
            field_dict["odpt:openingDoorsToGetOff"] = odptopening_doors_to_get_off
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        odptbusstop_pole = d.pop("odpt:busstopPole")

        odptindex = d.pop("odpt:index")

        odptopening_doors_to_get_on = []
        _odptopening_doors_to_get_on = d.pop("odpt:openingDoorsToGetOn", UNSET)
        for odptopening_doors_to_get_on_item_data in _odptopening_doors_to_get_on or []:
            odptopening_doors_to_get_on_item = OpeningDoor(odptopening_doors_to_get_on_item_data)

            odptopening_doors_to_get_on.append(odptopening_doors_to_get_on_item)

        odptopening_doors_to_get_off = []
        _odptopening_doors_to_get_off = d.pop("odpt:openingDoorsToGetOff", UNSET)
        for odptopening_doors_to_get_off_item_data in _odptopening_doors_to_get_off or []:
            odptopening_doors_to_get_off_item = OpeningDoor(odptopening_doors_to_get_off_item_data)

            odptopening_doors_to_get_off.append(odptopening_doors_to_get_off_item)

        odptnote = d.pop("odpt:note", UNSET)

        bussstop_pole_order = cls(
            odptbusstop_pole=odptbusstop_pole,
            odptindex=odptindex,
            odptopening_doors_to_get_on=odptopening_doors_to_get_on,
            odptopening_doors_to_get_off=odptopening_doors_to_get_off,
            odptnote=odptnote,
        )

        bussstop_pole_order.additional_properties = d
        return bussstop_pole_order

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
