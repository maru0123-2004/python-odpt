from enum import Enum


class AirportType(str, Enum):
    ODPTAIRPORT = "odpt:Airport"

    def __str__(self) -> str:
        return str(self.value)
