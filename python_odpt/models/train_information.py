from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.train_information_type import TrainInformationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multilingual_title import MultilingualTitle


T = TypeVar("T", bound="TrainInformation")


@_attrs_define
class TrainInformation:
    """列車運行情報

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (TrainInformationType): クラス名 Example: odpt:TrainInformation.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttime_of_origin (str): ISO8601 日付時刻形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_information_text (MultilingualTitle): 多言語対応のタイトル
        dctvalid (Union[Unset, str]): ISO8601 日付時刻形式
        odptrailway (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_information_status (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptrail_direction (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_information_area (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odpttrain_information_kind (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odptstation_from (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptstation_to (Union[Unset, str]): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odpttrain_information_range (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odpttrain_information_cause (Union[Unset, MultilingualTitle]): 多言語対応のタイトル
        odpttransfer_railways (Union[Unset, List[str]]): 振替路線一覧のリスト Example: ['odpt.Railway:JR-East.Yamanote'].
        odptresume_estimate (Union[Unset, str]): ISO8601 日付時刻形式
    """

    context: str
    id: str
    type: TrainInformationType
    dcdate: str
    owlsame_as: str
    odpttime_of_origin: str
    odptoperator: str
    odpttrain_information_text: "MultilingualTitle"
    dctvalid: Union[Unset, str] = UNSET
    odptrailway: Union[Unset, str] = UNSET
    odpttrain_information_status: Union[Unset, "MultilingualTitle"] = UNSET
    odptrail_direction: Union[Unset, str] = UNSET
    odpttrain_information_area: Union[Unset, "MultilingualTitle"] = UNSET
    odpttrain_information_kind: Union[Unset, "MultilingualTitle"] = UNSET
    odptstation_from: Union[Unset, str] = UNSET
    odptstation_to: Union[Unset, str] = UNSET
    odpttrain_information_range: Union[Unset, "MultilingualTitle"] = UNSET
    odpttrain_information_cause: Union[Unset, "MultilingualTitle"] = UNSET
    odpttransfer_railways: Union[Unset, List[str]] = UNSET
    odptresume_estimate: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odpttime_of_origin = self.odpttime_of_origin

        odptoperator = self.odptoperator

        odpttrain_information_text = self.odpttrain_information_text.to_dict()

        dctvalid = self.dctvalid

        odptrailway = self.odptrailway

        odpttrain_information_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odpttrain_information_status, Unset):
            odpttrain_information_status = self.odpttrain_information_status.to_dict()

        odptrail_direction = self.odptrail_direction

        odpttrain_information_area: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odpttrain_information_area, Unset):
            odpttrain_information_area = self.odpttrain_information_area.to_dict()

        odpttrain_information_kind: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odpttrain_information_kind, Unset):
            odpttrain_information_kind = self.odpttrain_information_kind.to_dict()

        odptstation_from = self.odptstation_from

        odptstation_to = self.odptstation_to

        odpttrain_information_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odpttrain_information_range, Unset):
            odpttrain_information_range = self.odpttrain_information_range.to_dict()

        odpttrain_information_cause: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.odpttrain_information_cause, Unset):
            odpttrain_information_cause = self.odpttrain_information_cause.to_dict()

        odpttransfer_railways: Union[Unset, List[str]] = UNSET
        if not isinstance(self.odpttransfer_railways, Unset):
            odpttransfer_railways = self.odpttransfer_railways

        odptresume_estimate = self.odptresume_estimate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "@id": id,
                "@type": type,
                "dc:date": dcdate,
                "owl:sameAs": owlsame_as,
                "odpt:timeOfOrigin": odpttime_of_origin,
                "odpt:operator": odptoperator,
                "odpt:trainInformationText": odpttrain_information_text,
            }
        )
        if dctvalid is not UNSET:
            field_dict["dct:valid"] = dctvalid
        if odptrailway is not UNSET:
            field_dict["odpt:railway"] = odptrailway
        if odpttrain_information_status is not UNSET:
            field_dict["odpt:trainInformationStatus"] = odpttrain_information_status
        if odptrail_direction is not UNSET:
            field_dict["odpt:railDirection"] = odptrail_direction
        if odpttrain_information_area is not UNSET:
            field_dict["odpt:trainInformationArea"] = odpttrain_information_area
        if odpttrain_information_kind is not UNSET:
            field_dict["odpt:trainInformationKind"] = odpttrain_information_kind
        if odptstation_from is not UNSET:
            field_dict["odpt:stationFrom"] = odptstation_from
        if odptstation_to is not UNSET:
            field_dict["odpt:stationTo"] = odptstation_to
        if odpttrain_information_range is not UNSET:
            field_dict["odpt:trainInformationRange"] = odpttrain_information_range
        if odpttrain_information_cause is not UNSET:
            field_dict["odpt:trainInformationCause"] = odpttrain_information_cause
        if odpttransfer_railways is not UNSET:
            field_dict["odpt:transferRailways"] = odpttransfer_railways
        if odptresume_estimate is not UNSET:
            field_dict["odpt:resumeEstimate"] = odptresume_estimate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.multilingual_title import MultilingualTitle

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = TrainInformationType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odpttime_of_origin = d.pop("odpt:timeOfOrigin")

        odptoperator = d.pop("odpt:operator")

        odpttrain_information_text = MultilingualTitle.from_dict(d.pop("odpt:trainInformationText"))

        dctvalid = d.pop("dct:valid", UNSET)

        odptrailway = d.pop("odpt:railway", UNSET)

        _odpttrain_information_status = d.pop("odpt:trainInformationStatus", UNSET)
        odpttrain_information_status: Union[Unset, MultilingualTitle]
        if isinstance(_odpttrain_information_status, Unset):
            odpttrain_information_status = UNSET
        else:
            odpttrain_information_status = MultilingualTitle.from_dict(_odpttrain_information_status)

        odptrail_direction = d.pop("odpt:railDirection", UNSET)

        _odpttrain_information_area = d.pop("odpt:trainInformationArea", UNSET)
        odpttrain_information_area: Union[Unset, MultilingualTitle]
        if isinstance(_odpttrain_information_area, Unset):
            odpttrain_information_area = UNSET
        else:
            odpttrain_information_area = MultilingualTitle.from_dict(_odpttrain_information_area)

        _odpttrain_information_kind = d.pop("odpt:trainInformationKind", UNSET)
        odpttrain_information_kind: Union[Unset, MultilingualTitle]
        if isinstance(_odpttrain_information_kind, Unset):
            odpttrain_information_kind = UNSET
        else:
            odpttrain_information_kind = MultilingualTitle.from_dict(_odpttrain_information_kind)

        odptstation_from = d.pop("odpt:stationFrom", UNSET)

        odptstation_to = d.pop("odpt:stationTo", UNSET)

        _odpttrain_information_range = d.pop("odpt:trainInformationRange", UNSET)
        odpttrain_information_range: Union[Unset, MultilingualTitle]
        if isinstance(_odpttrain_information_range, Unset):
            odpttrain_information_range = UNSET
        else:
            odpttrain_information_range = MultilingualTitle.from_dict(_odpttrain_information_range)

        _odpttrain_information_cause = d.pop("odpt:trainInformationCause", UNSET)
        odpttrain_information_cause: Union[Unset, MultilingualTitle]
        if isinstance(_odpttrain_information_cause, Unset):
            odpttrain_information_cause = UNSET
        else:
            odpttrain_information_cause = MultilingualTitle.from_dict(_odpttrain_information_cause)

        odpttransfer_railways = cast(List[str], d.pop("odpt:transferRailways", UNSET))

        odptresume_estimate = d.pop("odpt:resumeEstimate", UNSET)

        train_information = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odpttime_of_origin=odpttime_of_origin,
            odptoperator=odptoperator,
            odpttrain_information_text=odpttrain_information_text,
            dctvalid=dctvalid,
            odptrailway=odptrailway,
            odpttrain_information_status=odpttrain_information_status,
            odptrail_direction=odptrail_direction,
            odpttrain_information_area=odpttrain_information_area,
            odpttrain_information_kind=odpttrain_information_kind,
            odptstation_from=odptstation_from,
            odptstation_to=odptstation_to,
            odpttrain_information_range=odpttrain_information_range,
            odpttrain_information_cause=odpttrain_information_cause,
            odpttransfer_railways=odpttransfer_railways,
            odptresume_estimate=odptresume_estimate,
        )

        train_information.additional_properties = d
        return train_information

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
