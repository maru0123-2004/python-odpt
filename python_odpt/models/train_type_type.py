from enum import Enum


class TrainTypeType(str, Enum):
    ODPTTRAINTYPE = "odpt:TrainType"

    def __str__(self) -> str:
        return str(self.value)
