from enum import Enum


class PassengerSurveyType(str, Enum):
    ODPTPASSENGERSURVEY = "odpt:PassengerSurvey"

    def __str__(self) -> str:
        return str(self.value)
