from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.flight_information_arrival_type import FlightInformationArrivalType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="FlightInformationArrival")


@_attrs_define
class FlightInformationArrival:
    """フライト到着情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL
        id (str): 固有識別子
        type (FlightInformationArrivalType): クラス指定
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): フライト到着情報を提供する事業者を示すID
        odptflight_number (List[str]): フライト番号のリスト
        odptarrival_airport (str): 到着空港を示すID
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptairline (Union[Unset, str]): エアラインの運行会社を表すID
        odptflight_status (Union[Unset, str]): フライト状況を表すID
        odptflight_information_summary (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptflight_information_text (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptscheduled_arrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptestimated_arrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptactual_arrival_time (Union[Unset, str]): ISO8601 時刻形式
        odptarrival_airport_terminal (Union[Unset, str]): 到着空港のターミナルを表すID
        odptarrival_gate (Union[Unset, str]): 到着空港のゲート番号
        odptbaggage_claim (Union[Unset, str]): 到着空港の預け手荷物受取所
        odptorigin_airport (Union[Unset, str]): 出発地の空港を示すID
        odptvia_airport (Union[Unset, List[str]]): 経由地の空港を表すIDのリスト
        odptaircraft_type (Union[Unset, str]): 航空機の機種
    """

    context: str
    id: str
    type: FlightInformationArrivalType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptflight_number: List[str]
    odptarrival_airport: str
    dctvalid: Union[Unset, str] = UNSET
    odptairline: Union[Unset, str] = UNSET
    odptflight_status: Union[Unset, str] = UNSET
    odptflight_information_summary: Union[Unset, "MultilingualTitle"] = UNSET
    odptflight_information_text: Union[Unset, "MultilingualTitle"] = UNSET
    odptscheduled_arrival_time: Union[Unset, str] = UNSET
    odptestimated_arrival_time: Union[Unset, str] = UNSET
    odptactual_arrival_time: Union[Unset, str] = UNSET
    odptarrival_airport_terminal: Union[Unset, str] = UNSET
    odptarrival_gate: Union[Unset, str] = UNSET
    odptbaggage_claim: Union[Unset, str] = UNSET
    odptorigin_airport: Union[Unset, str] = UNSET
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

        odptarrival_airport = self.odptarrival_airport

        dctvalid = self.dctvalid

        odptairline = self.odptairline

        odptflight_status = self.odptflight_status

        odptflight_information_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptflight_information_summary, Unset):
            odptflight_information_summary = self.odptflight_information_summary.to_dict()

        odptflight_information_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptflight_information_text, Unset):
            odptflight_information_text = self.odptflight_information_text.to_dict()

        odptscheduled_arrival_time = self.odptscheduled_arrival_time

        odptestimated_arrival_time = self.odptestimated_arrival_time

        odptactual_arrival_time = self.odptactual_arrival_time

        odptarrival_airport_terminal = self.odptarrival_airport_terminal

        odptarrival_gate = self.odptarrival_gate

        odptbaggage_claim = self.odptbaggage_claim

        odptorigin_airport = self.odptorigin_airport

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
                "odpt:arrivalAirport": odptarrival_airport,
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
        if odptscheduled_arrival_time is not UNSET:
            field_dict["odpt:scheduledArrivalTime"] = odptscheduled_arrival_time
        if odptestimated_arrival_time is not UNSET:
            field_dict["odpt:estimatedArrivalTime"] = odptestimated_arrival_time
        if odptactual_arrival_time is not UNSET:
            field_dict["odpt:actualArrivalTime"] = odptactual_arrival_time
        if odptarrival_airport_terminal is not UNSET:
            field_dict["odpt:arrivalAirportTerminal"] = odptarrival_airport_terminal
        if odptarrival_gate is not UNSET:
            field_dict["odpt:arrivalGate"] = odptarrival_gate
        if odptbaggage_claim is not UNSET:
            field_dict["odpt:baggageClaim"] = odptbaggage_claim
        if odptorigin_airport is not UNSET:
            field_dict["odpt:originAirport"] = odptorigin_airport
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

        type = FlightInformationArrivalType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptflight_number = cast(List[str], d.pop("odpt:flightNumber"))

        odptarrival_airport = d.pop("odpt:arrivalAirport")

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

        odptscheduled_arrival_time = d.pop("odpt:scheduledArrivalTime", UNSET)

        odptestimated_arrival_time = d.pop("odpt:estimatedArrivalTime", UNSET)

        odptactual_arrival_time = d.pop("odpt:actualArrivalTime", UNSET)

        odptarrival_airport_terminal = d.pop("odpt:arrivalAirportTerminal", UNSET)

        odptarrival_gate = d.pop("odpt:arrivalGate", UNSET)

        odptbaggage_claim = d.pop("odpt:baggageClaim", UNSET)

        odptorigin_airport = d.pop("odpt:originAirport", UNSET)

        odptvia_airport = cast(List[str], d.pop("odpt:viaAirport", UNSET))

        odptaircraft_type = d.pop("odpt:aircraftType", UNSET)

        flight_information_arrival = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptflight_number=odptflight_number,
            odptarrival_airport=odptarrival_airport,
            dctvalid=dctvalid,
            odptairline=odptairline,
            odptflight_status=odptflight_status,
            odptflight_information_summary=odptflight_information_summary,
            odptflight_information_text=odptflight_information_text,
            odptscheduled_arrival_time=odptscheduled_arrival_time,
            odptestimated_arrival_time=odptestimated_arrival_time,
            odptactual_arrival_time=odptactual_arrival_time,
            odptarrival_airport_terminal=odptarrival_airport_terminal,
            odptarrival_gate=odptarrival_gate,
            odptbaggage_claim=odptbaggage_claim,
            odptorigin_airport=odptorigin_airport,
            odptvia_airport=odptvia_airport,
            odptaircraft_type=odptaircraft_type,
        )

        flight_information_arrival.additional_properties = d
        return flight_information_arrival

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
