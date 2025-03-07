# inheritance is two individual classes sharing the same properties.
# inheritance is the ability of a sub/child/derived-class to take on one or more attributes of a super/parent/base class.

class Animal():
    name = ""
    color = ""
    weight = 50
    owner = ""
# when variables a put in class they become properties or features.
# A function is a methods when used in a class.
# The word self means each individual object that will take on this method.
# In this case the dog took on the method.
    def sound(self):
        print("I bark")

# statement you write in a method a refered to as behaviours eg. we have a behaviour in line 12 found in a method called sound.
# What is an object?
# a class is memory space that is experdable
# 

# This is an object dog.
dog = Animal()
dog.sound ()