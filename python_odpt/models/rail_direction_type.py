from enum import Enum


class RailDirectionType(str, Enum):
    ODPTRAILDIRECTION = "odpt:RailDirection"

    def __str__(self) -> str:
        return str(self.value)
