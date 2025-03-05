# # student_id = {112, 114, 116, 118, 115}

# # print(type(student_id))


# # Sequence data types.
# # list [].
# # It is mutable.
# # It is ordered.
# # It is indexed.
# # It is allows duplicates.

# # list of students names.
# students = ["Alice","Bob","charlie"]
# # This line talks of adding a name to the list.
# students.append("David")
# # This statement talks of modifaying a list.
# students[1] = "Brian"
# print(students)

# # This statement removes all changes made on the list and prints the original list.
# # students.pop()
# # print(students)



# # Tuple.
# # This is only defined by parentheses ().
# # Though you can convert a tuple in to a list.eg num =([,,,,,])
# # Its the same as the list in behaviour, it is indext
# # It is imutable, cant be changed.
# # A tuple accepts duplicating, it can have repeated values.

# # Tuple set ()
# atendence = ("Alice", "Bob","Charlie")
# # atendence.append("Sam") # This line prints a error becausea items in a tuple cant be changes and it a read only.
# # atendence[1] = "Arnold"

# print(atendence)


# # Dictionary 
# # Is unordered collection of key_value pair, where each key maps a specific value.



# study = ["Andrew", "Mark", "Angela", "sitati", "Allan", "Joan"]
# study.append("Mathew")
# print(study)

# OPERATORS IN PYTHON.
# Arithmetic operators
# Assigment operators
# comparison operators
# logical operstors
# SPECIAL OPERATORS
# Membership operators
# Identity operators

# Arithmetic operators.
# +, -, *, /, // Floor division, % Modulos, ** Power.

# Assigment operators.
# =, ==, +=, -=, *=, /=, %= Remaider assigment, **= Exponent asssigment.

# Comparison operator.
# == Equal to, != Not equal to, <, >, <=, >=.

# Logical operators.
# and = True if both operands a True, or = True if at least one of the operand is True., not = True if the operand false and vise versa.

# SPECIAL OPERATORS.
# Membership operators.
# in, not in.
# in = True if the value is found in the sequence, not in = True if the value is found in the sequence. 

# Identity operators.
# is, is not
# is = True if both the operands a the same, is not = True if both the operands a not identical.


# The for loop
# it interates over a sequence, this could be a list, tuple, range and a string, runs a block of code for a certain number of times.
products = ['Beans', 'Maize', 'G-nuts', 'Cowpeas', 'Soebeans']
# # for loop = Used to run a block of code for a certain number of times.
# for products in products:
#     print(products)


# # range funtction.
# # For the range function
# # We have the start, exclusive and the step.

# for products in range(4):
#     print(products)

# for student in range(4, 10):
#     print(student)

# for fruits in range(2, 19):
#     print( fruits)

# for bananas in range(2, 19, 4): # Here the start is 2 the exclusive is 19 and the step is 4.
#     print(bananas)

# The for loop with else
# This used when you want to check out a condition in a loop.
# This is also used when you want to execut some code only if the loop finishes with out breaking.

# price = (200000, 8)
# for i in price:
#     print(i)


# basket = "blanket"
# for B in basket:
#     print(B)

# # USING FOR LOOP WITH ENUMERATE.
# # This statement will print out an expression of the list of products but each with its indexing but both braketed and with comers eg. (0, 'Beans')
# for products1 in enumerate(products):
#     print(products1)

# # This statement will print out a list of products but this time round will have no commers and brackets eg. 0 Beans.
# for index, products1 in enumerate(products):
#     print(index, products1)


# names = ["Joan", "Sitati", "Mathew", "Kulabako", "sylvia"]
# ages = [15, 14, 28, 13, 9]
# for index, name in enumerate(names): # Using a for loop with enumerate.
#     print(index, name)

# for index, old in enumerate(ages): 
#     print(index, old)

# for index, some in enumerate(names):
#     print(index, some)

# for index, mark in enumerate(ages): # Using a for loop with enumerate.
#     print(index, mark)



# USING THE FOR LOOP WITH ZIP.
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.") # The syntax of writing an f-string is f"string with {expressions}.

# students5 = ["Joan", "Sitati", "Mathew", "Kulabako", "sylvia"]
# numbers = [15, 14, 28, 13, 9]
# for student, number in zip(students5, numbers):
#     print(f"{student} is {number} years old.")


amount = [2000, 3000, 4500, 5000, 3000]
exp = ["good befor due date"] 


# for produce, size in zip(students5, numbers):
#     print(f"{produce} is {size} years to expiary")


for items, sales, expiary in zip(products, amount, exp *5): # You use a multiplication arithmetic operatore to run a string multiple times ziped with other lists.
    print(f"{items} a {sales} shs but {expiary}")

print(f" The sum of {amount[0]} and {amount[3]} is {amount[0] + amount[3]} ") # Expressions inside an f-string.


def mark_sheet():
    test1 = int(input("Enter test1 marks: "))
    test2 = int(input("Enter test2 marks: "))
    final_exams = int(input("Enter final exams marks: "))
    print("sum_marks")
    print(f"The sum of {test1} and {test2} is {test1 + test2}")
    print("average_mark")
    average_mark = (f"The average of is {test1 + test2} / 2 ")
    print(average_mark)
    total_mark = (f"The total mark is {average_mark * 40/100 + final_exams * 60/100} ")
    print(total_mark)

    
    return total_mark
print(mark_sheet())