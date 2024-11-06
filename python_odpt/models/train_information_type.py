from enum import Enum


class TrainInformationType(str, Enum):
    ODPTTRAININFORMATION = "odpt:TrainInformation"

    def __str__(self) -> str:
        return str(self.value)
