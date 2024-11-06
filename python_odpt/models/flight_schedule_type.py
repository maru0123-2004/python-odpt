from enum import Enum


class FlightScheduleType(str, Enum):
    ODPTFLIGHTSCHEDULE = "odpt:FlightSchedule"

    def __str__(self) -> str:
        return str(self.value)
