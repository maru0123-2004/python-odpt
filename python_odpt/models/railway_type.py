from enum import Enum


class RailwayType(str, Enum):
    ODPTRAILWAY = "odpt:Railway"

    def __str__(self) -> str:
        return str(self.value)
