from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="RetrieveResponse")


@_attrs_define
class RetrieveResponse:
    """データ取得APIのレスポンス

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt_Station.jsonld.
        id (str): 固有識別子
        type (str): クラス名 Example: odpt:Station.
        dcdate (str): ISO8601 日付時刻形式
        dctitle (str): 駅名(日本語) Example: 上野.
        geolat (float): 緯度 Example: 35.711835.
        geolong (float): 経度 Example: 139.775625.
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrailway (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptstation_code (str): 駅コード Example: G16.
        odptstation_title (MultilingualTitle): 多言語対応のタイトル
        odptpassenger_survey (List[str]): 駅乗降人員数を表すIDのリスト Example: ['odpt.PassengerSurvey:TokyoMetro.Ueno'].
        odptstation_timetable (List[str]): 駅時刻表を表すIDのリスト Example:
            ['odpt.StationTimetable:TokyoMetro.Ginza.Ueno.TokyoMetro.Shibuya.Weekday'].
        odptconnecting_railway (List[str]): 乗り換え可能路線のIDのリスト Example: ['odpt.Railway:TokyoMetro.Hibiya',
            'odpt.Railway:JR-East.AkitaShinkansen'].
        odptconnecting_station (List[str]): 乗り換え可能駅のIDのリスト Example: ['odpt.Station:TokyoMetro.Hibiya.Ueno',
            'odpt.Station:JR-East.AkitaShinkansen.Ueno'].
    """

    context: str
    id: str
    type: str
    dcdate: str
    dctitle: str
    geolat: float
    geolong: float
    owlsame_as: str
    odptrailway: str
    odptoperator: str
    odptstation_code: str
    odptstation_title: "MultilingualTitle"
    odptpassenger_survey: List[str]
    odptstation_timetable: List[str]
    odptconnecting_railway: List[str]
    odptconnecting_station: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type

        dcdate = self.dcdate

        dctitle = self.dctitle

        geolat = self.geolat

        geolong = self.geolong

        owlsame_as = self.owlsame_as

        odptrailway = self.odptrailway

        odptoperator = self.odptoperator

        odptstation_code = self.odptstation_code

        odptstation_title = self.odptstation_title.to_dict()

        odptpassenger_survey = self.odptpassenger_survey

        odptstation_timetable = self.odptstation_timetable

        odptconnecting_railway = self.odptconnecting_railway

        odptconnecting_station = self.odptconnecting_station

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:date": dcdate,
                "dc:title": dctitle,
                "geo:lat": geolat,
                "geo:long": geolong,
                "owl:sameAs": owlsame_as,
                "odpt:railway": odptrailway,
                "odpt:operator": odptoperator,
                "odpt:stationCode": odptstation_code,
                "odpt:stationTitle": odptstation_title,
                "odpt:passengerSurvey": odptpassenger_survey,
                "odpt:stationTimetable": odptstation_timetable,
                "odpt:connectingRailway": odptconnecting_railway,
                "odpt:connectingStation": odptconnecting_station,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = d.pop("@type")

        dcdate = d.pop("dc:date")

        dctitle = d.pop("dc:title")

        geolat = d.pop("geo:lat")

        geolong = d.pop("geo:long")

        owlsame_as = d.pop("owl:sameAs")

        odptrailway = d.pop("odpt:railway")

        odptoperator = d.pop("odpt:operator")

        odptstation_code = d.pop("odpt:stationCode")

        odptstation_title = MultilingualTitle.from_dict(d.pop("odpt:stationTitle"))

        odptpassenger_survey = cast(List[str], d.pop("odpt:passengerSurvey"))

        odptstation_timetable = cast(List[str], d.pop("odpt:stationTimetable"))

        odptconnecting_railway = cast(List[str], d.pop("odpt:connectingRailway"))

        odptconnecting_station = cast(List[str], d.pop("odpt:connectingStation"))

        retrieve_response = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            dctitle=dctitle,
            geolat=geolat,
            geolong=geolong,
            owlsame_as=owlsame_as,
            odptrailway=odptrailway,
            odptoperator=odptoperator,
            odptstation_code=odptstation_code,
            odptstation_title=odptstation_title,
            odptpassenger_survey=odptpassenger_survey,
            odptstation_timetable=odptstation_timetable,
            odptconnecting_railway=odptconnecting_railway,
            odptconnecting_station=odptconnecting_station,
        )

        retrieve_response.additional_properties = d
        return retrieve_response

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
