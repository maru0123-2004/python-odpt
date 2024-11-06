from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DumpResponse")


@_attrs_define
class DumpResponse:
    """データダンプAPIのレスポンス

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (str): クラス名 Example: odpt:Station.
        dctitle (str): 駅名(日本語) Example: 東京.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
    """

    context: str
    id: str
    type: str
    dctitle: str
    owlsame_as: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type

        dctitle = self.dctitle

        owlsame_as = self.owlsame_as

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:title": dctitle,
                "owl:sameAs": owlsame_as,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = d.pop("@type")

        dctitle = d.pop("dc:title")

        owlsame_as = d.pop("owl:sameAs")

        dump_response = cls(
            context=context,
            id=id,
            type=type,
            dctitle=dctitle,
            owlsame_as=owlsame_as,
        )

        dump_response.additional_properties = d
        return dump_response

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
