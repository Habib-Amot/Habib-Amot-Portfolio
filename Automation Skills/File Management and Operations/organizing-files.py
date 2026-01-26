# in this lesson, I will be learning about how to copy, move and rename files and folders using python shutil module

import os
import time
import shutil
import pathlib
import send2trash
from pathlib import Path

# first I am going to create a file
new_file = pathlib.Path('leads.csv')
try:
    pathlib.Path.touch(new_file)
except FileExistsError:
    pass

# then, I am going to rename the file 
time.sleep(3)

if os.path.exists('business-leads.csv'):
    new_file = Path('business-leads.csv')
else:
    new_file = new_file.rename('business-leads.csv')

# copy the newly created file to a folder
business_dir = Path('Business Leads')
business_dir.mkdir(exist_ok=True)
lead_path = Path(shutil.copy(new_file, 'Business leads'))

# and finally, the folder will be moved to user home dir
time.sleep(3)
if Path.exists(Path.home()/lead_path.name):
    pass
else:
    shutil.move(str(business_dir/lead_path.name), str(Path.home()))

# permanently delete the file 
os.remove(Path.home()/lead_path.name)

# but sometimes, we often to dont want to delete a file permanently and want to first the file to trash
# this can be achieved by using the send2trash module
send2trash.send2trash(new_file)  # temporarily deleting the business-leads.csv file

# also sending the Business Leads folder to trash
send2trash.send2trash(business_dir)

