# creating dicision making statements.
# if, if....else, if....elif, else.
# number = 10

# # if number > 0:
# #     print('Number is positive.') 

# # print('# The if statement is easy.')


# # An if statement only prints when a condition is true only but it doest'n print if the codition is false.
# # The if statement is used when you want to make a decision based on a certain condition, this checks weather the condition is true or false.
# if number > 6: # statement is true , 
#     print("The number is positive.") # This will print out.

# if number < 5: # This statement wont print out, because the codition is false.
#     print("The number is negative.")


# The if else statement.
# age = int(input("Please user, enter  your age here : "))
# # This statemet is always executed because of the else gate way.
# if age >= 18:
#     print("Your a an adult.")
# else: # The else statement opens up another option to the if statement to get another option just in case the fist condition is not True.
#     print("You a a youth.")

# weather = int(input("Enter the weather updates here."))
# if weather <= 18 :
#     print("The weather is cold.")
# elif weather <= 25:
#     print("The weather is normal. ")
# else: 
#     print("The weather is hot. ")

# # Grading students using the if elif else statement using there marks.
# grade = int(input("Plese enter your mark : "))
# if grade >= 90:
#     print("first class pass.")
# elif grade >= 85:
#     print("second class upper pass. ")
# elif grade >= 75:
#     print("sencond class lower pass")
# elif grade >= 65:
#     print("qualified")
# elif grade >= 55:
#     print("pass.")
# else:
#     print("try again.")



# LOGIN CODE.
# A getpass is an inbuilt module that you need to call befor you use it.
import getpass
# These a the saved crudentials of the user after creating an account.
correct_username = "Ainembabazi lilian"
correct_password = "secure123"
# capturing users details from the keyboard.
username = input("Enter your user name here: ")
password = getpass.getpass("Enter your password here: ") # The getpass.getpass module hides input crudentials, and these cant be seen when inputing
# This statement has the a control statement if which is a decision making statement.
# We nest the if because running the next line of code is best on the first input weather true or false.
if username == correct_username:
    if password == correct_password:
        print("login succefull ! welcome,", username)
    else:
        print("incorrect password, please try again.")
else:
    print("username not found! please check your username. ")
    



# import getpass

# username = input("Enter your username: ")
# password = getpass.getpass("Enter your password: ")  # Password input is hidden

# print(f"Welcome, {username}!")