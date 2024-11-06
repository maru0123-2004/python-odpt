from enum import Enum


class FlightInformationArrivalType(str, Enum):
    ODPTFLIGHTINFORMATIONARRIVAL = "odpt:FlightInformationArrival"

    def __str__(self) -> str:
        return str(self.value)
