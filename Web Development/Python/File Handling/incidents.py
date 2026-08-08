# this class is responsible for creating incidents objects
# each incident has a report id, the date, airport, aircraft id, aircraft type, pilot fly hours, midair and narrative
import datetime
from textwrap import TextWrapper


class Incident:
    REPORT_ID = set()  # holds all object id
    
    def __init__(self, report_id: str, date: str, airport: str, aircraft_id: int, aircraft_type: str, pilot_total_hours: int, midair: str, narrative: str=""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1 and report_id not in self.REPORT_ID, "invalid report id or report id existed"
        self.REPORT_ID.add(report_id)
        self.__report_id = report_id
        self.__date = date
        self.airport = airport
        self.aircraft_type = aircraft_type
        self.aircraft_id = aircraft_id
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative

    def __str__(self) -> str:
        return self.narrative if self.narrative else self.__report_id

    def __repr__(self) -> str:
        return "Incident({0})".format(self.__report_id)

    @property
    def report_id(self):
        return self.__report_id
    
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        assert isinstance(value, datetime.date), "value must be of type datetime"
        self.__date = value


class ParseFileError(Exception): pass


class IncidentCollection(dict):
    
    def items(self):
        for item in self.keys():
            yield item, self[item]
    
    def values(self):
        for value in self.keys():
            yield self[value]
    
    def __iter__(self):
        keys = sorted(super().keys())
        for k in keys:
            yield k
    
    keys = __iter__

    def export_to_text(self, filename):
        # this converts the given object into text
        try:
            with open(filename, 'w') as file:
                wrapper = TextWrapper(initial_indent="    ", subsequent_indent="    ")
                for incident in self.values():
                    narrative = "\n".join(wrapper.wrap(incident.narrative))
                    file.write("""[{incident.report_id}]\n\tdate={incident.date}\n\taircraft id={incident.aircraft_id}\n\tairport={incident.airport}\n\taircraft_type={incident.aircraft_type}\n\tpilot total hours={incident.pilot_total_hours}\n\tmidair={incident.midair}\n.NARRATIVE START\n{narrative}\n.NARRATIVE END\n\n""".format(incident=incident, narrative=narrative)
                )
                return True
        except EnvironmentError as err:
            print(err)
            return False
    
    def import_from_text(self, filename):
        narrative = None
        enter_narrative = False
        incident_data = {}
        try:
            with open(filename) as file:
                self.clear()
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()
                    if not line and narrative is None:
                        continue

                    if enter_narrative:
                        if line.startswith(".NARRATIVE END"):
                            incident = Incident(**incident_data)
                            self.update({incident.report_id: incident})
                            incident_data = {}
                            narrative = None
                            enter_narrative = False
                        else:
                            incident_data["narrative"] = line

                    elif line.startswith("[") and line[-1] == "]":  # this mean that this is the beginning of an incident
                        report_id = line[1: -1]
                        if report_id in Incident.REPORT_ID:
                            Incident.REPORT_ID.remove(report_id)

                        incident_data['report_id'] = report_id
                    elif "=" in line:
                        field, value = line.split("=")
                        field = field.strip()
                        if field == "date":
                            incident_data["date"] = datetime.datetime.strptime(value, "%Y-%m-%d").date()
                        elif field == "aircraft id":
                            incident_data["aircraft_id"] = value
                        elif field == "airport":
                            incident_data["airport"] = value
                        elif field == "aircraft_type":
                            incident_data["aircraft_type"] = value
                        elif field == "pilot total hours":
                            incident_data["pilot_total_hours"] = value
                        else:
                            incident_data[field] = value
                    
                    elif line.startswith(".NARRATIVE START"):
                        enter_narrative = True
                        narrative = ""

                    else:
                        raise ParseFileError("unable to parse file at line {0}".format(line_number))
                return True
        except EnvironmentError as err:
            print(err)
            return False

