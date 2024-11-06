from enum import Enum


class BusType(str, Enum):
    ODPTBUS = "odpt:Bus"

    def __str__(self) -> str:
        return str(self.value)
