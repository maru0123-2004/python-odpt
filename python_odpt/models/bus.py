from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bus_door_status import BusDoorStatus
from ..models.bus_type import BusType
from ..models.occupancy_status import OccupancyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Bus")


@_attrs_define
class Bus:
    """バスの運行情報
    `odpt:busroutePattern` が運行中の系統を示し、 `odpt:fromBusstopPole`, `odpt:toBusstopPole` で現在位置を示す。
    接近中の判別がつかない場合は、`odpt:fromBusstopPole` は null とはならない場合がある。
    停車中の判別がつかない場合は、`odpt:toBusstopPole` は null とはならない場合がある。
    odpt:occupancyStatus は車両の混雑度を示す。

        Attributes:
            context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt_Bus.jsonld.
            id (str): 固有識別子
            type (BusType): バス運行情報のクラス名 Example: odpt:Bus.
            owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptbus_number (str): バス車両番号 Example: 1889.
            dcdate (str): ISO8601 日付時刻形式
            dctvalid (str): ISO8601 日付時刻形式
            odptfrequency (int): 更新頻度(秒)、指定された秒数以降にリクエストを行うことで、最新値が取得される。 Example: 30.
            odptbusroute_pattern (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptbus_timetable (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptstarting_busstop_pole (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptterminal_busstop_pole (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptfrom_busstop_pole (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptfrom_busstop_pole_time (Union[Unset, str]): ISO8601 日付時刻形式
            odptto_busstop_pole (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
            odptprogress (Union[Unset, float]): Fromを0, Toを1とした際の現在位置 (割合)
            geolong (Union[Unset, float]): 対象となるバスの経度 (10進表記、測地系はWGS84) Example: 139.63494873046875.
            geolat (Union[Unset, float]): 対象となるバスの緯度 (10進表記、測地系はWGS84) Example: 35.41614532470703.
            odptspeed (Union[Unset, float]): 対象となるバスの速度 (km/h)
            odptazimuth (Union[Unset, float]): 対象となるバスの進行方向方位角を示す。単位は度(°)。北が0度で、時計回り(東回り)に増加する。 Example: 249.9993896484375.
            odptdoor_status (Union[Unset, BusDoorStatus]):
            odptoccupancy_status (Union[Unset, OccupancyStatus]):
    """

    context: str
    id: str
    type: BusType
    owlsame_as: str
    odptbus_number: str
    dcdate: str
    dctvalid: str
    odptfrequency: int
    odptbusroute_pattern: str
    odptoperator: str
    odptbus_timetable: Union[Unset, str] = UNSET
    odptstarting_busstop_pole: Union[Unset, str] = UNSET
    odptterminal_busstop_pole: Union[Unset, str] = UNSET
    odptfrom_busstop_pole: Union[Unset, str] = UNSET
    odptfrom_busstop_pole_time: Union[Unset, str] = UNSET
    odptto_busstop_pole: Union[Unset, str] = UNSET
    odptprogress: Union[Unset, float] = UNSET
    geolong: Union[Unset, float] = UNSET
    geolat: Union[Unset, float] = UNSET
    odptspeed: Union[Unset, float] = UNSET
    odptazimuth: Union[Unset, float] = UNSET
    odptdoor_status: Union[Unset, BusDoorStatus] = UNSET
    odptoccupancy_status: Union[Unset, OccupancyStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        odptbus_number = self.odptbus_number

        dcdate = self.dcdate

        dctvalid = self.dctvalid

        odptfrequency = self.odptfrequency

        odptbusroute_pattern = self.odptbusroute_pattern

        odptoperator = self.odptoperator

        odptbus_timetable = self.odptbus_timetable

        odptstarting_busstop_pole = self.odptstarting_busstop_pole

        odptterminal_busstop_pole = self.odptterminal_busstop_pole

        odptfrom_busstop_pole = self.odptfrom_busstop_pole

        odptfrom_busstop_pole_time = self.odptfrom_busstop_pole_time

        odptto_busstop_pole = self.odptto_busstop_pole

        odptprogress = self.odptprogress

        geolong = self.geolong

        geolat = self.geolat

        odptspeed = self.odptspeed

        odptazimuth = self.odptazimuth

        odptdoor_status: Union[Unset, str] = UNSET
        if not isinstance(self.odptdoor_status, Unset):
            odptdoor_status = self.odptdoor_status.value

        odptoccupancy_status: Union[Unset, str] = UNSET
        if not isinstance(self.odptoccupancy_status, Unset):
            odptoccupancy_status = self.odptoccupancy_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "odpt:busNumber": odptbus_number,
                "dc:date": dcdate,
                "dct:valid": dctvalid,
                "odpt:frequency": odptfrequency,
                "odpt:busroutePattern": odptbusroute_pattern,
                "odpt:operator": odptoperator,
            }
        )
        if odptbus_timetable is not UNSET:
            field_dict["odpt:busTimetable"] = odptbus_timetable
        if odptstarting_busstop_pole is not UNSET:
            field_dict["odpt:startingBusstopPole"] = odptstarting_busstop_pole
        if odptterminal_busstop_pole is not UNSET:
            field_dict["odpt:terminalBusstopPole"] = odptterminal_busstop_pole
        if odptfrom_busstop_pole is not UNSET:
            field_dict["odpt:fromBusstopPole"] = odptfrom_busstop_pole
        if odptfrom_busstop_pole_time is not UNSET:
            field_dict["odpt:fromBusstopPoleTime"] = odptfrom_busstop_pole_time
        if odptto_busstop_pole is not UNSET:
            field_dict["odpt:toBusstopPole"] = odptto_busstop_pole
        if odptprogress is not UNSET:
            field_dict["odpt:progress"] = odptprogress
        if geolong is not UNSET:
            field_dict["geo:long"] = geolong
        if geolat is not UNSET:
            field_dict["geo:lat"] = geolat
        if odptspeed is not UNSET:
            field_dict["odpt:speed"] = odptspeed
        if odptazimuth is not UNSET:
            field_dict["odpt:azimuth"] = odptazimuth
        if odptdoor_status is not UNSET:
            field_dict["odpt:doorStatus"] = odptdoor_status
        if odptoccupancy_status is not UNSET:
            field_dict["odpt:occupancyStatus"] = odptoccupancy_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = BusType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        odptbus_number = d.pop("odpt:busNumber")

        dcdate = d.pop("dc:date")

        dctvalid = d.pop("dct:valid")

        odptfrequency = d.pop("odpt:frequency")

        odptbusroute_pattern = d.pop("odpt:busroutePattern")

        odptoperator = d.pop("odpt:operator")

        odptbus_timetable = d.pop("odpt:busTimetable", UNSET)

        odptstarting_busstop_pole = d.pop("odpt:startingBusstopPole", UNSET)

        odptterminal_busstop_pole = d.pop("odpt:terminalBusstopPole", UNSET)

        odptfrom_busstop_pole = d.pop("odpt:fromBusstopPole", UNSET)

        odptfrom_busstop_pole_time = d.pop("odpt:fromBusstopPoleTime", UNSET)

        odptto_busstop_pole = d.pop("odpt:toBusstopPole", UNSET)

        odptprogress = d.pop("odpt:progress", UNSET)

        geolong = d.pop("geo:long", UNSET)

        geolat = d.pop("geo:lat", UNSET)

        odptspeed = d.pop("odpt:speed", UNSET)

        odptazimuth = d.pop("odpt:azimuth", UNSET)

        _odptdoor_status = d.pop("odpt:doorStatus", UNSET)
        odptdoor_status: Union[Unset, BusDoorStatus]
        if isinstance(_odptdoor_status, Unset):
            odptdoor_status = UNSET
        else:
            odptdoor_status = BusDoorStatus(_odptdoor_status)

        _odptoccupancy_status = d.pop("odpt:occupancyStatus", UNSET)
        odptoccupancy_status: Union[Unset, OccupancyStatus]
        if isinstance(_odptoccupancy_status, Unset):
            odptoccupancy_status = UNSET
        else:
            odptoccupancy_status = OccupancyStatus(_odptoccupancy_status)

        bus = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            odptbus_number=odptbus_number,
            dcdate=dcdate,
            dctvalid=dctvalid,
            odptfrequency=odptfrequency,
            odptbusroute_pattern=odptbusroute_pattern,
            odptoperator=odptoperator,
            odptbus_timetable=odptbus_timetable,
            odptstarting_busstop_pole=odptstarting_busstop_pole,
            odptterminal_busstop_pole=odptterminal_busstop_pole,
            odptfrom_busstop_pole=odptfrom_busstop_pole,
            odptfrom_busstop_pole_time=odptfrom_busstop_pole_time,
            odptto_busstop_pole=odptto_busstop_pole,
            odptprogress=odptprogress,
            geolong=geolong,
            geolat=geolat,
            odptspeed=odptspeed,
            odptazimuth=odptazimuth,
            odptdoor_status=odptdoor_status,
            odptoccupancy_status=odptoccupancy_status,
        )

        bus.additional_properties = d
        return bus

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
