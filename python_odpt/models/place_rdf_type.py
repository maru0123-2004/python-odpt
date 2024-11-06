from enum import Enum


class PlaceRDFType(str, Enum):
    ODPTBUSSTOPPOLE = "odpt:BusstopPole"
    ODPTSTATION = "odpt:Station"

    def __str__(self) -> str:
        return str(self.value)
