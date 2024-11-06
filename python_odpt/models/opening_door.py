from enum import Enum


class OpeningDoor(str, Enum):
    ODPTOPENINGDOORFRONTSIDE = "odpt:OpeningDoor:FrontSide"
    ODPTOPENINGDOORREARSIDE = "odpt:OpeningDoor:RearSide"

    def __str__(self) -> str:
        return str(self.value)
