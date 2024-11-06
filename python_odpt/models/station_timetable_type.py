from enum import Enum


class StationTimetableType(str, Enum):
    ODPTSTATIONTIMETABLE = "odpt:StationTimetable"

    def __str__(self) -> str:
        return str(self.value)
