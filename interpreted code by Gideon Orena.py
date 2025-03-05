# This statement shows a variable that is assigned a value called "Python is fun" which is a string datatype due described by quotes.
some_string = 'Python is fun' 



# This statement states that there a three individual memory spaces with each having a variable name and a value stored in it.
a, b, c = 5, 3.2, 'Hello'
print(a)  # The expression here will be 5 which is an int.
print(b)  # The expression here will be 3.2 which is a float.
print(c)  # The expression here will be a "Hello" which is a coplex numeric datatype.
# This statement states that a varible num1 is assigned a value which is 5.
num1 = 5
# This statement gives an expression datatype and a class which is num1 and the class which is int.
print(num1, 'is of type', type(num1))
# This line states that a value 2.0 is assigned to variable num2.
num2 = 2.0
# The expression will be the value of num2 which is 2.0 and the datatype class which is a float.
print(num2, 'is of type', type(num2))
# This statement states a value which is a complex to a varable which is num3.
num3 = 1+2j
# The expression here will be the value of num3 and the datatype class which is  complex.
print(num3, 'is of type', type(num3))




# This is a list of intems, thus a datatype class which is mutable, ordered and allows duplicating values.
languages = ["Swift", "Java", "Python"]
# In list operators, we can access list intems using there indexes starting from 0.
print(languages[0])   # The expression is "Swift" 
# This will give an expression in the index position of 2.
print(languages[2])   # The expressio is "Python"




#  This statement describes a tuple which is an ordered sequence same with lists but immutable.
product = ('Microsoft', 'Xbox', 499.99)
# This statement talks about accessing elements at index 0, that is why the expression is "Microsoft".
print(product[0])   # Microsoft
# The statment here describes the item in index 1 in the tuple list which is "Xbox".
print(product[1])   # Xbox



# This statement discribes the mapping datatype in which we store values with there coresponding lables.
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
# This statement comand will print an expression of the whole list including the lables and there coresponding values.
print(capital_city)



# This statement discribes the set class datatype, in 
student_id = {112, 114, 116, 118, 115}
# This statement will print out the whole list of student_id including the brackets.
print(student_id)
# The expression that will be run will be a set.
print(type(student_id))



# This statement represents a list with a variable fruits. 
fruits = ["apple", "mango", "orange"] 
# This statement will print out a list of fruits in square brakets.
print(fruits)



# This statement represents a tuple which is represented with the parentheses brakets. 
numbers = (1, 2, 3) 
# This statement will print out a tuple which is closely the same with a list though it is imutable.
print(numbers)



# This statement represents a dictionary having values each with a lable indexing it. 
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
# This expression will be a list of values in a dicrionary with a varible alphabets.
print(alphabets)



# This statement represents a set, which holds unique values and doesnt accept duplicates.
vowels = {'a', 'e', 'i' , 'o', 'u'} 
# The print out here will be a set with values that a unique. 
print(vowels) 



# This statement represents a set of values with a variable student_id.
student_id = {112, 114, 116, 118, 115}
# This statement will print out values of a set with a variable student_id.
print(student_id)
# The expression on this statement will be <class 'set'>
print(type(student_id))



# This statement represents a tuple having random values. 
product = ('Microsoft', 'Xbox', 499.99)
# This statement will print out a value that is indexed by 0.
print(product[0])   # Microsoft
# This statement will print out a value indexed by 1.
print(product[1])   # Xbox



# The lines 109 and 110 represent two variables a, b having values 7, 2.
a = 7
b = 2
# This statement will print out the sum of the variables a and b which will be 9.
print ('Sum: ', a + b)  
# This statement will print out the value got from subtracting the value of variable a and b which is 5. 
print ('Subtraction: ', a - b)   
# This statement will print  out the value got from multplying the value of variacble a and b which is 14.
print ('Multiplication: ', a * b)  
# This statement will print out the value got from dividing the value of variable a and b which will give us a float as an answer and this is 3.5.
print ('Division: ', a / b) 
# This statement will print out a value rounded off after dividing the value of variable a and b which is from 3.5 to just 3. 
print ('Floor Division: ', a // b)
# This statement will print out the remained got from dividing the value of variable a and b which is 5.
print ('Modulo: ', a % b)  
# This statement will print out a value got from rising the value of variable a to the power of the value of varible b which is 49.
print ('Power: ', a ** b)   



# This statement is a varible a asigned a value 10. 
a = 10
# Thia statement is a variable b asigned a value 5
b = 5 
# This statement says that add the value of variable a to that of b.
a += b      # This is an additional assigment operator.
print(a)
# Output: 15
# This statement is comparing weather the value of variable a is equal to that of b which is False.
print('a == b =', a == b)
# Thia statemen is trying to prove weather the value of variable a is not equal to that of b which is True. 
print('a != b =', a != b)
# This statement is comparing weather the value of variable a is greater than that of b which is True.
print('a > b =', a > b)
# This statement is comparing weather the value of variable a is less than that of b which is False.
print('a < b =', a < b)
# This statement is comparing weather the value of variable a is greater or equal to that of b which is will run True as the expression.
print('a >= b =', a >= b)
# This statement is comparing weather the value of variable a is less or equal to that of b which is False.
print('a <= b =', a <= b)
# This statement representents the and operator which prints True if both operands a true but in this case the print out is false because of the and operator.
print((a > 2) and (b >= 6)) 
# These a logical operators and the and operator only prints True in the terminal if both operands a true.
print(True and True)     # True
print(True and False)    # False


# logical OR
print(True or False)     # This statement prints True because of the or operator which prints True if one of the operands is True.
# This statement has the not operator which normaly prints the oposite of the condition.
print(not True)          # False



# The block of code states 6 operators asigned with each a single operand.
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# This statement is having an identity operator which is 'is not' and this prints True if the operands a not the same.
print(x1 is not y1)  # False
# The is operator prints True if the operands a the same.
print(x2 is y2)  # True
# This statement says is the variable x3 having the same value as y3.
print(x3 is y3)  # True.



# This statement has an operator message asigned an operand 'Hello world' which is a string.
message = 'Hello world'
# This statement has a dictionary with values having labales indexing them, and we access values in the dictionary using there coresponding labales.
dict1 = {1:'a', 2:'b'}
# This statement tells the computer to to check weather there is H in the message operator.
print('H' in message)  # True
# This statement tells the computer to check weather there is hello in the operator message.
print('hello' not in message)  # True.
# This statement has a membership operator that tells the computer to check weather the value is in the sequence and this reterns a boolean expression.
print(1 in dict1)  # True.
# This statement tells the computer to check weather the value 'a' is in the sequence with a variable dict1. 
print('a' in dict1)  # False this is because the value 'a' is indexed with its lable 1, this is the syntax of accessing values in a dictionary.


