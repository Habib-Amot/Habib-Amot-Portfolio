""" 
Say you want to rename every file in some folder and also every file in every subfolder of that folder. That is, you want to walk through the directory tree, touching each file as you go.
"""

# the  os.walk method allows for traversing of any folder. it generates folder name, the directory in the folder and also the filenames
# for example, traversing the current user folder

import os
from pathlib import Path

user_dir = Path.home()

for current_dir, folder, files in os.walk(user_dir, topdown=True):
    for file in files:
        print(Path(current_dir, file).name)
