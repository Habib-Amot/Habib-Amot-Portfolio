""" 
This lesson is about how to run processes in such a way that we can spawn up a new process, hand over tasks to it, communicate with it and even 
kill the process
In the field of computer science, a process is a program in memory with its own stack, heaps data and generally its resources. what this means is 
that each process run parallel to one another with their own python interpreter and without interrupting one another's data.
For this lesson, I will be making use of python subprocess module and in the part 2, I will be making use of python multiprocessing module which
provides a similar API to python threading
"""

import os
import sys
import argparse
import subprocess

# below is a program that searches for a particular word in a file, mentions where the word was found and also output it
# it uses multi processing to achieve this
def main():
    child_program = os.path.join(os.path.dirname(__file__), "word-finder.py")
    child_pipes = []

    # next we get the names of the file or folder to search the word from
    command_line_opt = get_opt()
    search_locations = command_line_opt.locations

    if not search_locations:
        print("please enter file or folder to search from")
        return
    
    files: list = get_files(search_locations, command_line_opt.recurse)
    files_per_process: int = len(files) // command_line_opt.process_count  # getting the number of process to handle the files
    start, end = 0, files_per_process + len(files) % command_line_opt.process_count

    while start < len(files):
        file_assigned_to_process = files[start:end]
        commands = [sys.executable, child_program]
        pipe = subprocess.Popen(commands, stdin=subprocess.PIPE)
        child_pipes.append(pipe)  # saving the communication mechanism for this process

        # sending data to the process
        # first is to send the word or phrase to be searched to the child program
        pipe.stdin.write(command_line_opt.search_word.encode('utf8') + b'\n')

        # writing each individual file name to the child program
        for file in file_assigned_to_process:
            pipe.stdin.write(file.encode('utf8') + b'\n')
        
        pipe.stdin.close()
        start, end = end, end + files_per_process  # incrementing the file access

        while child_pipes:
            pipe = child_pipes.pop()
            pipe.wait()



def get_files(locations: list, recurse_dir: bool=False) -> list: 
    assert isinstance(locations, list), "please enter a collection of locations to search"
    files = []

    for location in locations:
        if os.path.isfile(location):
            files.append(location)

        if os.path.isdir(location):
            if not recurse_dir:
                files_in_location = [location + '\\'+ file for file in os.listdir(location) if os.path.isfile(os.path.join(location, file))]
                files.extend(files_in_location)
                continue
            for dir, subdir, dir_files in os.walk(location):
                for file in dir_files:
                    files.append(os.path.join(dir, file))
            
        else:
            continue
    return files if files else []


def get_opt():
    parser = argparse.ArgumentParser('Word-finder.py')
    parser.add_argument('-w','--word', type=str, required=True, help="the word or phrase to search for in files", dest='search_word')
    parser.add_argument('-r', '--recurse', help="either to recurse directories or not", default=False, action='store_true')
    parser.add_argument('-p', '--process', help="the number of process to create for the task", default=7, dest='process_count')
    parser.add_argument('-t', '--threads', help="the number of threads to create for the task", default=7, type=int)
    parser.add_argument('locations', help='the folder or files(s) to search word from', nargs='+')
    args = parser.parse_args()
    return args


main()
