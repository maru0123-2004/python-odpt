from enum import Enum


class AirportTerminalType(str, Enum):
    ODPTAIRPORTTERMINAL = "odpt:AirportTerminal"

    def __str__(self) -> str:
        return str(self.value)
