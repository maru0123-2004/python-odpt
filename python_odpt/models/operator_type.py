from enum import Enum


class OperatorType(str, Enum):
    ODPTOPERATOR = "odpt:Operator"

    def __str__(self) -> str:
        return str(self.value)
