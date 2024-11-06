from enum import Enum


class BusroutePatternFareType(str, Enum):
    ODPTBUSROUTEPATTERNFARE = "odpt:BusroutePatternFare"

    def __str__(self) -> str:
        return str(self.value)
