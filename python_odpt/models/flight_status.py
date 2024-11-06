from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_status_type import FlightStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="FlightStatus")


@_attrs_define
class FlightStatus:
    """フライト状況

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (FlightStatusType): クラス名
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): フライト状況(日本語)
        odptflight_status_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    context: str
    id: str
    type: FlightStatusType
    owlsame_as: str
    dcdate: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odptflight_status_title: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        dctitle = self.dctitle

        odptflight_status_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptflight_status_title, Unset):
            odptflight_status_title = self.odptflight_status_title.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
            }
        )
        if dcdate is not UNSET:
            field_dict["dc:date"] = dcdate
        if dctitle is not UNSET:
            field_dict["dc:title"] = dctitle
        if odptflight_status_title is not UNSET:
            field_dict["odpt:flightStatusTitle"] = odptflight_status_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = FlightStatusType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        _odptflight_status_title = d.pop("odpt:flightStatusTitle", UNSET)
        odptflight_status_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptflight_status_title, Unset):
            odptflight_status_title = UNSET
        else:
            odptflight_status_title = MultilingualTitle.from_dict(_odptflight_status_title)

        flight_status = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            dctitle=dctitle,
            odptflight_status_title=odptflight_status_title,
        )

        flight_status.additional_properties = d
        return flight_status

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
