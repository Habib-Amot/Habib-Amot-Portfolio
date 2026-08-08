# this file contains validators that are used to validate values of a field
from django.core.exceptions import ValidationError
import string

def VALIDATECHARACTERS(value):
    print("i was called")
    valid_character = set(string.ascii_letters + string.digits + string.whitespace)
    value_set = set(value)
    if value_set - valid_character:
        raise ValidationError(message="Username can only contain alpahabets, numbers or space", code='invalid_username_char')
