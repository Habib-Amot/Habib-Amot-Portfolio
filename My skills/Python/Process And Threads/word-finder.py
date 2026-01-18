""" 
Here is the word Finder file that recieves input from it parent process
This program reads data from it's parent process and once the parent process closes the communication channel (pipe) it begins execution 
"""

import sys
import subprocess


def main():
    FILE_CHUNK_SIZE = 1000

    parent_input = sys.stdin.buffer.read()
    # and once the data has been read, it is being decoded

    decoded_data = parent_input.decode('utf8', 'ignore')  # a file object
    lines = decoded_data.splitlines() # converts object into a list
    word = lines[0]
    files = lines[1:]

    # now the word can be searched for in the files

    for file in files:
        try:
            with open(file, 'rb') as file_obj:
                while True:
                    chunk = file_obj.read(FILE_CHUNK_SIZE)
                    if not chunk:
                        break
                    if word in chunk.decode('utf8', 'ignore'):
                        print("{0:.<24}{1}".format(word, file))
                        break
                    if len(chunk) != FILE_CHUNK_SIZE:
                        break
        except EnvironmentError as err:
            print(err)


if __name__ == "__main__":
    main()
