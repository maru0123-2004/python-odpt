from enum import Enum


class BusDoorStatus(str, Enum):
    CLOSE = "close"
    OPEN = "open"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
