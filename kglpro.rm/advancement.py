
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
if username == correct_username: # comparred with the user's input to see if they correct.
    # A function is nested when a certain condition needs to be met.
    if password == correct_password:
        print("login succefull ! welcome,", username)
    else:
        print("incorrect password, please try again.")
else:
    print("username not found! please check your username. ")
   