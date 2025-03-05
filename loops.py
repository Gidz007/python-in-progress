# The for loop 
# The for loop is used to interate over a sequence eg. list, tuple, dictionary, set and string.

students = ["mark", "dan", "mathew", "akello"]
# The for loop interates the list in line 4.
for name in students:
    print(name)

# The for loop interating a string.
cars = "students"
for vehicles in cars:
    # The expression here will be students from top to bootom.
    print(vehicles)

# The break statement.
# We can stop the loop befor it loops through all the items.
for name in students:
     # This prints out the students list.
     # This statement tells the computer to print the student list.
    print(name)
     # ' We use a control statement to an is encoparating in the comparison operator to equalize a condition so as to break the loop before it loops through all items'
    if name == "mathew":
        # The break stops the loop emideatly the condition in line 21 is true. and name is == to mathew, that is when the loop stops.
        # This statement tells the computer to break after reaching mathem in the students list.
        break

# changing the break position.
for name in students:
    if name == "mathew":
        # Breaking before the print means you a telling the computer to break befor reaching the name mathew. 
        break
    # This statement tells the computer to print the list of students but dont print the name that was breked on because it is remove from the run sequence by the break function.
    print(name)