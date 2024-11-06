from enum import Enum


class TrainTimetableType(str, Enum):
    ODPTTRAINTIMETABLE = "odpt:TrainTimetable"

    def __str__(self) -> str:
        return str(self.value)
