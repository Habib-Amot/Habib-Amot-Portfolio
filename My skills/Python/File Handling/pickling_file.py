# pickling in python ie a way of storing objects in binary form
# Python pickle module offer one of the simplest method of loading and saving files in binary and compact form

# below is a python function that takes an object and converts the object to binary format and then
# save it in a file using the pickle  module
import gzip
import pickle
import datetime

from incidents import IncidentCollection, Incident

# say I have two incidents that I want to record and also store in the incident collection 
crash_101 = Incident("12367091", str(datetime.datetime.now()), "Danax", 234213, "Boeing", 3000, "300")
crash_102 = Incident("12368001", str(datetime.datetime.now()), "Danax", 234213, "Blaze-400", 3000, "300", "flew for 200 minutes before engine stops")

crash_collections = IncidentCollection({crash_101.report_id:crash_101, crash_102.report_id: crash_102})


def export_pickle(data: Incident | IncidentCollection, filename, compressed=False):
    fh = None
    try:
        if compressed:
            fh = gzip.open(filename, "wb")
        else:
            fh = open(filename, "wb")
        
        pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        return True
    except (pickle.PicklingError, EnvironmentError) as e:
        print(e)
        return False
    finally:
        if fh is not None:
            fh.close()


# below is a function that is used to import a binary file using pickle

def import_pickle(file):
    # to.import the pickle back, we need to be sure if the file we are reading from is a compressed file or not. 
    # A compressed file contains a binary number know as magic number at it beginning which helps to.determine if the
    # file is compressed or not
    MAGIC_NUMBER = b"\x1f\x88"
    fh = None
    try:
        fh = open(file, "rb")
        if fh.read(len(MAGIC_NUMBER)) == MAGIC_NUMBER:
            fh.close()
            fh = gzip.open(file, "rb")
        
        data = pickle.load(fh)
        return data
    except (EnvironmentError, pickle.PicklingError) as e:
        print(e)
        return False
    finally:
        if fh is not None:
            fh.close()


export_pickle(crash_collections, "crash_case.pkl")
