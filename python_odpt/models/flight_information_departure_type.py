from enum import Enum


class FlightInformationDepartureType(str, Enum):
    ODPTFLIGHTINFORMATIONDEPARTURE = "odpt:FlightInformationDeparture"

    def __str__(self) -> str:
        return str(self.value)
