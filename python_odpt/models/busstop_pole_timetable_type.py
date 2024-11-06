from enum import Enum


class BusstopPoleTimetableType(str, Enum):
    ODPTBUSSTOPPOLETIMETABLE = "odpt:BusstopPoleTimetable"

    def __str__(self) -> str:
        return str(self.value)
