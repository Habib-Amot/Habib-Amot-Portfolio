# multiple inheritance is the practice whereby a single subclass or child class inherits from multiple base classes or
# parent class. In this case, the child class will have all the parent class or classes properties and method accessible

import datetime

# here is an example which shows the use such classes


class ProcessCsv:
    def __init__(self, filename: str):
        self.filename = filename
        self.__data = {}

    def load_csv(self, filename):
        print("loading from csv file....", self.filename if not filename else filename)

    def dump_csv(self, filename):
        print("Dumping data into csv file....", self.filename if not filename else filename)


# and here is a class that processes Excel file
class ProcessExcel:
    def __init__(self, filename):
        self.filename = filename
        self.__data = {}

    def load_xlsx(self, filename):
        print("loading excel file", self.filename if not filename else filename)

    def dump_xlsx(self, filename):
        print(f"Writing content into {self.filename if not filename else filename}")


# now an Automation Bot can be created which will have the ability to process both excel and csv files
class FileManager(ProcessCsv, ProcessExcel):
    def __init__(self, csv_file, excel_file):
        # It is ambiguous to let python determine which base class we are referring to by calling super, so it is nice
        # to call the base class explicitly by name
        ProcessCsv.__init__(self, csv_file)
        ProcessExcel.__init__(self, excel_file)
        self.__data = {}

    # this gets data from Google form and then save it in the object data property
    def get_data_from_form_to_csv(self, url):
        print("fetching data from url..", url)
        self.__data = {"name": "Arial the Dev", "date-joined": datetime.date(2025, 10, 5)}
        self.dump_csv('user-data.csv')  # this saves the data inside the provided csv file

    def get_data_from_form(self, url):
        print("fetching data from url", url)
        self.__data = {"name": "Arial the Dev", "date-joined": datetime.date(2025, 10, 5)}


# now the FileManager class can be used alongside the provided interfaces of the classes it inherits from
bot = FileManager(csv_file="data.csv", excel_file="data.xlsx")
bot.get_data_from_form_to_csv("https://forms.google.com/amot")  # getting data and dumping the data to csv
# and I can explicitly just get the data alone without saving it in a file yet

bot.get_data_from_form('https://forms.google.com')
# saving the data to csv
bot.dump_xlsx("data.xlsx")
