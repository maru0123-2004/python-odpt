from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calendar_type import CalendarType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="Calendar")


@_attrs_define
class Calendar:
    """曜日・日付区分を扱うクラス

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (CalendarType): クラス指定
        owlsame_as (str): 固有識別子
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): カレンダー名称(日本語)
        odptcalendar_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    context: str
    id: str
    type: CalendarType
    owlsame_as: str
    dcdate: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odptcalendar_title: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        dctitle = self.dctitle

        odptcalendar_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptcalendar_title, Unset):
            odptcalendar_title = self.odptcalendar_title.to_dict()

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
        if odptcalendar_title is not UNSET:
            field_dict["odpt:calendarTitle"] = odptcalendar_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = CalendarType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        _odptcalendar_title = d.pop("odpt:calendarTitle", UNSET)
        odptcalendar_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptcalendar_title, Unset):
            odptcalendar_title = UNSET
        else:
            odptcalendar_title = MultilingualTitle.from_dict(_odptcalendar_title)

        calendar = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            dctitle=dctitle,
            odptcalendar_title=odptcalendar_title,
        )

        calendar.additional_properties = d
        return calendar

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
