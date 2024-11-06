from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="StationOrder")


@_attrs_define
class StationOrder:
    """駅の順序

    Attributes:
        odptstation (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptindex (int): 駅の順序を示す整数値 原則として、列車は進行方向に応じて、この値の昇順または降順に停車する。環状線などの場合は、同一の駅が複数回記載される場合がある。 Example: 1.
        odptstation_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    odptstation: str
    odptindex: int
    odptstation_title: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptstation = self.odptstation

        odptindex = self.odptindex

        odptstation_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptstation_title, Unset):
            odptstation_title = self.odptstation_title.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odpt:station": odptstation,
                "odpt:index": odptindex,
            }
        )
        if odptstation_title is not UNSET:
            field_dict["odpt:stationTitle"] = odptstation_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        odptstation = d.pop("odpt:station")

        odptindex = d.pop("odpt:index")

        _odptstation_title = d.pop("odpt:stationTitle", UNSET)
        odptstation_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptstation_title, Unset):
            odptstation_title = UNSET
        else:
            odptstation_title = MultilingualTitle.from_dict(_odptstation_title)

        station_order = cls(
            odptstation=odptstation,
            odptindex=odptindex,
            odptstation_title=odptstation_title,
        )

        station_order.additional_properties = d
        return station_order

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
