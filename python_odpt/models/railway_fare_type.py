from enum import Enum


class RailwayFareType(str, Enum):
    ODPTRAILWAYFARE = "odpt:RailwayFare"

    def __str__(self) -> str:
        return str(self.value)
