from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PassengerSurveyObject")


@_attrs_define
class PassengerSurveyObject:
    """調査年度と平均乗降人員数(または乗車人員数)の組

    Attributes:
        odptsurvey_year (int): 調査年度 Example: 2017.
        odptpassenger_journeys (int): 駅の1日あたりの平均乗降人員数(または乗車人員数) Example: 12345.
    """

    odptsurvey_year: int
    odptpassenger_journeys: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        odptsurvey_year = self.odptsurvey_year

        odptpassenger_journeys = self.odptpassenger_journeys

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "odpt:surveyYear": odptsurvey_year,
                "odpt:passengerJourneys": odptpassenger_journeys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        odptsurvey_year = d.pop("odpt:surveyYear")

        odptpassenger_journeys = d.pop("odpt:passengerJourneys")

        passenger_survey_object = cls(
            odptsurvey_year=odptsurvey_year,
            odptpassenger_journeys=odptpassenger_journeys,
        )

        passenger_survey_object.additional_properties = d
        return passenger_survey_object

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
