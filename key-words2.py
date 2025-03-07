def create_input_function(field_name):
    """Dynamically creates an input function for a given field name."""
    return lambda: input(f"Enter {field_name}: ")

#lambda ia a key word in python used to pass simple functions as arguments 
# List of student details to collect
fields = ["Name", "Age", "Gender", "Course", "year_of_study"]

# Dictionary to store student details
student_details = {}

# Collect input dynamically
for field in fields:
    input_func = create_input_function(field)  # Create a function dynamically
    student_details[field] = input_func()  # Call the function to get input

# Display the collected details
print("\nStudent Details:")
# This statement talks about the dictionary that saves values using lables
for key, value in student_details.items():
    print(f"{key}: {value}")

def tests(test1, test2, course_work, final_exam):
    sum_marks = test1 + test2
    average = sum_marks / 2
    final_mark = average * (40 / 100)
    final_exam_mark = final_exam * (60 / 100)
    total_mark = final_mark + final_exam_mark
    return (f"Sum: {sum_marks}, Average: {average}, Final Mark: {final_mark}, Final exam: {final_exam_mark}, Total mark: {total_mark}")
print(tests(60, 70, 40, 80))
