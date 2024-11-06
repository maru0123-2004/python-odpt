from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.airport_terminal_type import AirportTerminalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.airport_terminal_ugregion import AirportTerminalUgregion
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="AirportTerminal")


@_attrs_define
class AirportTerminal:
    """空港のターミナルの情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (AirportTerminalType): クラス名
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptairport (str): 空港を示すID
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        dctitle (Union[Unset, str]): 空港ターミナル名(日本語)
        odptairport_terminal_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        geolong (Union[Unset, float]): 代表点の経度
        geolat (Union[Unset, float]): 代表点の緯度
        ugregion (Union[Unset, AirportTerminalUgregion]): GeoJSON形式による地物情報
    """

    context: str
    id: str
    type: AirportTerminalType
    owlsame_as: str
    odptairport: str
    dcdate: Union[Unset, str] = UNSET
    dctitle: Union[Unset, str] = UNSET
    odptairport_terminal_title: Union[Unset, "MultilingualTitle"] = UNSET
    geolong: Union[Unset, float] = UNSET
    geolat: Union[Unset, float] = UNSET
    ugregion: Union[Unset, "AirportTerminalUgregion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        odptairport = self.odptairport

        dcdate = self.dcdate

        dctitle = self.dctitle

        odptairport_terminal_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptairport_terminal_title, Unset):
            odptairport_terminal_title = self.odptairport_terminal_title.to_dict()

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
                "odpt:airport": odptairport,
            }
        )
        if dcdate is not UNSET:
            field_dict["dc:date"] = dcdate
        if dctitle is not UNSET:
            field_dict["dc:title"] = dctitle
        if odptairport_terminal_title is not UNSET:
            field_dict["odpt:airportTerminalTitle"] = odptairport_terminal_title
        if geolong is not UNSET:
            field_dict["geo:long"] = geolong
        if geolat is not UNSET:
            field_dict["geo:lat"] = geolat
        if ugregion is not UNSET:
            field_dict["ug:region"] = ugregion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.airport_terminal_ugregion import AirportTerminalUgregion
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = AirportTerminalType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        odptairport = d.pop("odpt:airport")

        dcdate = d.pop("dc:date", UNSET)

        dctitle = d.pop("dc:title", UNSET)

        _odptairport_terminal_title = d.pop("odpt:airportTerminalTitle", UNSET)
        odptairport_terminal_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptairport_terminal_title, Unset):
            odptairport_terminal_title = UNSET
        else:
            odptairport_terminal_title = MultilingualTitle.from_dict(_odptairport_terminal_title)

        geolong = d.pop("geo:long", UNSET)

        geolat = d.pop("geo:lat", UNSET)

        _ugregion = d.pop("ug:region", UNSET)
        ugregion: Union[Unset, AirportTerminalUgregion]
        if isinstance(_ugregion, Unset):
            ugregion = UNSET
        else:
            ugregion = AirportTerminalUgregion.from_dict(_ugregion)

        airport_terminal = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            odptairport=odptairport,
            dcdate=dcdate,
            dctitle=dctitle,
            odptairport_terminal_title=odptairport_terminal_title,
            geolong=geolong,
            geolat=geolat,
            ugregion=ugregion,
        )

        airport_terminal.additional_properties = d
        return airport_terminal

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
