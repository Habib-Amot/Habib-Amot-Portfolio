""" 
Strings are represented by the immutable str data type which holds a sequence of Unicode characters. 
"""
# strings can either be represented using single, double, triple-single and triple double quotes. e.g
name = 'habib'
full_name = "Habib Yakubu"
about_me = ''' Hey there, my name is Habib and I am python programmer \
    but this line will not come as a newline
'''
about_my_job = """ I am a python programmer
An AI automation expert and also a 
web developer"""
print(f'name {name} \nfull name: {full_name}\nAbout me: {about_me}')
print(f'about my job: {about_my_job}')
print()

print('='*50 + "[Escaping Special Character]" +"="*50)
# sometimes we might want to include some escape characters inside of out text, there are two ways to do this
# 1. use backslashes
print('this will come out as \\n rather than a newline because it has been escaped using backslash')
# 2. we can make use of raw strings
print(r'this will also not be processed as a \n newline because it is a raw string')
print()

print('='*50 + "[Unicode Characters]" +"="*50)
# printing of Unicode characters can also be achieved in several ways
# 1. making use of \N{char name} e.g
print('this is the euro sign \N{euro sign} and this is the dollar sign \N{dollar sign}')
# 2. we can make use the unicode numbers
print("I love \u2764 programming")
print()

""" Slicing and Striding Strings in Python """
# in slicing two integers are given, the start index number and the end index number. when the start is ommitted it defaults to 0
# and when the last index is omitted, it defaults to the length of the string - 1
# providing a negative in the start will cause the indexing to be invalid because slicing moves forward rather than backwards
print('='*50 + "[SLICING AND STRIDING]" +"="*50)
job_title = "The Python Programmer"
print(job_title[0], ': zero-th character')  # gets the first index
print(job_title[:6], ': zero to 6th -1 character')  # starts at 0 and proceeds to the 6th -1 character
print(job_title[1:], ': secondth to the last character')  # starts at index 1 and proceeds to the end of the character
print(job_title[:-1], ': zero to the last character minus one')  # starts from the first character and proceeds to the last character
# when it comes to striding, elements are first sliced and then strided. In this case, striding allows for backward and forward direction
print(job_title[::-1], ": slice from the first to the last character then starts from the back and use a step of 1 to pick items")
print(job_title[:6:2], ": slices from the first character to the 6th -1 character then use a start of 2 to select items")
print(job_title[::2], ": slices from the first character to the end character then use a start of 2 to select items")

print('='*50 + "[STRING OPERATORS]" +"="*50)
# string operators and methods
# in python, strings come with a lot of methods that allow for manipulation od the the string data e.g
print(f'''
      Hi, {full_name.lower().split(" ")[0]}
     Your full name is {full_name.upper()}
     Or {full_name.lower().title()}
     You have {full_name.count('a')} number of a in your name
     and your name {"can" if full_name.isidentifier() else "cannot"} be used as an identifier'''
)
# another example is that, we can make use string finding methods to look for substrings
# let's say we want to get the last path in a path string
path = r'C:\Users\user\Document'
# the last folder can be extracted using either, rpartition, rfind, find or rindex or index method
try:
    last_folder = path[path.rindex('\\') +1:]
    print(f"the last folder is {last_folder}")
except ValueError:
    print("invalid path given")

print('we can use the endswith method to determine if a string ends with a given choices or not')
file_name = "my-cat.png"
print(f'this file is {"a" if file_name.endswith(("jpeg", "jpg")) else "not"} jpeg file''')
# we can also make use of maketrans and tranlate method to create a translation rule of mapping
# characters to another characters
# e.g.
print('*'*10,'making translation','*'*10)
name_map = str.maketrans('Hau', 'Bei')
print(full_name.translate(name_map))

print()
print('='*50 + "[STRING FORMATTING WITH .format]" +"="*50)
# formatting involes making use of formatting fields, conversions and format specification inside our strings
# field names can be an integer or a value. If it is an integer, the value will be looked up in one of format positional argument
# and if the the field name is a value, the value will be looked up in one of .formtat keyword argument
# when arguments are passed into .format, the values are mapped to *args or **kwargs which are list and dictionary respectively and then the value
# will be looked up in one of this containers. If the field name is an int, the int will be used as lookup in the *args list and if the field name 
# is a value, the value will be used as a lookup index in the **kwargs dictionary e.g
sententce = "my name is {0} and I am the {position} born of my family. We are {1} in number and I am the only {gender} in the family"
print(sententce.format('habib', 12, gender='male', position='third'))
sententce2 = "how many {food_name} is being prepared for the {creature} in block {0}, room {1[room]}"
human_data = {'food_name': "vegetables", "creature":"Human", 'room':10}
print(sententce2.format(2, human_data, **human_data))
# from the example above, we can conclude that the format method takes in positional and keyword args and it uses them to build its list and dict
# which it uses to map field names to their corresponding values
""" Conversion of field names """
# after checking and knowing the data to work with, .format will then check if any conversion has been specified
# for example, we have this chineese movie name and we want to convert this ascii representational form, we can do this using the .format method
chineese_movie = "翻訳で失われる"
print("{0!a}".format(chineese_movie))  # converts the chineese to ascii characters
""" Format Specification for Strings """
# the format specification for strings are just fill, alignment and then the width of the character
# for example:
movie_crew = "[The Sword of Truth Crew]"
print("below is a formatted string")
print("{0:-^100}".format(movie_crew))
print()
# we can also use this string format spec to create a table head and also underline it
print("{0:^20}  {1:^20}".format("First Name", "Last Name"))
print("{0:-^20}  {0:-^20}".format(""))

""" Format Specification for Integers """
# format specification for integers and floats are more complex than that of strings
# first we have the fill,alignment(<,^,> or =),sign(can be +, - or space),#(force the base prefix),
# zero(zero padding between sign), width, comma, precision and type
# for example
machine_speed = 1242895.1953986
# now we want to perform some formatting with this number
print("{0:^+#030}, {0:.2f}. {0:,}".format(machine_speed))
# lets say there is a number that I will like to format to different base and also the unicode character that the number represent
num = 1600
print("Decimal:{0}, Binary:{0:#b}, Octal:{0:#o}, hex:{0:#x}, unicode char:{0:c}".format(num))


