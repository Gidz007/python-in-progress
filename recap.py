# A function is a defined block of code.
# A global variable can be accessed in the function with out the return function.
# we call upon a function to be executed. 
# If you invest your time in learning my progrmming you will never sleep hungry.
# All functions a built on a function notation.
# if you master loops, conditions and functions.
# in line 6 you a simply going through variables, syntax and structure.

# A function is block of code that runs when called upon.
# Data passed in a fuction can be known as parameters.

# defining a function students.
# def students():
#     print("Hello students")

# students()

# # Aguments can be passed in parenthesis of a function.
# def students(self):
#     print(self +  "football club")

# students("Arsenal")
# students("Manchester")
# students("Real madrid") 


#
# A class is a blueprint for creating objects. It can have different types of functions:
# Instance Methods (functions that use self)
# Class Methods (functions that use cls)
# Static Methods (functions that don’t use self or cls)
# A static function inside a class is just a function that belongs to the class but does not depend on an instance. 
# An instance is an object created form a class, which is the blue print of an object.



"""Assigment; Use at list five classes to demonstrate inheritance in python use a construtor with at list 7 parameters and 
there coresponding properties, the last/ fifth class should be taking on five methods.
"""
class Phones:
    '''The constructor tells the computer the operations to do when creating an object and on this statement 
    we a having parameters and a refrence self in perameters.
    '''
    # We use self to refer to the properties of an objects.
    def __init__(self, name, type, size, color, weight, ram, storage ):
        # Here we assign and store values in the object parameters.
        self.name = name
        self.type = type
        self.size = size
        self.color = color
        self.weight = weight
        self.ram = ram 
        self.storage = storage
        # The details method displays the outlook of the expression of the instances created.
    def details(self):
        return f"name : {self.name}\n type : {self.type}\n size : {self.size}\n color : {self.color}\n weight : {self.weight}\n ram : {self.ram}\n storage : {self.storage}"

# The statements below show inheritance of properties from the parent class to the children classes.
# The fifth class takes on five methods inheritaing them from the other four child classes.
        
class Tecno(Phones):
    # On this statement we define a method which is thems.
    def themes(self):
        return"Tecno : Has the best themes."

class Iphone(Phones):
    # The method statement here shows a particular property a child has of its own leaving alon the inheritade property.
    # This is also inheriting properties from the parent class only.
    def itunes(self):
        return"Iphone : Itunes make backing up easy."

class Samsung(Phones):
    """The statement here has a method showing its own property it posese on its own 
    which is display, samsung has a good diaplay of things, mostly the samsung edge.
    """ 
    def display(self):
        return"Samsung : The latest folding screens a mind blowing."

class Black_berry(Phones):
    """The statement here shows a property a child class holds on its own, 
    which is keyboard, this is a particular aparence of the keyboards made by Black_berry as a company.
    """
    def keyboard(self):
        return"Black berry : The keyboard computer is one in a million."

class Oppo(Tecno, Iphone, Samsung, Black_berry):
    # This class inherits all methods of the rest of the classes and calling them under one class.
    """This class also has a property of its own that it poseses and this is on how it
      holds its security, it is hard to unlock it if you dont have its passkey.
    """
    def security(self):
        return "Oppo : The Oppo Japan made has security that has never been seen, no passkey - no entry."
    

# This statement shows the creation of an instance based on the Oppo class.
final_obj = Oppo("Oppo", "Smart phone", "4.5 inches", "light pink", "150 gms", "8 Gb", "64 Gb")
# This statement shows the creation of an instance based on the Tecno class.
tec = Tecno("Tecno", "Smart phone", "6 inches", "Black", "100 gms", "6 Gb", "128 Gb")
# This statement shows the creation of an instance based on the Iphone class.
ip = Iphone("Iphone", "Smart phone", "5 inches", "grey", "150 gm", "4 Gb", "64 Gb")
# This statement shows the creation of an instance based on the Samsung class.
sam = Samsung("Samsung", "Smart phone", "6 inches", "Black", "150 gms", "8 Gb", "128 Gb")
# This statement shows the creation of an instance based on the Black_berry class.
black = Black_berry("Black_berry", "Smart phone", "5 inches", "Brown", "200 gms", "4 Gb", "64 Gb")

# This statement is calling the details method on the tec object.
print(tec.details())
# This statement is calling the themes method in the Tecno class.
print(tec.themes())
print("-")
# This statement is calling the details method on the ip object.
print(ip.details())
# This statement is calling the itunes method in the iphone class.
print(ip.itunes())
print("-")
print(sam.details())
print(sam.display())
print("-")
print(black.details())
print(black.keyboard())
print("-")
print(final_obj.details())
print(final_obj.security())
