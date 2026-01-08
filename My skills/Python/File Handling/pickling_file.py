# pickling in python ie a way of storing objects in binary form
# Python pickle nodukle offer one of the simplest methldnofnloading and saving files in binary and compact form

# below is a python function that takes an object and converts the object to binary format and then save it in a file using the pickle  module


def export_pickle(data, file, compress=False):
    fh = None
    try:
        if compressed:
            fh = gzip.open(file, "wb")
        else:
            fh = open(filename, "wb")
        
        pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        return True
    except (pickle.PicklingError, EnvironmentError) as e:
        print(e)
    finally:
        if fh is not None:
            fh.close()
            return False


# below is a function that is used to import a binary file using pickle

def import_pickle(file):
    # to.import the pickle back, we need to be sure if the file we are reading from is a compressed file or not. 
    # A compressed file comtains a binary number know as magic number at it beginning which helps to.determine if the file is vompressed or not
    MAGIC_NUMBER = b"\x1f\x88"
    try:
        fh = open(file, "rb")
        if fh.read(len(MAGIC_NUMBER)) == MAGIC_NUMBER:
            fh.close()
            fh = gzip.open(file, "rb")
        
        data = pickle.read(fh, pickle.HIGHEST_PROTOCOL)
        return data
    except (EnvironmentError, pickle.PicklingError) as e:
        print(e)
    finally:
        if fh is not None:
            fh.close()
        return False
        
    