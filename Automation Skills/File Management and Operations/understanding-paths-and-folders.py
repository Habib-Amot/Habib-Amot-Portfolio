""" in this lesson, I will be working with creating of folders and paths using the pathlib module in python """

import os
import shutil
import signal
import pathlib
from pathlib import Path

print("{0:=^60}".format("[+]Creating of paths..."))


new_path = pathlib.Path( 'home', 'contents', 'businesss-files')
print(new_path)  # prints home\contents\businesss-files

# and now, the path can be added to using the / operator
updated_business_path = new_path / 'private-file'
print(updated_business_path)  # home\contents\businesss-files\private-file

# and now this folders can be created on the system,
# NB: this paths are relative to the current working directory if the path is a relative path 
Path.mkdir(new_path, parents=True, exist_ok=True)  # creates the paths even if it exists

print()
print("{0:=^60}".format("[+]Getting the part of a file..."))

# to get the path of the current running file, the __file__ variable can be used for this 
print("current path of this file is", __file__)

# to get the various parth of this Path, it first needs to be converted to a path object
current_file_path = Path(__file__)
print("\nparent of the current file is ", current_file_path.parent)

# and the parents of the file can also be gotten
print("\nparents of the current file is", [str(parent) for parent in current_file_path.parents])
print()

print("\ncurrent file is", current_file_path.name)
print("\ncurrent file name is", current_file_path.stem)
print("\ncurrent file extension is", current_file_path.suffix)

print("{0:=^60}".format("[+]Getting the size of a file..."))
print()
print("the size of this file is {0:.2f} KB".format(os.path.getsize(current_file_path) / 1024))

print("\n{0:=^90}".format("[+]Listing the content of a directory using glob patterns and os.listdir method ..."))
print()
print("Getting every python file in this portfolio folder")
parent_dir = Path(r"C:\Users\user\Documents\Amot The Dev\My Portfolio\My Skills")

all_python_file = list(parent_dir.glob('**/*.py'))

print()
print("{0:=^60}".format("[+]Checking File Validity..."))

# I am going to create a file now
new_file = Path("home.txt")
Path.touch(new_file)

# checking if the file now exists in the directory
if Path.exists(new_file):
    print("home.txt created successfully...")
else:
    print("unable to create file")

# and now, I can check if the created path is a file or not
print(f"{str(new_file)} is {'' if Path.is_file(new_file) else 'not'} a file")

# and the same thing can also be achieved for confirming directories
print(f"{str(current_file_path)} is {'' if current_file_path.parent.is_dir() else 'not'}a folder")

print()
print("{0:=^60}".format("[+]Reading and writing to file..."))
# reading and writing file content can be done in two ways, either via the open function, or via pathlib object

# writing this file content to the home.txt file and also renaming it
current_file_path_content = current_file_path.read_text()
new_file.write_text(current_file_path_content)

try:
    new_file = new_file.rename(new_file.stem + current_file_path.suffix)
except FileExistsError:
    pass

# and now the entire file content can be written to the terminal
# print(new_file.read_text())  

print()
print("{0:=^60}".format("[+]Navigating directories..."))

print('Current working directory is', Path.cwd())
# say that i created a folder in this directory and will like to then move it into the user home dir
new_folder =  Path('Test-Tools')
Path.mkdir(new_folder, exist_ok=True)

# and now I want to move the newly created folder to the user home directory
if os.access(str(Path.home()), os.W_OK):
    try:
        shutil.move(str(new_folder), str(Path.home()))
    except shutil.Error:
        pass


# navigating to another dir
home_directory = Path.home()
os.chdir(str(home_directory))

print("switched to directory: {}".format(Path.cwd()))

print('getting the content of the directory')
home_dir_content = os.listdir()

# or in a more better way, this can be all converted to path objects using the Path.glob method
print(Path.cwd().glob('*'))

# now, checking if the newly created folder exists in this dir
if Path.exists(new_folder):
    print("[+]Folder created successfully..")
    print("[*]Renaming the folder...")
    new_folder.rename('Business Suite')
else:
    print("[-]Unable to create folder")
