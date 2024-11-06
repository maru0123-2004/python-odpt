from enum import Enum


class StationType(str, Enum):
    ODPTSTATION = "odpt:Station"

    def __str__(self) -> str:
        return str(self.value)
