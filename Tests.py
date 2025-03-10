# An inheritance of a class with six sub classes with the last class taking on all methods of the rest of the classes and five inheritances.

# We define a class Boxing.
class Boxing:
    # we define a constructer which is called upon on creating an object.
    # We define a constructor with parameters in the parenthesis.
    # The word self is just a word that was adopted in python to refer to properties of an object and its not a keyword.
    def __init__(self, organisation, work, fundings, contracts, sponserships):
        self.organisation = organisation
        self.work = work
        self.fundings = fundings
        self.contracts = contracts
        self.sponserships = sponserships
    # We define a details function which will be called on to the objects that a to be created with in the class.
    def details(self):
        return f"organisation : {self.organisation}\n work : {self.work}\n fundings : {self.fundings}\n contracts : {self.contracts}\n sponserships : { self.sponserships}"

"""We now create the sub classes that will inherit properties from the parent class 
and add properties to it these will be in existance with properties inheritade from the parent class.
"""
class IBF(Boxing):
    # We now create a property in the IBA class by defining a function.
    def jab(self):
        num = "International Boxing Fedaration"
        num1 = "This organisation handels boxing mainly in the United Kindom."
        return num, num1

# We go on to create another class which is the WBO and it also inherits from the parent class.       
class WBO(Boxing):
    # We define a function to give ower class properties.
    def upper_cut(self):
        num2 = "World Boxing Organisation"
        num3 = "This works generally in the whole world."
        return num2, num3
    
# Here we create another class which is IBA.
class IBA(Boxing):
    # We difine a function for it to inorder to give it properties also.
    def hook(self):
        num4 = "International Boxing Association"
        num5 = "This organisation is the top dog."
        return num4, num5

# We create another class which is the WBA and inherites properties from the parent class    
class WBA(Boxing):
    # We define a function in the WBA class.
    def straight_right(self):
        num6 = "World Boxing Association"
        num7 = "This organisation handels boxing mainly in Africa."
        return num6, num7
    
# We create another class which is WBC and also inherits from the parent class Boxing.
class WBC(Boxing):
    # We define for it a function to give it personal properties.
    def left_hook(self):
        num8 = "World Boxing Championship"
        num9 = "This organisation deals with titles that a meant to represent a champion."
        return num8, num9
    
# We create another class which is IBC, this will inherite all the methods of all the sub classes created inclusive of the details method.
class IBC(IBF, WBO, IBA, WBA, WBC):
    # We define a function for it to.
    def right_uppercut(self):
        train = "International Boxing Championship"
        train2 = "This handels championship belts that a to be compited for in each fight in a particular country."
        return train, train2

# We now create instances for our classes.
final_obj = IBC("International Boxing Championship", "Boxing related", "Has internal and external funders", "Contracts a given to its athletes", "Sponsers a got for the athletes but the organisation dosen't do sponserships")
gloves = IBF("International Boxing Federation", "Boxing related", "Getts it's funds from Emirated", "Contracts a given to every athlete", "The organisation does fundings to all sports men and women")
mouth_gaurd = WBO("World Boxing Organisation", "Boxing and promotes wrestling", "It has its owner who funds it", "contracts a given to athletes that perform under it only", "The organisation does sponsor its atheles")
hand_wraps = IBA("International Boxing Association", "Boxing and also promotes technology development", "Gettings its main funds from USAID", "Contracts a give to athletes that need to be promoted only", "Sponserships a given to athelets that pass there drug tests")
paching_bag = WBA("World Boxing Association", "Boxing related", "Has internal and external funders", "Contracts a given to athletes that perform under the organisation's name", "sponserships a given the athletes that perform under the organisation only")
dumbell = WBC("World Boxing Championship", "Boxing related only", "Funds a got from USAID", "Contracts a given to athelets that pass the drug and qualification test", "The organisation does sponser it's athletes")

# This statement calls the details function on to the class methods. 
print(gloves.details())
print(gloves.jab())
print("-")
print(mouth_gaurd.details())
print(mouth_gaurd.upper_cut())
print("-")
print(hand_wraps.details())
print(hand_wraps.hook())
print("-")
print(paching_bag.details())
print(paching_bag.straight_right())
print("-")
print(dumbell.details())
print(dumbell.left_hook())
print("-")
print(final_obj.details())
print(final_obj.right_uppercut())