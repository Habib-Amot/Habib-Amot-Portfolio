""" branching allows for the execution of python programs without the regular sequential flow of programs
    There are 2 main branching techniques in Python:
    if else statement and match statement
"""

# here is a simple program that checks the length of a user name and their age to determine if they will be give discount or not

username = "Amot The Dev"
age = 25

if len(username) > 15:
    print("You are not eligible for discount. Name too long")
elif age > 30:
    print("Name is okay, but you are old for discount")
else:
    print(
        "Congratulations, you are eligble for discount"
        )
    # now lets assign a class for this user to know the class of eligibility
    user_class = "premium user" if age <= 25 else "super user"
    print("You are a {0}".format(user_class))
    

# we can also make use of match statements 
username = input("please enter your name: ")
match username.lower():
    case len(username)
