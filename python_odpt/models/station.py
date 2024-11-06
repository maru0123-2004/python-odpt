from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.station_type import StationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle
    from ..models.station_ugregion import StationUgregion


T = TypeVar("T", bound="Station")


@_attrs_define
class Station:
    """駅情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (StationType): クラス名 Example: odpt:Station.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrailway (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        dctitle (Union[Unset, str]): 駅名(日本語) Example: 東京.
        odptstation_title (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptstation_code (Union[Unset, str]): 駅コード Example: JY01.
        geolong (Union[Unset, float]): 代表点の経度 Example: 139.1234.
        geolat (Union[Unset, float]): 代表点の緯度 Example: 35.1234.
        ugregion (Union[Unset, StationUgregion]): GeoJSON形式による地物情報
        odptexit (Union[Unset, List[str]]): 駅出入口を表すIDのリスト IDにはug:Poiの@idの値を利用 Example: ['string'].
        odptconnecting_railway (Union[Unset, List[str]]): 乗り換え可能路線のIDのリスト Example: ['odpt.Railway:JR-East.ChuoRapid',
            'odpt.Railway:TokyoMetro.Marunouchi'].
        odptconnecting_station (Union[Unset, List[str]]): 乗り換え可能駅のIDのリスト Example: ['odpt.Station:JR-
            East.ChuoRapid.Tokyo', 'odpt.Station:TokyoMetro.Marunouchi.Tokyo'].
        odptstation_timetable (Union[Unset, List[str]]): 駅時刻表を表すIDのリスト Example: ['odpt.StationTimetable:JR-
            East.Yamanote.Tokyo.Outbound.Weekday'].
        odptpassenger_survey (Union[Unset, List[str]]): 駅乗降人員数を表すIDのリスト Example: ['odpt.PassengerSurvey:JR-East.Tokyo'].
    """

    context: str
    id: str
    type: StationType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptrailway: str
    dctitle: Union[Unset, str] = UNSET
    odptstation_title: Union[Unset, "MultilingualTitle"] = UNSET
    odptstation_code: Union[Unset, str] = UNSET
    geolong: Union[Unset, float] = UNSET
    geolat: Union[Unset, float] = UNSET
    ugregion: Union[Unset, "StationUgregion"] = UNSET
    odptexit: Union[Unset, List[str]] = UNSET
    odptconnecting_railway: Union[Unset, List[str]] = UNSET
    odptconnecting_station: Union[Unset, List[str]] = UNSET
    odptstation_timetable: Union[Unset, List[str]] = UNSET
    odptpassenger_survey: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptrailway = self.odptrailway

        dctitle = self.dctitle

        odptstation_title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptstation_title, Unset):
            odptstation_title = self.odptstation_title.to_dict()

        odptstation_code = self.odptstation_code

        geolong = self.geolong

        geolat = self.geolat

        ugregion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ugregion, Unset):
            ugregion = self.ugregion.to_dict()

        odptexit: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptexit, Unset):
            odptexit = self.odptexit

        odptconnecting_railway: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptconnecting_railway, Unset):
            odptconnecting_railway = self.odptconnecting_railway

        odptconnecting_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptconnecting_station, Unset):
            odptconnecting_station = self.odptconnecting_station

        odptstation_timetable: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptstation_timetable, Unset):
            odptstation_timetable = self.odptstation_timetable

        odptpassenger_survey: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptpassenger_survey, Unset):
            odptpassenger_survey = self.odptpassenger_survey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:date": dcdate,
                "owl:sameAs": owlsame_as,
                "odpt:operator": odptoperator,
                "odpt:railway": odptrailway,
            }
        )
        if dctitle is not UNSET:
            field_dict["dc:title"] = dctitle
        if odptstation_title is not UNSET:
            field_dict["odpt:stationTitle"] = odptstation_title
        if odptstation_code is not UNSET:
            field_dict["odpt:stationCode"] = odptstation_code
        if geolong is not UNSET:
            field_dict["geo:long"] = geolong
        if geolat is not UNSET:
            field_dict["geo:lat"] = geolat
        if ugregion is not UNSET:
            field_dict["ug:region"] = ugregion
        if odptexit is not UNSET:
            field_dict["odpt:exit"] = odptexit
        if odptconnecting_railway is not UNSET:
            field_dict["odpt:connectingRailway"] = odptconnecting_railway
        if odptconnecting_station is not UNSET:
            field_dict["odpt:connectingStation"] = odptconnecting_station
        if odptstation_timetable is not UNSET:
            field_dict["odpt:stationTimetable"] = odptstation_timetable
        if odptpassenger_survey is not UNSET:
            field_dict["odpt:passengerSurvey"] = odptpassenger_survey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle
        from ..models.station_ugregion import StationUgregion

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = StationType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptrailway = d.pop("odpt:railway")

        dctitle = d.pop("dc:title", UNSET)

        _odptstation_title = d.pop("odpt:stationTitle", UNSET)
        odptstation_title: Union[Unset, MultilingualTitle]
        if isinstance(_odptstation_title, Unset):
            odptstation_title = UNSET
        else:
            odptstation_title = MultilingualTitle.from_dict(_odptstation_title)

        odptstation_code = d.pop("odpt:stationCode", UNSET)

        geolong = d.pop("geo:long", UNSET)

        geolat = d.pop("geo:lat", UNSET)

        _ugregion = d.pop("ug:region", UNSET)
        ugregion: Union[Unset, StationUgregion]
        if isinstance(_ugregion, Unset):
            ugregion = UNSET
        else:
            ugregion = StationUgregion.from_dict(_ugregion)

        odptexit = cast(List[str], d.pop("odpt:exit", UNSET))

        odptconnecting_railway = cast(List[str], d.pop("odpt:connectingRailway", UNSET))

        odptconnecting_station = cast(List[str], d.pop("odpt:connectingStation", UNSET))

        odptstation_timetable = cast(List[str], d.pop("odpt:stationTimetable", UNSET))

        odptpassenger_survey = cast(List[str], d.pop("odpt:passengerSurvey", UNSET))

        station = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptrailway=odptrailway,
            dctitle=dctitle,
            odptstation_title=odptstation_title,
            odptstation_code=odptstation_code,
            geolong=geolong,
            geolat=geolat,
            ugregion=ugregion,
            odptexit=odptexit,
            odptconnecting_railway=odptconnecting_railway,
            odptconnecting_station=odptconnecting_station,
            odptstation_timetable=odptstation_timetable,
            odptpassenger_survey=odptpassenger_survey,
        )

        station.additional_properties = d
        return station

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
