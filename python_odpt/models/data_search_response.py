from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSearchResponse")


@_attrs_define
class DataSearchResponse:
    """データ検索APIのレスポンス

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt_Train.jsonld.
        id (str): 固有識別子
        type (str): クラス名 Example: odpt:Train.
        dcdate (str): ISO8601 日付時刻形式
        dctvalid (str): ISO8601 日付時刻形式
        odptfrequency (int): 更新頻度(秒)、指定された秒数以降にリクエストを行うことで、最新値が取得される。 Example: 30.
        odptrailway (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_number (str): 列車番号 Example: B1045S.
        odpttrain_type (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptorigin_station (List[str]): 列車の始発駅のIDのリスト Example: ['odpt.Station:TokyoMetro.Yurakucho.ShinKiba'].
        odptdestination_station (List[str]): 列車の終着駅のIDのリスト Example: ['odpt.Station:TokyoMetro.Yurakucho.Wakoshi'].
        odptfrom_station (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptto_station (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrail_direction (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptdelay (Union[Unset, int]): 遅延時間(秒)
    """

    context: str
    id: str
    type: str
    dcdate: str
    dctvalid: str
    odptfrequency: int
    odptrailway: str
    owlsame_as: str
    odpttrain_number: str
    odpttrain_type: str
    odptorigin_station: List[str]
    odptdestination_station: List[str]
    odptfrom_station: str
    odptto_station: str
    odptrail_direction: str
    odptoperator: str
    odptdelay: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type

        dcdate = self.dcdate

        dctvalid = self.dctvalid

        odptfrequency = self.odptfrequency

        odptrailway = self.odptrailway

        owlsame_as = self.owlsame_as

        odpttrain_number = self.odpttrain_number

        odpttrain_type = self.odpttrain_type

        odptorigin_station = self.odptorigin_station

        odptdestination_station = self.odptdestination_station

        odptfrom_station = self.odptfrom_station

        odptto_station = self.odptto_station

        odptrail_direction = self.odptrail_direction

        odptoperator = self.odptoperator

        odptdelay = self.odptdelay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:date": dcdate,
                "dct:valid": dctvalid,
                "odpt:frequency": odptfrequency,
                "odpt:railway": odptrailway,
                "owl:sameAs": owlsame_as,
                "odpt:trainNumber": odpttrain_number,
                "odpt:trainType": odpttrain_type,
                "odpt:originStation": odptorigin_station,
                "odpt:destinationStation": odptdestination_station,
                "odpt:fromStation": odptfrom_station,
                "odpt:toStation": odptto_station,
                "odpt:railDirection": odptrail_direction,
                "odpt:operator": odptoperator,
            }
        )
        if odptdelay is not UNSET:
            field_dict["odpt:delay"] = odptdelay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = d.pop("@type")

        dcdate = d.pop("dc:date")

        dctvalid = d.pop("dct:valid")

        odptfrequency = d.pop("odpt:frequency")

        odptrailway = d.pop("odpt:railway")

        owlsame_as = d.pop("owl:sameAs")

        odpttrain_number = d.pop("odpt:trainNumber")

        odpttrain_type = d.pop("odpt:trainType")

        odptorigin_station = cast(List[str], d.pop("odpt:originStation"))

        odptdestination_station = cast(List[str], d.pop("odpt:destinationStation"))

        odptfrom_station = d.pop("odpt:fromStation")

        odptto_station = d.pop("odpt:toStation")

        odptrail_direction = d.pop("odpt:railDirection")

        odptoperator = d.pop("odpt:operator")

        odptdelay = d.pop("odpt:delay", UNSET)

        data_search_response = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            dctvalid=dctvalid,
            odptfrequency=odptfrequency,
            odptrailway=odptrailway,
            owlsame_as=owlsame_as,
            odpttrain_number=odpttrain_number,
            odpttrain_type=odpttrain_type,
            odptorigin_station=odptorigin_station,
            odptdestination_station=odptdestination_station,
            odptfrom_station=odptfrom_station,
            odptto_station=odptto_station,
            odptrail_direction=odptrail_direction,
            odptoperator=odptoperator,
            odptdelay=odptdelay,
        )

        data_search_response.additional_properties = d
        return data_search_response

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
