from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.airport_type import AirportType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.airport_ugregion import AirportUgregion
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="Airport")


@_attrs_define
class Airport:
    """空港の情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (AirportType): クラス名
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): 空港名(日本語)
        odptairport_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptairport_terminal (Union[Unset, List[str]]): 空港のターミナルを表す ID のリスト
        geolong (Union[Unset, float]): 代表点の経度
        geolat (Union[Unset, float]): 代表点の緯度
        ugregion (Union[Unset, AirportUgregion]): GeoJSON形式による地物情報
    """

    context: str
    id: str
    type: AirportType
    owlsame_as: str
    dcdate: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odptairport_title: Union[Unset, "MultilingualTitle"] = UNSET
    odptairport_terminal: Union[Unset, List[str]] = UNSET
    geolong: Union[Unset, float] = UNSET
    geolat: Union[Unset, float] = UNSET
    ugregion: Union[Unset, "AirportUgregion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        dcdate = self.dcdate

        dctitle = self.dctitle

        odptairport_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptairport_title, Unset):
            odptairport_title = self.odptairport_title.to_dict()

        odptairport_terminal: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptairport_terminal, Unset):
            odptairport_terminal = self.odptairport_terminal

        geolong = self.geolong

        geolat = self.geolat

        ugregion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ugregion, Unset):
            ugregion = self.ugregion.to_dict()

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
        if odptairport_title is not UNSET:
            field_dict["odpt:airportTitle"] = odptairport_title
        if odptairport_terminal is not UNSET:
            field_dict["odpt:airportTerminal"] = odptairport_terminal
        if geolong is not UNSET:
            field_dict["geo:long"] = geolong
        if geolat is not UNSET:
            field_dict["geo:lat"] = geolat
        if ugregion is not UNSET:
            field_dict["ug:region"] = ugregion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.airport_ugregion import AirportUgregion
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = AirportType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        dcdate = d.pop("dc:date", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        _odptairport_title = d.pop("odpt:airportTitle", UNSET)
        odptairport_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptairport_title, Unset):
            odptairport_title = UNSET
        else:
            odptairport_title = MultilingualTitle.from_dict(_odptairport_title)

        odptairport_terminal = cast(List[str], d.pop("odpt:airportTerminal", UNSET))

        geolong = d.pop("geo:long", UNSET)

        geolat = d.pop("geo:lat", UNSET)

        _ugregion = d.pop("ug:region", UNSET)
        ugregion: Union[Unset, AirportUgregion]
        if isinstance(_ugregion, Unset):
            ugregion = UNSET
        else:
            ugregion = AirportUgregion.from_dict(_ugregion)

        airport = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            dcdate=dcdate,
            dctitle=dctitle,
            odptairport_title=odptairport_title,
            odptairport_terminal=odptairport_terminal,
            geolong=geolong,
            geolat=geolat,
            ugregion=ugregion,
        )

        airport.additional_properties = d
        return airport

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
