import sys
import unicodedata
import math, cmath
from collections import namedtuple

def show_help() -> None:
    print("Usage: {0[0]} [string]".format(sys.argv))


def main():
    if len(sys.argv) < 2:
        show_help()

    else:
        print()
        print("{0:-^40}".format(f"[Unicode name containing {sys.argv[1]}]"))
        print()
        print('{0:^7}  {1:^4}  {2:^3}  {3:^40}'.format('decimal', 'hex', 'chr', "name"))
        print('{0:-^7}  {0:-^4}  {0:-^3}  {0:-^40}'.format(''))
        unicode_printer(sys.argv[1])

def unicode_printer(name: str):
    start_char = ord(" ")  # this is the start number which is the number representing zero
    max_unicode = sys.maxunicode  # the maximum character that can be processed by the system
    while start_char < max_unicode:
        character = chr(start_char)
        character_name = unicodedata.name(character, "*** unknown ***")  # getting the name of our character
        if name in character_name.lower():
            print("{0:>7}  {0:^5x}  {0:^c}  {1}".format(start_char, character_name))
        start_char += 1


def quadratic_equation(a:float, b:float, c:float):
    # printing out the formular for recall purpose
    print("quadratic formular: ax\N{superscript two} + bx + c = 0")

    # instantiating our roots
    x1 = None
    x2 = None
    root = 0.0
    discriminant = (b**2 - (4 * a * c))
    if discriminant > 0:
        root = math.sqrt(discriminant)
    elif discriminant == 0:
        x1 = -b / (2 * a)
    elif discriminant < 0:
        root = cmath.sqrt(discriminant)
    
    if x1 is None:
        x1 = (-b + root)/(2 * a)
        x2 = (-b - root)/(2 * a)
        print(f"the root of our equation is {x1}, {x2}")
    else:
        print(f"the root of our equation is {x1}")


# main()
# quadratic_equation(1, 3, 4)

# this exercise is for collection types lesson

# we are to create a usernames from file of user data

user_profile = namedtuple('User', 'id username forename middlename surname department')
ID, FIRST_NAME, MIDDLENAME, SURNNAME, DEPT = range(5)


def username_generator(file_name: str) -> None:
    users = {}
    usernames = set()
    try:
        for line in open(file_name):
            line = line.strip()
            if line:
                user = process_line(line, usernames)
                users[user.id] = user
        
        if users:
            print_users(users)

    except FileNotFoundError, OSError:
        print("Unable to locate file {}".format(file_name))


def process_line(line: str, usernames: set) -> user_profile:
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = user_profile(
        username=username, id=fields[ID], forename=fields[FIRST_NAME], middlename=fields[MIDDLENAME], surname=fields[SURNNAME], department=fields[DEPT]
    )
    return user


def generate_username(fields: list, usernames: set) -> str:
    username = fields[SURNNAME][0] + fields[FIRST_NAME]+fields[MIDDLENAME][:1] + fields[ID][:2]
    real_username = username[:8]
    count = 0
    while real_username in usernames:
        real_username = "{0}{1}".format(real_username, count)
        count += 1
    usernames.add(real_username)
    return real_username


def print_users(users: dict) -> None:
    print("This are the users that we have in our company")
    if users:
        print("{0:^4}  {1:^12}  {2:^12}  {3:^16}  {4:^10}".format("ID", "Firstname", "Surname", "Dept", "Username"))
        print("{0:->4}  {1:->12}  {2:->12}  {3:->16}  {4:->10}".format("", "", "", "", ""))
        for user in users:
            print("{0:<4}  {1.forename:<12}  {1.surname:<12}  {1.department:<16}  {1.username:<10}".format(user, users[user]))
        print()


username_generator('user-data.txt')
