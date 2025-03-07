# Static functions that have had coded values.
# Functions a self contained and variables that a in it cant be accessed. 
def add():
    varl = 10
    var2 = 20
# The key word return helps us to access a value inside a function.
# When we want expose a value we use the return function.
    return varl + var2

# This prints out a value out of a function.
print(add())
my_num = add()
print(my_num)




# This line is exposing the value of the return key.
def sub():
    var1 = 10
    var2 = 20
    return var2 - var1

# The reason we a calling a funtion in a print comand is because we just want to see the value on the screen but not able to access it.
# This is because its the syntax of how we access a value in a functin using the return key.
# On this line we a printing what the function sub is exposing.
print(sub())



def both():
    return sub() + add()

print(both())




def add1():
    var3 = int(input('please enter your number here: '))
    var4 = int(input('please enter your number here: '))
    return var3 + var4

def sub1():
    var3 = int(input('please enter your number here: '))
    var4 = int(input('please enter your number here: '))
    return var3 + var4

def both1():
    return add1() + sub1()

print(both1())

sub()