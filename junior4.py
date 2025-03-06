# we dont put a bracket when we adeclaring a class in encapsulation.
# The class name has to be in capital letter.
class Animal: 
    # we don't quote parameters.
    # dynamic functions will have values in the calling of that function, line 6.
    # This function is function is in this called a dynamic method.
    # This function could be called a constructor function, and usef to initialise/ giving value of an object of a class.
    def __init__(self,name, size, colour): # name, size, colour. these a parameters, the word self is used to identify the properties of a class.
        self.animalname = name
        self.animalsize = size
        self.animalcolour = colour
# self.animalname will come as the properties of the class.
# name, size, colour will come as aguments.

# Here the word cat comes as the agument to the property animalname.
cat = Animal("cat", "small", "black")
dog = Animal("dog", "medium", "blue")
        