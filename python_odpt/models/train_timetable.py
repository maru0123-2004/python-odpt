from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.train_timetable_type import TrainTimetableType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle
    from ..models.train_timetable_object import TrainTimetableObject


T = TypeVar("T", bound="TrainTimetable")


@_attrs_define
class TrainTimetable:
    """列車時刻表

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (TrainTimetableType): クラス名 Example: odpt:TrainTimetable.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptrailway (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_number (str): 列車番号 Example: 123M.
        odpttrain_timetable_object (List['TrainTimetableObject']): 出発時刻と出発駅の組か、到着時刻と到着駅の組のリスト Example:
            [{'odpt:departureTime': '06:00', 'odpt:departureStation': 'odpt.Station:JR-East.ChuoRapid.Tokyo'},
            {'odpt:arrivalTime': '07:00', 'odpt:arrivalStation': 'odpt.Station:JR-East.ChuoRapid.Takao'}].
        dctissued (Union[Unset, str]): ISO8601 日付形式
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptrail_direction (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptcalendar (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_type (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_name (Union[Unset, List['MultilingualTitle']]): 編成の名称・愛称のリスト Example: [{'ja': 'むさし', 'en':
            'Musashi'}].
        odpttrain_owner (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptorigin_station (Union[Unset, List[str]]): 列車の始発駅を表すIDのリスト Example: ['odpt.Station:JR-East.ChuoRapid.Tokyo'].
        odptdestination_station (Union[Unset, List[str]]): 列車の終着駅を表すIDのリスト Example: ['odpt.Station:JR-
            East.ChuoRapid.Takao'].
        odptvia_station (Union[Unset, List[str]]): 列車の経由駅を表すIDのリスト Example:
            ['odpt.Station:TokyoMetro.Tozai.NishiFunabashi'].
        odptvia_railway (Union[Unset, List[str]]): 列車の経由路線を表すIDのリスト Example: ['odpt.Railway:TokyoMetro.Tozai'].
        odptprevious_train_timetable (Union[Unset, List[str]]): 直前の列車時刻表を表すIDのリスト Example: ['odpt.TrainTimetable:JR-
            East.ChuoRapid.123M.Weekday'].
        odptnext_train_timetable (Union[Unset, List[str]]): 直後の列車時刻表を表すIDのリスト Example: ['odpt.TrainTimetable:JR-
            East.ChuoRapid.123M.Weekday'].
        odptneed_extra_fee (Union[Unset, bool]): 乗車券の他に別料金が必要か Example: True.
        odptnote (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
    """

    context: str
    id: str
    type: TrainTimetableType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptrailway: str
    odpttrain_number: str
    odpttrain_timetable_object: List["TrainTimetableObject"]
    dctissued: Union[Unset, str] = UNSET
    dctvalid: Union[Unset, str] = UNSET
    odptrail_direction: Union[Unset, str] = UNSET
    odptcalendar: Union[Unset, str] = UNSET
    odpttrain: Union[Unset, str] = UNSET
    odpttrain_type: Union[Unset, str] = UNSET
    odpttrain_name: Union[Unset, List["MultilingualTitle"]] = UNSET
    odpttrain_owner: Union[Unset, str] = UNSET
    odptorigin_station: Union[Unset, List[str]] = UNSET
    odptdestination_station: Union[Unset, List[str]] = UNSET
    odptvia_station: Union[Unset, List[str]] = UNSET
    odptvia_railway: Union[Unset, List[str]] = UNSET
    odptprevious_train_timetable: Union[Unset, List[str]] = UNSET
    odptnext_train_timetable: Union[Unset, List[str]] = UNSET
    odptneed_extra_fee: Union[Unset, bool] = UNSET
    odptnote: Union[Unset, "MultilingualTitle"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptrailway = self.odptrailway

        odpttrain_number = self.odpttrain_number

        odpttrain_timetable_object = []
        for odpttrain_timetable_object_item_data in self.odpttrain_timetable_object:
            odpttrain_timetable_object_item = odpttrain_timetable_object_item_data.to_dict()
            odpttrain_timetable_object.append(odpttrain_timetable_object_item)

        dctissued = self.dctissued

        dctvalid = self.dctvalid

        odptrail_direction = self.odptrail_direction

        odptcalendar = self.odptcalendar

        odpttrain = self.odpttrain

        odpttrain_type = self.odpttrain_type

        odpttrain_name: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.odpttrain_name, Unset):
            odpttrain_name = []
            for odpttrain_name_item_data in self.odpttrain_name:
                odpttrain_name_item = odpttrain_name_item_data.to_dict()
                odpttrain_name.append(odpttrain_name_item)

        odpttrain_owner = self.odpttrain_owner

        odptorigin_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptorigin_station, Unset):
            odptorigin_station = self.odptorigin_station

        odptdestination_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptdestination_station, Unset):
            odptdestination_station = self.odptdestination_station

        odptvia_station: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_station, Unset):
            odptvia_station = self.odptvia_station

        odptvia_railway: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptvia_railway, Unset):
            odptvia_railway = self.odptvia_railway

        odptprevious_train_timetable: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptprevious_train_timetable, Unset):
            odptprevious_train_timetable = self.odptprevious_train_timetable

        odptnext_train_timetable: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odptnext_train_timetable, Unset):
            odptnext_train_timetable = self.odptnext_train_timetable

        odptneed_extra_fee = self.odptneed_extra_fee

        odptnote: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odptnote, Unset):
            odptnote = self.odptnote.to_dict()

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
                "odpt:trainNumber": odpttrain_number,
                "odpt:trainTimetableObject": odpttrain_timetable_object,
            }
        )
        if dctissued is not UNSET:
            field_dict["dct:issued"] = dctissued
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptrail_direction is not UNSET:
            field_dict["odpt:railDirection"] = odptrail_direction
        if odptcalendar is not UNSET:
            field_dict["odpt:calendar"] = odptcalendar
        if odpttrain is not UNSET:
            field_dict["odpt:train"] = odpttrain
        if odpttrain_type is not UNSET:
            field_dict["odpt:trainType"] = odpttrain_type
        if odpttrain_name is not UNSET:
            field_dict["odpt:trainName"] = odpttrain_name
        if odpttrain_owner is not UNSET:
            field_dict["odpt:trainOwner"] = odpttrain_owner
        if odptorigin_station is not UNSET:
            field_dict["odpt:originStation"] = odptorigin_station
        if odptdestination_station is not UNSET:
            field_dict["odpt:destinationStation"] = odptdestination_station
        if odptvia_station is not UNSET:
            field_dict["odpt:viaStation"] = odptvia_station
        if odptvia_railway is not UNSET:
            field_dict["odpt:viaRailway"] = odptvia_railway
        if odptprevious_train_timetable is not UNSET:
            field_dict["odpt:previousTrainTimetable"] = odptprevious_train_timetable
        if odptnext_train_timetable is not UNSET:
            field_dict["odpt:nextTrainTimetable"] = odptnext_train_timetable
        if odptneed_extra_fee is not UNSET:
            field_dict["odpt:needExtraFee"] = odptneed_extra_fee
        if odptnote is not UNSET:
            field_dict["odpt:note"] = odptnote

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle
        from ..models.train_timetable_object import TrainTimetableObject

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = TrainTimetableType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptrailway = d.pop("odpt:railway")

        odpttrain_number = d.pop("odpt:trainNumber")

        odpttrain_timetable_object = []
        _odpttrain_timetable_object = d.pop("odpt:trainTimetableObject")
        for odpttrain_timetable_object_item_data in _odpttrain_timetable_object:
            odpttrain_timetable_object_item = TrainTimetableObject.from_dict(odpttrain_timetable_object_item_data)

            odpttrain_timetable_object.append(odpttrain_timetable_object_item)

        dctissued = d.pop("dct:issued", UNSET)

        dctvalid = d.pop("dct:valid", UNSET)

        odptrail_direction = d.pop("odpt:railDirection", UNSET)

        odptcalendar = d.pop("odpt:calendar", UNSET)

        odpttrain = d.pop("odpt:train", UNSET)

        odpttrain_type = d.pop("odpt:trainType", UNSET)

        odpttrain_name = []
        _odpttrain_name = d.pop("odpt:trainName", UNSET)
        for odpttrain_name_item_data in _odpttrain_name or []:
            odpttrain_name_item = MultilingualTitle.from_dict(odpttrain_name_item_data)

            odpttrain_name.append(odpttrain_name_item)

        odpttrain_owner = d.pop("odpt:trainOwner", UNSET)

        odptorigin_station = cast(List[str], d.pop("odpt:originStation", UNSET))

        odptdestination_station = cast(List[str], d.pop("odpt:destinationStation", UNSET))

        odptvia_station = cast(List[str], d.pop("odpt:viaStation", UNSET))

        odptvia_railway = cast(List[str], d.pop("odpt:viaRailway", UNSET))

        odptprevious_train_timetable = cast(List[str], d.pop("odpt:previousTrainTimetable", UNSET))

        odptnext_train_timetable = cast(List[str], d.pop("odpt:nextTrainTimetable", UNSET))

        odptneed_extra_fee = d.pop("odpt:needExtraFee", UNSET)

        _odptnote = d.pop("odpt:note", UNSET)
        odptnote: Union[Unset, MultilingualTitle]
        if isinstance(_odptnote, Unset):
            odptnote = UNSET
        else:
            odptnote = MultilingualTitle.from_dict(_odptnote)

        train_timetable = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptrailway=odptrailway,
            odpttrain_number=odpttrain_number,
            odpttrain_timetable_object=odpttrain_timetable_object,
            dctissued=dctissued,
            dctvalid=dctvalid,
            odptrail_direction=odptrail_direction,
            odptcalendar=odptcalendar,
            odpttrain=odpttrain,
            odpttrain_type=odpttrain_type,
            odpttrain_name=odpttrain_name,
            odpttrain_owner=odpttrain_owner,
            odptorigin_station=odptorigin_station,
            odptdestination_station=odptdestination_station,
            odptvia_station=odptvia_station,
            odptvia_railway=odptvia_railway,
            odptprevious_train_timetable=odptprevious_train_timetable,
            odptnext_train_timetable=odptnext_train_timetable,
            odptneed_extra_fee=odptneed_extra_fee,
            odptnote=odptnote,
        )

        train_timetable.additional_properties = d
        return train_timetable

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
