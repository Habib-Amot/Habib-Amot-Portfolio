# this class is responsible for creating incidents objects
# each incident has a report id, the date, airport, aircraft id, aircraft type, pilot fly hours, midair and narrative


class Incident:
    REPORT_ID = set()  # holds all object id
    
    def __init__(self, report_id, date, airport, aircraft_id, aircraft_type, pilot_total_hours, midair, narrative=""):
        assert len(report_id) >= 8 and len(report_id.split()) == 1 and report_id not in self.REPORT_ID, "invalid report id or report id existed"
        self.REPORT_ID.add(report_id)
        self.__report_id = report_id
        self.date = date
        self.airport = airport
        self.aircraft_type = aircraft_type
        self.aircraft_id = aircraft_id
        self.pilot_total_hours = pilot_total_hours
        self.midair = midair
        self.narrative = narrative
    
    
    @property
    def report_id(self):
        return self.__report_id


class IncidentCollection(dict):
    
    def items(self):
        for item in self.keys():
            yield (item, self[item])
    
    def values(self):
        for value in self.keys():
            yield self[value]
    
    def __iter__(self):
        keys = sorted(super().keys())
        for k in keys:
            yield k
    
    keys = __iter__

print("test")


i = Incident("23467136", 123, "Dana Airport", 23456, "sonic", 2000, 12, )
print(i.REPORT_ID)

"""i = Incident("23567136", 123, "Dana Airport", 23456, "sonic", 2000, 12, )
print(i.REPORT_ID)"""

collections = IncidentCollection({i.report_id: i})
for item in collections:
    print(item)
