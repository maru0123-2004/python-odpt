from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.passenger_survey_type import PassengerSurveyType

if TYPE_CHECKING:
    from ..models.passenger_survey_object import PassengerSurveyObject


T = TypeVar("T", bound="PassengerSurvey")


@_attrs_define
class PassengerSurvey:
    """駅の乗降人員数または乗車人員数

    Attributes:
        context (str): JSON-LD仕様に基づく @context のURL Example: http://vocab.odpt.org/context_odpt.jsonld.
        id (str): 固有識別子
        type (PassengerSurveyType): クラス名 Example: odpt:PassengerSurvey.
        dcdate (str): ISO8601 日付時刻形式
        owlsame_as (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptoperator (str): 固有識別子の別名 多くが`odpt.hoge:fuga`形式
        odptstation (List[str]): 駅を表すIDのリスト Example: ['odpt.Station:JR-East.Yamanote.Tokyo', 'odpt.Station:JR-
            East.ChuoRapid.Tokyo'].
        odptrailway (List[str]): 路線を表すIDのリスト Example: ['odpt.Railway:JR-East.Yamanote', 'odpt.Railway:JR-
            East.ChuoRapid'].
        odptinclude_alighting (bool): 乗降人員(降車を含む)の場合はtrue、乗車人員(降車を含まない)の場合はfalse Example: True.
        odptpassenger_survey_object (List['PassengerSurveyObject']): 調査年度と平均乗降人員数(または乗車人員数)の組のリスト Example:
            [{'odpt:surveyYear': 2017, 'odpt:passengerJourneys': 12345}].
    """

    context: str
    id: str
    type: PassengerSurveyType
    dcdate: str
    owlsame_as: str
    odptoperator: str
    odptstation: List[str]
    odptrailway: List[str]
    odptinclude_alighting: bool
    odptpassenger_survey_object: List["PassengerSurveyObject"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = self.context

        id = self.id

        type = self.type.value

        dcdate = self.dcdate

        owlsame_as = self.owlsame_as

        odptoperator = self.odptoperator

        odptstation = self.odptstation

        odptrailway = self.odptrailway

        odptinclude_alighting = self.odptinclude_alighting

        odptpassenger_survey_object = []
        for odptpassenger_survey_object_item_data in self.odptpassenger_survey_object:
            odptpassenger_survey_object_item = odptpassenger_survey_object_item_data.to_dict()
            odptpassenger_survey_object.append(odptpassenger_survey_object_item)

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
                "odpt:station": odptstation,
                "odpt:railway": odptrailway,
                "odpt:includeAlighting": odptinclude_alighting,
                "odpt:passengerSurveyObject": odptpassenger_survey_object,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.passenger_survey_object import PassengerSurveyObject

        d = src_dict.copy()
        context = d.pop("@context")

        id = d.pop("@id")

        type = PassengerSurveyType(d.pop("@type"))

        dcdate = d.pop("dc:date")

        owlsame_as = d.pop("owl:sameAs")

        odptoperator = d.pop("odpt:operator")

        odptstation = cast(List[str], d.pop("odpt:station"))

        odptrailway = cast(List[str], d.pop("odpt:railway"))

        odptinclude_alighting = d.pop("odpt:includeAlighting")

        odptpassenger_survey_object = []
        _odptpassenger_survey_object = d.pop("odpt:passengerSurveyObject")
        for odptpassenger_survey_object_item_data in _odptpassenger_survey_object:
            odptpassenger_survey_object_item = PassengerSurveyObject.from_dict(odptpassenger_survey_object_item_data)

            odptpassenger_survey_object.append(odptpassenger_survey_object_item)

        passenger_survey = cls(
            context=context,
            id=id,
            type=type,
            dcdate=dcdate,
            owlsame_as=owlsame_as,
            odptoperator=odptoperator,
            odptstation=odptstation,
            odptrailway=odptrailway,
            odptinclude_alighting=odptinclude_alighting,
            odptpassenger_survey_object=odptpassenger_survey_object,
        )

        passenger_survey.additional_properties = d
        return passenger_survey

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
