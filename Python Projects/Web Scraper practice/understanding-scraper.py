# this is a practice to understand how scrapers work in python 
# The library that is being used is BeautifulSoup which is a python ibrary that is used to parse and extract data from web Documnets which # can be in the form of HTML or XML

""" 
Author: HABIB AMOT
Email: habibgemini1@gmail.com
 """

from bs4 import BeautifulSoup

html_doc="""
 <html><head><title>TheDormouse'sstory</title></head>
 <body>
 <p class="title"><b>TheDormouse's story</b></p>
 <p class="story">Once upon a time there were three little sisters and their names were
 <a href="#"> <h1> this is the main site home </h1> </a>
 <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
 <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
 <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
 andtheylivedatthebottomofawell.</p>
 <p class="story"> This is a short story about a Man that knows how to make money by using python scripts. </p>

 """
# passing the html doc into Beautiful soup object
# This allows for getting and indexing of the HTML elements using tags and attributes names
parsed_data = BeautifulSoup(html_doc)

# showing the prettify version of the document
print(parsed_data.prettify())

# now all the html tags are now present as attribute os the parsed_data object
print(parsed_data.a) # this will print out the first anchor tag that is in the document

# to get all the element that has a particular tag name, we make use of the find_all method
print(parsed_data.find_all('a'))

# getting the html title of the page
print(parsed_data.title)

# getting the tag name of an element
print(parsed_data.title.name)

# getting the content inside an element
print(parsed_data.a.string) # the string property will get the value of an element if the element has just one child

# getting the parent of an element
print(parsed_data.title.parent)


# one common task is to get all the link that is inside a page, this can be done or achieved by using .find_all method
for link in parsed_data.find_all('a'):
    print(link.get('href'))

# also to extract all the text inside a page, we can make use of the get_text method
print(parsed_data.get_text())