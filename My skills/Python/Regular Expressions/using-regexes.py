# python re module provides two ways of creating regular expressions, we either make use of the functions that is provided by the re 
# module or make use of the compile method
# Taking the first approach is suitable for one off use while the second (using compile) is suitable for multiple times usage
import re


# Example 1: Extracting hexadecimal color code
print("=" * 60)
print("Example 1: Extracting Hexadecimal Color Code")
print("=" * 60)

# given the text
sentence = r"color red in hexadecimal format is #ff0000"
print(sentence)

# to get the hexadecimal color from the sentence, the regex can be used

# # this returns a match object and there are different attributes and methods that can be called on it
color = re.search(r'\s+(?P<hex_value>#[\dA-Fa-f]{6})(?!\w)', sentence)  
print(color.span(), color.start(), color.end(), color.group(0), color.groupdict())

# while the search function only searches and returns the first match that it encounters, the finditer and findall function and methods 
# will find and store all match

# Example 2: Finding hashtag comments using findall and finditer
print("\n" + "=" * 60)
print("Example 2: Finding Hashtag Comments")
print("=" * 60)

# given the string
hashtag_comments = '''my favorite text editor is #vscode
my favorite programming language is #python, #js, #typescript
#automationexpert, #webdeveloper, #backenddeveloper
'''
# to get all the comments from this string, the regex can be used
comment_regex = re.compile(r'(?<!\w)#\w+')
# and now, the regex can be used in any text to capture the hashtags that were used
comments = comment_regex.findall(hashtag_comments)

print(comments)

# and if each match is to be treated as a match object, the finditer method can be used instead
comments_obj = comment_regex.finditer(hashtag_comments)
for comment in comments_obj:
    print(comment.group(0), comment.span())  # getting each object and their positions


# Example 3: Extracting image filenames from HTML
print("\n" + "=" * 60)
print("Example 3: Extracting Image Filenames from HTML")
print("=" * 60)

# another very useful application of regex is its application in extracting file names from a webpage
# these filenamaes can be either image filenames or any other links on the webpage
# I am going to be extracting image tag in this case

image_regex = re.compile(r'''<img\s+[^/>]*?src=(?:(?P<start_quote>["'])(?P<file_name>[^\1]+?)(?P=start_quote)|(?P<filename>[^"' ]+?))[^>]*?>''', re.IGNORECASE)

# reading an HTML file and extracting the images there
with open(r'C:\Users\user\Documents\Amot The Dev\My Portfolio\My skills\Responsive UI Designs-CSS\Online Computer Store\index.html') as file:
    content = file.read()
    image_content = image_regex.finditer(content)

for match in image_content:
    print(match.group('filename') or match.group('file_name'))


# Example 4: substituting names in a text
print("\n" + "=" * 60)
print("Example 4: Substituting Names in a Text")
print("=" * 60)
# regex can also be used to substitute names in a text
# given that names are in the format, firstname, middlename1 middlename2 ... , lastname
# we can create a regex to capture these names and swap them to lastname, firstname middlenames format
name_swap = re.compile(r'(\w+(?:\w+[\s,]+)*)(\w+)')
my_name = "Habib, Amot, Oluwaseyi, Gemini, Yakubu"

swapped_name = name_swap.sub(r"\2 \1", my_name)
print(swapped_name)
