class Animal():
    type = ""
    name = ""
    color = "" 

# This statement is an object, and there properties a defined in the class.
lion = Animal()

lion.type = "cats"
lion.name = "lion"
lion.color = "brown"
# The print fuction will print this because the condition works as long as one feature is met, then the rest will be printed.
lion.look = "eye"
lion.teeth = "syber tooth"

chicken = Animal()

chicken.type = "poultry"
chicken.name = "chicken"

print(f"lion: {lion.name} , {lion.color} , {lion.type} ,{lion.look} , {lion.teeth}")


# The dot operator is used to access characteristics of an object.
# Class names a always in singilar and not prural.


class car():
    type = ""
    name = ""
    # colour = ""
    # number_plate = ""
    # milage = ""

Hilux = car()
# The dot operator is used to access characteristics of an object.
Hilux.type = "2025 latest release"
Hilux.name = "Hilux"
Hilux.colour = "Black"
Hilux.number = "UAN 9651"
Hilux.milage = 0

Benz = car()

Benz.type = "2023 modal"
Benz.name = "Benz"
Benz. colour = "grey"
Benz.number = "UAY 1967"
Benz.milage = 0

Bmw = car()

Bmw.type = "2025 modal"
Bmw.name = "Bmw Red gohst"
Bmw.colour = "orange"
Bmw. number = "UBG 1760"
Bmw.milage = "80 km"

# For one to see the characteristics of a Bmw you use the .name function to print them out.
print(f"Hilux: {Hilux.type}, {Hilux.name}, {Hilux.colour}, {Hilux.number}, {Hilux.milage}")
print(f"Benz: {Benz.type}, {Benz.name}, {Benz.colour}, {Benz.number}, {Benz.milage}")
print(f"Bmw: {Bmw.type}, {Bmw.name}, {Bmw.colour}, {Bmw. number}, {Bmw.milage}")


# PRINCIPLES OF OBJECT ORIENTED PROGRAMMING.
# Abstract : This means forcusing on something and ignoring its details eg a tree but not looking were it is and its type.
# Encapsulation : This is the ability of objects to put control access over its details eg.the details of the tree, you cant konw how it does osmosis and how it gets food but its is ther, that is public, private, protected.
# Polymorphism : This is the ability of an object to take on more than one forms.


# with object oriented programmming code is reusable, code is relatable to daily life.