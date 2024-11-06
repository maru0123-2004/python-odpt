from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_schedule_type import FlightScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flight_schedule_object import FlightScheduleObject


T = TypeVar("T", bound="FlightSchedule")


@_attrs_define
class FlightSchedule:
    """フライト時刻表

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (FlightScheduleType): クラス指定
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): フライト時刻表を提供する事業者を示すID
        odptcalendar (str): カレンダー情報を示すID
        odptorigin_airport (str): 出発地の空港のID
        odptdestination_airport (str): 目的地の空港のID
        dcdate (Union[Unset, str]): ISO8601 日付時刻形式
        odptflight_schedule_object (Union[Unset, List['FlightScheduleObject']]): 時刻表オブジェクト
    """

    context: str
    id: str
    type: FlightScheduleType
    owlsame_as: str
    odptoperator: str
    odptcalendar: str
    odptorigin_airport: str
    odptdestination_airport: str
    dcdate: Union[Unset, str] = UNSET
    odptflight_schedule_object: Union[Unset, List["FlightScheduleObject"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptcalendar = self.odptcalendar

        odptorigin_airport = self.odptorigin_airport

        odptdestination_airport = self.odptdestination_airport

        dcdate = self.dcdate

        odptflight_schedule_object: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.odptflight_schedule_object, Unset):
            odptflight_schedule_object = []
            for odptflight_schedule_object_item_data in self.odptflight_schedule_object:
                odptflight_schedule_object_item = odptflight_schedule_object_item_data.to_dict()
                odptflight_schedule_object.append(odptflight_schedule_object_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "owl:sameAs": owlsame_as,
                "odpt:operator": odptoperator,
                "odpt:calendar": odptcalendar,
                "odpt:originAirport": odptorigin_airport,
                "odpt:destinationAirport": odptdestination_airport,
            }
        )
        if dcdate is not UNSET:
            field_dict["dc:date"] = dcdate
        if odptflight_schedule_object is not UNSET:
            field_dict["odpt:flightScheduleObject"] = odptflight_schedule_object

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.flight_schedule_object import FlightScheduleObject

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = FlightScheduleType(d.pop("@type"))

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptcalendar = d.pop("odpt:calendar")

        odptorigin_airport = d.pop("odpt:originAirport")

        odptdestination_airport = d.pop("odpt:destinationAirport")

        dcdate = d.pop("dc:date", UNSET)

        odptflight_schedule_object = []
        _odptflight_schedule_object = d.pop("odpt:flightScheduleObject", UNSET)
        for odptflight_schedule_object_item_data in _odptflight_schedule_object or []:
            odptflight_schedule_object_item = FlightScheduleObject.from_dict(odptflight_schedule_object_item_data)

            odptflight_schedule_object.append(odptflight_schedule_object_item)

        flight_schedule = cls(
            context=context,
            id=id,
            type=type,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptcalendar=odptcalendar,
            odptorigin_airport=odptorigin_airport,
            odptdestination_airport=odptdestination_airport,
            dcdate=dcdate,
            odptflight_schedule_object=odptflight_schedule_object,
        )

        flight_schedule.additional_properties = d
        return flight_schedule

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
