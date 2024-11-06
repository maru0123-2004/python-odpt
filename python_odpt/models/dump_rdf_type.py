from enum import Enum


class DumpRDFType(str, Enum):
    ODPTAIRPORT = "odpt:Airport"
    ODPTAIRPORTTERMINAL = "odpt:AirportTerminal"
    ODPTBUSROUTEPATTERN = "odpt:BusroutePattern"
    ODPTBUSROUTEPATTERNFARE = "odpt:BusroutePatternFare"
    ODPTBUSSTOPPOLE = "odpt:BusstopPole"
    ODPTBUSSTOPPOLETIMETABLE = "odpt:BusstopPoleTimetable"
    ODPTBUSTIMETABLE = "odpt:BusTimetable"
    ODPTCALENDAR = "odpt:Calendar"
    ODPTFLIGHTSCHEDULE = "odpt:FlightSchedule"
    ODPTFLIGHTSTATUS = "odpt:FlightStatus"
    ODPTOPERATOR = "odpt:Operator"
    ODPTPASSENGERSURVEY = "odpt:PassengerSurvey"
    ODPTRAILDIRECTION = "odpt:RailDirection"
    ODPTRAILWAY = "odpt:Railway"
    ODPTRAILWAYFARE = "odpt:RailwayFare"
    ODPTSTATION = "odpt:Station"
    ODPTSTATIONTIMETABLE = "odpt:StationTimetable"
    ODPTTRAINTIMETABLE = "odpt:TrainTimetable"
    ODPTTRAINTYPE = "odpt:TrainType"

    def __str__(self) -> str:
        return str(self.value)
