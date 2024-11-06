from enum import Enum


class BusTimetableType(str, Enum):
    ODPTBUSTIMETABLE = "odpt:BusTimetable"

    def __str__(self) -> str:
        return str(self.value)
