# We have two types of functions in python, 
# Static functions. # This has hardcoded values meaning they wont change automatically. 
# Dynamic functions. # These have parameters
# The number of values you have out into the parenthesis of the paremiter of the dynamic function.
# loops help you to filter because you a running code basing on a certain condition.
# structured programing or funtional programming
# The number of values in the parenthesis is called parameter list.
# urguments must fulfill the parameter list.
# Both statics and dynamic functions can return a value.
def add():
    num1, num2, = 20, 30
    print(num1 + num2)
    # a return statement marks the end of execution in a function. ( This is a sytax.)
    return num1 + num2
    # This function wont print out because of the indentation.
    print(num1) 

add()
print(add())
num3 = add()
print(num3)



