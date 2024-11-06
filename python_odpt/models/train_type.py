from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.train_type_type import TrainTypeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="TrainType")


@_attrs_define
class TrainType:
    """列車種別

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (TrainTypeType): クラス名 Example: odpt:TrainType.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): 列車種別(日本語) Example: 普通.
        odpttrain_type_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    context: str
    id: str
    type: TrainTypeType
    owlsame_as: str
    odptoperator: str
    dcdate: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odpttrain_type_title: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        dcdate = self.dcdate

        dctitle = self.dctitle

        odpttrain_type_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odpttrain_type_title, Unset):
            odpttrain_type_title = self.odpttrain_type_title.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "odpt:operator": odptoperator,
            }
        )
        if dcdate is not UNSET:
            field_dict["dc:date"] = dcdate
        if dctitle is not UNSET:
            field_dict["dc:title"] = dctitle
        if odpttrain_type_title is not UNSET:
            field_dict["odpt:trainTypeTitle"] = odpttrain_type_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = TrainTypeType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        dcdate = d.pop("dc:date", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        _odpttrain_type_title = d.pop("odpt:trainTypeTitle", UNSET)
        odpttrain_type_title: Union[Unset, MultilingualTitle]
        if isinstance(_odpttrain_type_title, Unset):
            odpttrain_type_title = UNSET
        else:
            odpttrain_type_title = MultilingualTitle.from_dict(_odpttrain_type_title)

        train_type = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            dcdate=dcdate,
            dctitle=dctitle,
            odpttrain_type_title=odpttrain_type_title,
        )

        train_type.additional_properties = d
        return train_type

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
