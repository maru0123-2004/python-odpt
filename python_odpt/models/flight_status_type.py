from enum import Enum


class FlightStatusType(str, Enum):
    ODPTFLIGHTSTATUS = "odpt:FlightStatus"

    def __str__(self) -> str:
        return str(self.value)
