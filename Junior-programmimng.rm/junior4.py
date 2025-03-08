class Fruit:
    def __init__(gideon, name, color, size, taste, price):
        gideon.name = name
        gideon.color = color
        gideon.size = size
        gideon.taste = taste
        gideon.price = price
# Here we have two objects banana and apple; the word self is not a key word but is a word of choice for parameter of methods.
# Aguments a put in the brakets in line 10 for properties of class Fruits.
banana = Fruit("banana", "yellow", "small", "sweet", 1000)
apple = Fruit("apple", "green", "small", "sweet", 2000)


# This represents the inheritance bit. picking treats of a class
class Animal:
    # This is a constructor in line 16.
    # self is not a parameter but used to identify or link the properties of a class.
    # This statement is a constructor method.
    # We use init to assign value to properties of an object
    # This statement is executed when an object is being initiated.
    def __init__(self, name, bread, color, size, kgs):
        # This line contains individual values of the objects
        self.animalname = name
        self.animalbread = bread
        self.animalcolor = color
        self.animalsize = size
        self.animalkgs = kgs
        # This method simply outputs the attrubutes in a redable way for the user, but nothing much special about it.
    def details(self):
        print(f"animalname: {self.animalname}\n animalbread: {self.animalbread}\n animalcolor: {self.animalcolor}\n animalsize: {self.animalsize}")
# Here we a simply telling the dog to take on the properties of class animal.
# Here we the class dog is inheriting properties and mehtods for the class animal.
class Dog(Animal):
    # A method will always have the word self in the brackets.
    def sond(self):
        print("sound: dog wooofs")

class Bull_dog(Dog):
    # The class Bull dog has two methods which is sound and the inherited methos which is details from the Animal class.
    def greets(self):
        print("dog sooofs")

dog = Dog("Max", "German shepherd", "Brown", "Big", 10)
bull = Bull_dog("Max", "German shepherd", "Brown", "Big", 10)
dog.details()
dog.sond()
bull.greets()


# Assigment; Use at list five classes to demonstrate inheritance in python use a construtor with at list 7 parameters and there coresponding properties, the last/ fifth class should be taking on five methods.