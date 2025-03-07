# # The for loop 
# # The for loop is used to interate over a sequence eg. list, tuple, dictionary, set and string.

# students = ["mark", "dan", "mathew", "akello"]
# # The for loop interates the list in line 4.
# for name in students:
#     print(name)

# # The for loop interating a string.
# cars = "students"
# for vehicles in cars:
#     # The expression here will be students from top to bootom.
#     print(vehicles)

# # The break statement.
# # We can stop the loop befor it loops through all the items.
# for name in students:
#      # This prints out the students list.
#      # This statement tells the computer to print the student list.
#     print(name)
#      # 'We use a control statement to an is encoparating in the comparison operator to equalize a condition so as to break the loop before it loops through all items'
#     if name == "mathew":
#         # The break stops the loop emideatly the condition in line 21 is true. and name is == to mathew, that is when the loop stops.
#         # This statement tells the computer to break after reaching mathew in the students list.
#         break

# # changing the break position.
# for name in students:
#     if name == "mathew":
#         # Breaking before the print means you a telling the computer to break befor reaching the name mathew. 
#         break
#     # This statement tells the computer to print the list of students but dont print the name that was breked on because it is remove from the run sequence by the break function.
#     print(name)

# boxing = ["gloves", "mouth_piece", "bandages", "canvas_shoes"]
# # The continue statement.
# for athlete in boxing:
#     # if athlete == "mouth_piece":
#     #     continue
#     # # print(athlete)

#     if athlete in boxing:
#         if athlete == "canvas_shoes":
#             continue
#         print(athlete)

# # Break, continue, pass, a control statements in a loop.
# # Break means stop there, continue means continue with what you a doing, pass means by pass this dont mind it.
# # loops a not name.


# # The range function.
# # used to loop through a set of code a specific number of times.
# for x in range(6):
#     print(x)

# for u in range(10):
#     print(u)

# # You can also put a perameter, the start, by adding a parameter.
# # range(2, 7), the print here will start from 2 and run but will exculd  7, so it will be 2 - 6 an the expression.
# for y in range(2, 10):
#     print(y)

# # The default increament in a loop is 1 but you can madify it by adding a third parameter.
# for w in range(2, 30, 4):
#     print(w)



# The while loop and how it works
m = 1
# This statement states the while loop.
while m < 5:
    print(m)
    # remember to incremate m to prevent the loop from running forever.
    m += 1

# For the break statement,
# we use the break statement to stop a loop weather a condition is still true.
# eg.

i = 5
# while i < 15:
#     print(i)
#     if i == 13:
#         break
#     i += 1

# The continue statement.
# This is used to skip an interation of a value if a condition is true.

while i < 15:
    i += 1
    if i == 9:
        continue
    print(i)