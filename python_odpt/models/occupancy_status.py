from enum import Enum


class OccupancyStatus(str, Enum):
    ODPT_OCCUPANCYSTATUSCRUSHEDSTANDINGROOMONLY = "odpt.OccupancyStatus:CrushedStandingRoomOnly"
    ODPT_OCCUPANCYSTATUSEMPTY = "odpt.OccupancyStatus:Empty"
    ODPT_OCCUPANCYSTATUSFEWSEATSAVAILABLE = "odpt.OccupancyStatus:FewSeatsAvailable"
    ODPT_OCCUPANCYSTATUSFULLROOMONLY = "odpt.OccupancyStatus:FullRoomOnly"
    ODPT_OCCUPANCYSTATUSMANYSEATSAVAILABLE = "odpt.OccupancyStatus:ManySeatsAvailable"
    ODPT_OCCUPANCYSTATUSNOTACCEPTINGPASSENGERS = "odpt.OccupancyStatus:NotAcceptingPassengers"
    ODPT_OCCUPANCYSTATUSSTANDINGROOMONLY = "odpt.OccupancyStatus:StandingRoomOnly"

    def __str__(self) -> str:
        return str(self.value)
