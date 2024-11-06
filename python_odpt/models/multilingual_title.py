from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultilingualTitle")


@_attrs_define
class MultilingualTitle:
    """多言語対応のタイトル

    Attributes:
        ja (str):
        en (str):
        ko (Union[Unset, str]):
        ja_hrkt (Union[Unset, str]):
        zh_hans (Union[Unset, str]):
        zh_hant (Union[Unset, str]):
    """

    ja: str
    en: str
    ko: Union[Unset, str] = UNSET
    ja_hrkt: Union[Unset, str] = UNSET
    zh_hans: Union[Unset, str] = UNSET
    zh_hant: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ja = self.ja

        en = self.en

        ko = self.ko

        ja_hrkt = self.ja_hrkt

        zh_hans = self.zh_hans

        zh_hant = self.zh_hant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ja": ja,
                "en": en,
            }
        )
        if ko is not UNSET:
            field_dict["ko"] = ko
        if ja_hrkt is not UNSET:
            field_dict["ja-Hrkt"] = ja_hrkt
        if zh_hans is not UNSET:
            field_dict["zh-Hans"] = zh_hans
        if zh_hant is not UNSET:
            field_dict["zh-Hant"] = zh_hant

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ja = d.pop("ja")

        en = d.pop("en")

        ko = d.pop("ko", UNSET)

        ja_hrkt = d.pop("ja-Hrkt", UNSET)

        zh_hans = d.pop("zh-Hans", UNSET)

        zh_hant = d.pop("zh-Hant", UNSET)

        multilingual_title = cls(
            ja=ja,
            en=en,
            ko=ko,
            ja_hrkt=ja_hrkt,
            zh_hans=zh_hans,
            zh_hant=zh_hant,
        )

        multilingual_title.additional_properties = d
        return multilingual_title

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
