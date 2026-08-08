import math

""" 
There are some occasions when it is easier to write a piece of code that generates the code we need than to write the needed code directly. And in some contexts it is useful to let users enter code (e.g., functions in a spreadsheet),and to let Python execute the entered code for us rather than to write a parser and handle it ourselves—although executing arbitrary code like this is a potential security risk, of course. 
"""
# The easiest way to execute an expression is to use the built-in eval() function
# python exec function can only handle one expression and cannot handle multi line expressions for example
print("{0:=^40}".format('[EVAL AND EXEC]'))
print("Using Eval:")
five_time_5 = eval('5 * 5')
print("eval('5 * 5')=", five_time_5)
#  while the above code is a simple one, we can perform some more serious operations with eval
user_operation = input("enter a math operation:")
result = eval(user_operation)  # although this operation is dangerous as users might enter malicious data
print("Evaluating {0}=".format(user_operation) ,result)

# what if we want to create functions or something that is more serious than a simple expression
# here is where the exec function comes in
# for example, we can create a function

print()
print('using exec:')
area_of_circle = '''
def area_of_sphere(radius):
    result = math.pi * math.pow(radius, 2)
    return result
                      
'''
exec(area_of_circle)
# when we call exec like we did above, we have no way to access the object that is being created by exec and also there is no way for exec to 
# access any object in the global or local scope
# to solve this problem, a context object is passed to exec which it uses for storing and accessing objects
# below is a solution to how this is made possible
context = {
    'math': math
}
exec(area_of_circle, context)  # now the math module is accessible to exec, and now there is access to the function created by exec
area_of_circle = context['area_of_sphere']
print(area_of_circle(10))
