from enum import Enum


class CalendarType(str, Enum):
    ODPTCALENDAR = "odpt:Calendar"

    def __str__(self) -> str:
        return str(self.value)
