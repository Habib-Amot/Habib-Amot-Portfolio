# partial functions are functions whose arguments has been given beforehand, i.e. they have preloaded with some args
# this saves the stress of calling a function multiple times with the same arguments

import functools

# here is a modified print function that when called always separates its items with a newline
console = functools.partial(print, sep="\n")
console("this is the first line", "and this will end in the second line")
