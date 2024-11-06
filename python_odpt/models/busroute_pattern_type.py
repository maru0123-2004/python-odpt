from enum import Enum


class BusroutePatternType(str, Enum):
    ODPTBUSROUTEPATTERN = "odpt:BusroutePattern"

    def __str__(self) -> str:
        return str(self.value)
