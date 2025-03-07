def add(student_detail):
    """Dynamically creates an input function for a given field name."""
    return lambda: input(f"Enter {student_detail}: ")

#lambda ia a key word in python used to pass simple functions as arguments 
# List of student details to collect
details = ["Name", "Age", "Gender", "Course", "year_of_study"]

# Dictionary to store student details
student_details = {}

# Collect input dynamically
for detail in details:
    input_func = add(detail)  # Create a function dynamically
    student_details[detail] = input_func()  # Call the function to get input

# Display the collected details
print("\nStudent Details:")
# This statement talks about the dictionary that saves values using lables
for key, value in student_details.items():
    print(f"{key}: {value}")

# defined a dynamic function(tests)
def tests(test1, test2, course_work, final_exam):
#sum of the 2 best done test1 and test2    
    sum_marks = test1 + test2
# average of the 2 best done tests    
    average = sum_marks / 2
# final mark of 2 best done tests marked out of 40    
    final_mark = average * (40 / 100)
# final exam mark marked out of 60    
    final_exam_mark = final_exam * (60 / 100)
#total marks out of 100    
    total_mark = final_mark + final_exam_mark
    return (f"Sum: {sum_marks}, Average: {average}, Final Mark: {final_mark}, Final exam: {final_exam_mark}, Total mark: {total_mark}")
# calling out function tests to print results
print(tests(60, 70, 40, 80))
