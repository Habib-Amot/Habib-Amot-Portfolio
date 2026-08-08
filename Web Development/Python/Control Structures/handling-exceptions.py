""" Exception handling is the process of capturing runtime errors and properly handling them before they propagate
    they are caught using try:
        # TODO: write code...
    except Exception, e:
        raise e
    block
"""

print("{0:=^40}".format("[HANDLING EXCEPTION]"))
d = {
    0:"Admin",
    1: "habib",
    2: "samad"
}

# while handling exceptions, it is necessary we keep the right order in which the exception will be handled
# by firsr considering the most specific exception before the broad ones 
try:
    print("performing a lookup action")
    print()
    print(d[3])
except KeyError as e:
    print("error while accessing key", e)
    print("Error handled successfully...")
    print()
except LookupError:
    print("lookup action failed")
except Exception as e:
    print(e)
else:
    print("no exception was raised ")
finally:
    print("performing clean up actions here")

print()
print("{0:=^40}".format("[RAISING EXCEPTION"))
# raising exceptions can be either raising an exception alone or chaining the exception
# or allowing the exception determine what it should raise 
# for example

user_id = int(input("Enter your id: "))
if 0 == user_id or user_id >= 3:
    raise ValueError("id must be 1 or 2")
else:
    print("welcome {}".format(d[user_id]))
print()
print("Chaining errors:")
print("say the user enters 0 which is admin ID")


def get_user_id(exception_class):
    user_id = int(input("Enter your id: "))
    try:
        if user_id == 0:
            raise exception_class("Access denied")
    except exception_class as err:
        raise Exception(err) from exception_class



get_user_id(LookupError)

print()
print("{0:=^40}".format("[Custom EXCEPTION"))

# lets create a new EXCEPTION class
class AccessDeniedError(Exception):
    pass

get_user_id(AccessDeniedError)
