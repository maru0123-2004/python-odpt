from enum import Enum


class BusstopPoleType(str, Enum):
    ODPTBUSSTOPPOLE = "odpt:BusstopPole"

    def __str__(self) -> str:
        return str(self.value)
