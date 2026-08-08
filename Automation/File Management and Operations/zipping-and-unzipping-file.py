# zipping and unzipping operations are common in programming
# which is why it is important to know how to dip.and unzip files in python

import zipfile


# lets say i created 4 files, write some contents into them and then want to zip them together

# first i will create the files
for i in range(4):
    with open(f"file{i + 1}.txt", "w") as file:
        file.write(f"This file number {i+1}")
        
    with zipfile.ZipFile(f"files.zip", "a") as zfile:
        zfile.write(f"file{i+1}.txt")
        
# and the zipped folder can be unzipped
with zipfile.ZipFile("file.zip") as zfile:
    zfile.extract_all()
