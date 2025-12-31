import time

""" loops are ways of running a particular for a specitied number of times or as long as a condition is met
    there are 2 types of loops in python:
    for loop and while loop
"""

print("{0:=^40}".format("[FOR LOOPS]"))
# for loops uses the syntax for in iterable
# to loop over a list of names 
names = ["habib", "Amot", "Amot The Dev"]
for name in names:
    print(name)

# or we can loop over a range of numbers and then print the decicmal, binary, octal and hex value of the num er
print("{0:^6} {1:^6} {2:^6} {3:^6}".format("Number", "Binary", "Octal", "Hex"))
print("{0:-^6} {0:-^6} {0:-^6} {0:-^6}".format(""))
for i in range(1, 17):
    print("{0:<#6} {0:<#6b} {0:<#6o} {0:<#6x}".format(i))


print()
print("{0:=^40}".format("[WHILE LOOPS]"))
# while loops are blocks that run as long as a condition is met

# for example, this loop creates a multiplication table
row = 1
print()
while row <= 12:
    line = ""
    header =""
    rule = ""
    for number in range(1, 13):
        if row == 1:
            header += f"{number:^10} "
            rule += "{0:-^10} ".format("")
        multiplication = row * number
        message = f"{number}x{row}={multiplication}"
        data = "{0:<10} ".format(message)
        line += data
    if row == 1:
        print(header)
        print(rule)
    time.sleep(1)
    print(line)
    row += 1
