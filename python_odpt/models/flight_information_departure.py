from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_information_departure_type import FlightInformationDepartureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="FlightInformationDeparture")


@_attrs_define
class FlightInformationDeparture:
    """フライト出発情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (FlightInformationDepartureType): クラス指定
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): フライト出発情報を提供する事業者を示すID
        odptflight_number (List[str]): フライト番号のリスト
        odptdeparture_airport (str): 出発空港を示すID
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptairline (Union[Unset, str]): エアラインの運行会社を表すID
        odptflight_status (Union[Unset, str]): フライト状況を表すID
        odptflight_information_summary (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptflight_information_text (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptscheduled_departure_time (Union[Unset, str]): ISO8601 時刻形式
        odptestimated_departure_time (Union[Unset, str]): ISO8601 時刻形式
        odptactual_departure_time (Union[Unset, str]): ISO8601 時刻形式
        odptdeparture_airport_terminal (Union[Unset, str]): 出発空港のターミナルを示すID
        odptdeparture_gate (Union[Unset, str]): 出発空港のゲート番号
        odptcheck_in_counter (Union[Unset, List[str]]): 出発空港のチェックインカウンターのリスト
        odptdestination_airport (Union[Unset, str]): 目的地の空港を示すID
        odptvia_airport (Union[Unset, List[str]]): 経由地の空港を表すIDのリスト
        odptaircraft_type (Union[Unset, str]): 航空機の機種
    """

    context: str
    id: str
    type: FlightInformationDepartureType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptflight_number: List[str]
    odptdeparture_airport: str
    dctvalid: Union[Unset, str] = UNSET
    odptairline: Union[Unset, str] = UNSET
    odptflight_status: Union[Unset, str] = UNSET
    odptflight_information_summary: Union[Unset, "MultilingualTitle"] = UNSET
    odptflight_information_text: Union[Unset, "MultilingualTitle"] = UNSET
    odptscheduled_departure_time: Union[Unset, str] = UNSET
    odptestimated_departure_time: Union[Unset, str] = UNSET
    odptactual_departure_time: Union[Unset, str] = UNSET
    odptdeparture_airport_terminal: Union[Unset, str] = UNSET
    odptdeparture_gate: Union[Unset, str] = UNSET
    odptcheck_in_counter: Union[Unset, List[str]] = UNSET
    odptdestination_airport: Union[Unset, str] = UNSET
    odptvia_airport: Union[Unset, List[str]] = UNSET
    odptaircraft_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptflight_number = self.odptflight_number

        odptdeparture_airport = self.odptdeparture_airport

        dctvalid = self.dctvalid

        odptairline = self.odptairline

        odptflight_status = self.odptflight_status

        odptflight_information_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptflight_information_summary, Unset):
            odptflight_information_summary = self.odptflight_information_summary.to_dict()

        odptflight_information_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptflight_information_text, Unset):
            odptflight_information_text = self.odptflight_information_text.to_dict()

        odptscheduled_departure_time = self.odptscheduled_departure_time

        odptestimated_departure_time = self.odptestimated_departure_time

        odptactual_departure_time = self.odptactual_departure_time

        odptdeparture_airport_terminal = self.odptdeparture_airport_terminal

        odptdeparture_gate = self.odptdeparture_gate

        odptcheck_in_counter: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptcheck_in_counter, Unset):
            odptcheck_in_counter = self.odptcheck_in_counter

        odptdestination_airport = self.odptdestination_airport

        odptvia_airport: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_airport, Unset):
            odptvia_airport = self.odptvia_airport

        odptaircraft_type = self.odptaircraft_type

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
                "odpt:flightNumber": odptflight_number,
                "odpt:departureAirport": odptdeparture_airport,
            }
        )
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptairline is not UNSET:
            field_dict["odpt:airline"] = odptairline
        if odptflight_status is not UNSET:
            field_dict["odpt:flightStatus"] = odptflight_status
        if odptflight_information_summary is not UNSET:
            field_dict["odpt:flightInformationSummary"] = odptflight_information_summary
        if odptflight_information_text is not UNSET:
            field_dict["odpt:flightInformationText"] = odptflight_information_text
        if odptscheduled_departure_time is not UNSET:
            field_dict["odpt:scheduledDepartureTime"] = odptscheduled_departure_time
        if odptestimated_departure_time is not UNSET:
            field_dict["odpt:estimatedDepartureTime"] = odptestimated_departure_time
        if odptactual_departure_time is not UNSET:
            field_dict["odpt:actualDepartureTime"] = odptactual_departure_time
        if odptdeparture_airport_terminal is not UNSET:
            field_dict["odpt:departureAirportTerminal"] = odptdeparture_airport_terminal
        if odptdeparture_gate is not UNSET:
            field_dict["odpt:departureGate"] = odptdeparture_gate
        if odptcheck_in_counter is not UNSET:
            field_dict["odpt:checkInCounter"] = odptcheck_in_counter
        if odptdestination_airport is not UNSET:
            field_dict["odpt:destinationAirport"] = odptdestination_airport
        if odptvia_airport is not UNSET:
            field_dict["odpt:viaAirport"] = odptvia_airport
        if odptaircraft_type is not UNSET:
            field_dict["odpt:aircraftType"] = odptaircraft_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = FlightInformationDepartureType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptflight_number = cast(List[str], d.pop("odpt:flightNumber"))

        odptdeparture_airport = d.pop("odpt:departureAirport")

        dctvalid = d.pop("dct:valid", UNSET)

        odptairline = d.pop("odpt:airline", UNSET)

        odptflight_status = d.pop("odpt:flightStatus", UNSET)

        _odptflight_information_summary = d.pop("odpt:flightInformationSummary", UNSET)
        odptflight_information_summary: Union[Unset, MultilingualTitle]
        if isinstance(_odptflight_information_summary, Unset):
            odptflight_information_summary = UNSET
        else:
            odptflight_information_summary = MultilingualTitle.from_dict(_odptflight_information_summary)

        _odptflight_information_text = d.pop("odpt:flightInformationText", UNSET)
        odptflight_information_text: Union[Unset, MultilingualTitle]
        if isinstance(_odptflight_information_text, Unset):
            odptflight_information_text = UNSET
        else:
            odptflight_information_text = MultilingualTitle.from_dict(_odptflight_information_text)

        odptscheduled_departure_time = d.pop("odpt:scheduledDepartureTime", UNSET)

        odptestimated_departure_time = d.pop("odpt:estimatedDepartureTime", UNSET)

        odptactual_departure_time = d.pop("odpt:actualDepartureTime", UNSET)

        odptdeparture_airport_terminal = d.pop("odpt:departureAirportTerminal", UNSET)

        odptdeparture_gate = d.pop("odpt:departureGate", UNSET)

        odptcheck_in_counter = cast(List[str], d.pop("odpt:checkInCounter", UNSET))

        odptdestination_airport = d.pop("odpt:destinationAirport", UNSET)

        odptvia_airport = cast(List[str], d.pop("odpt:viaAirport", UNSET))

        odptaircraft_type = d.pop("odpt:aircraftType", UNSET)

        flight_information_departure = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptflight_number=odptflight_number,
            odptdeparture_airport=odptdeparture_airport,
            dctvalid=dctvalid,
            odptairline=odptairline,
            odptflight_status=odptflight_status,
            odptflight_information_summary=odptflight_information_summary,
            odptflight_information_text=odptflight_information_text,
            odptscheduled_departure_time=odptscheduled_departure_time,
            odptestimated_departure_time=odptestimated_departure_time,
            odptactual_departure_time=odptactual_departure_time,
            odptdeparture_airport_terminal=odptdeparture_airport_terminal,
            odptdeparture_gate=odptdeparture_gate,
            odptcheck_in_counter=odptcheck_in_counter,
            odptdestination_airport=odptdestination_airport,
            odptvia_airport=odptvia_airport,
            odptaircraft_type=odptaircraft_type,
        )

        flight_information_departure.additional_properties = d
        return flight_information_departure

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
