import time
import pathlib
import datetime
import contextlib

""" 
Context managers allow us to simplify code by ensuring that certain operations are performed before and after a particular block of code is executed.  
"""
file_name = __file__
# for example here is Timer class that logs the time it takes for a code to run and then show the start time and then the end time


class Timer:
    def __enter__(self):
        self.start_time = datetime.datetime.now()
        print(f'CODE EXECUTION STARTS AT: [{self.start_time.strftime("%I:%M")}]\n')
    
    def __exit__(self, exception, exception_type, exception_tb):
        if exception is not None:
            raise exception
        
        code_execution_time = datetime.datetime.now()
        total_time_taken = code_execution_time - self.start_time
        print(f'\nCODE ENDs AT: [{code_execution_time.strftime("%I:%M")}]')
        print(f'total time taken: {total_time_taken}')


# and now we can make use of the Time context manager to track the time that it takes to run a block of code
with Timer():
    # mickicking a long time running task with the sleep function
    username = input("Please enter your username: ")
    print("starting db query..")
    time.sleep(5)
    print("Login successful")


# also, multiple contexts can be handled at the same time

annotation_path = pathlib.Path(__file__).parent / 'annotation.py'
dynamic_code_execution_path = pathlib.Path(__file__).parent / 'dynamic-code-execution.py'

with open(annotation_path) as annot , open(dynamic_code_execution_path) as dce:
    print('annotaions.py number of lines = [{}]'.format(len(annot.readlines())))
    print('dynamic_code_execution.py number of lines = [{}]'.format(len(dce.readlines())))

