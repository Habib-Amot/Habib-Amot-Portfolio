""" 
If a program runs very slowly or consumes far more memory than we expect, the problem is most often due to our choice of algorithms or data structures, or due to our doing an inefficient implementation. In either case, the best thing to do is to profile our program to see which function or method is causing the program to slow down.
Python comes with two builtin modules that can be used to profile our code: 
The first one is the timeit module and the second is the cProile module both of which will be used in this lesson

Before delving into profiling in python, there are some optimization practice to consider before starting
1. always use tuples over list when saving read only data
2. use generators over for loops
3. when accessing a method or function (in case of module) using attribute access quite often, it is best to create a local variable to hold
that function and call the variable instead
4. use python data structures rather than creating a new one
5. rather than concatenating small strings to form a larger one, always aggregate the strings and in list and then join them together

After mentioning all these, now lets dive into profiling

"""

import timeit
import cProfile


print("=" * 50)
print("Profiling using Timeit module".title())
print("=" * 50)
print()


# here are two functions that performs the same operation but uses different algorithms and now we want to check how long each one takes
def add_numbers_1(*args):
    try:
        result = sum(args)
        return result
    except ValueError:
        print("error caught and handled...")


def add_numbers_2(*args):
    try:
        result = 0
        for num in args:
            result += num
        return result
    except ValueError as err:
        print(err)

# profiling each method
numbers = list(range(1, 1000))
if __name__ == "__main__":
    for function in ['add_numbers_1', 'add_numbers_2']:
        repeat = 1000
        profile = timeit.Timer('{0}(*numbers)'.format(function), 'from __main__ import {0}, numbers'.format(function))
        time_taken = profile.timeit(repeat) / repeat
        print("{0}() takes {1:.8f}s".format(function, time_taken, numbers))

""" 
Here is the result I got after running the above code
add_numbers_1() takes 0.00001163s
add_numbers_2() takes 0.00005727s

and from this, it is obvious that the first algorithm is faster than the second 
"""

print("\n", "=" * 50, sep="")
print("Profiling using cProfile module".title())
print("=" * 50)
print()

for function in ('add_numbers_1', 'add_numbers_2'):
    cProfile.run("for i in range(1000): {function}(*numbers)".format(**locals()))
