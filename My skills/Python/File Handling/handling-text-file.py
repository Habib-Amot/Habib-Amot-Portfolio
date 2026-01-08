# in this lesson, I am going to be reading and writing to files in text mode.
# Given a collection of an Incident object, I am going to be looping over all the items in the dictionary and then
# writing them to a text file

import datetime
from incidents import Incident, IncidentCollection

crash_101 = Incident("12367091", str(datetime.datetime.now().date()), "Danax", 234213, "Boeing", 3000, "300")
crash_102 = Incident("12368001", str(datetime.datetime.now().date()), "Danax", 234213, "Blaze-400", 3000, "300", "flew for 200 minutes before engine stops")
crash_collections = IncidentCollection({crash_101.report_id:crash_101, crash_102.report_id: crash_102})


crash_collections.export_to_text(filename="incidents.txt")  # this is going to store the collection object into a text file

# and now the data is also going to loaded back inside the text file using the import_from_text method
incidents = IncidentCollection()
if incidents.import_from_text("incidents.txt"):
    print(incidents)
