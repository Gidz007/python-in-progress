# paradigms or arrangment / structuring.
# structured programing, the one we have been doing, writting code in a brakedown in halfs.

# oop, Object_oriented programing.
# class, objects
# proparties(atributes, characteristics, features)
# Methods, constractors, 
# principles of oop( abstraction, encapsolation, inheritance and polymorphism)
# Overloading and overriding.

# oop is a programming concept that advocates writing software based on real world objects
# eg. windows software, android software.
# objects a gotten from classes or they are classified.
# eg. Gideon, joe, james... is an object in this class of python.
# classes a identified in singular. the number of individuals are the ones that will make it plural.
# A class is a blue print of an object.
# An object is an instance of a class.
# classes difines the features, atributes, characteristics of objects.
# in python, the number of parameters is the number of parenthesis.
# The lambda function is the only recussive function in python.
# eg. a person who calls upon his or her name.
# Object oriented programming.
# A blue print means a templet of something, skeleton, layout, 
# So many objects can be used to create many objects.
# date, time, venue, name of the guests, contacts, this is an example of features of the class invitation card

# for example an invitation card that is designed at first, this is the blueprint, then the copies a made which in this casse a objects but remember these copies have different names which a features in this casse.
# "is a" is a phrase we use to identify a class of a particular object.
# An object should fulfill all the properties of a class.

students = ["Aita", "Chiru", "Edna", "Allan"]
student1 = {"Name" : "Aita", "Gender" : "Female", "School" : "Refactory Academy"}

class laptop():
    pass

class food():
    # These a features, attributes, characteristcs.
    # This is the difinaition of the objects that will come out of this class.
    name = ""
    test = ""
    calories = 0
    price = 0
    value = ""

# Creating objects out of class on line 37.
matooke = food()

matooke.name = "Matooke"
matooke.tast = "Sweet"
matooke.calories = 0
matooke.price = 25000
matooke.value = "One"

rice = food()

rice.name = "Rice"
rice.taste = "Salty"
rice.calories = "3"
rice.price = "4000"
rice.value = "1kg"

print(rice.name)