# Using functions capture the students details Name, Age, Gender, Program, Year of study, Faculty, Date of Birth, Test1 marks, Test2 marks and final exam marks.Get the sum of test 1 and 2 and get its average. Test 1 and 2 is marked out of 40 get the final mark. And final exam is marked out of 60 get also its final mark. Later add the final marks to get the final results

def students_details():
    name = input("Enter students name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    program = input("Enter your program: ")
    year_of_study = int(input("Enter your year of study: "))
    faculty = input("Enter your faculty: ")
    date_of_birth = input("Enter your date of birth: ")
    students_info = {"name" : name, "age" : age, "gender" : gender, "program" : program, "year_of_study" : year_of_study, "faculty" : faculty, "date_of_birth" : date_of_birth }

    return students_info
print(students_details())

def mark_sheet():
    test1 = int(input("Enter test1 marks: "))
    test2 = int(input("Enter test2 marks: "))
    final_exams = int(input("Enter final exams marks: "))
    print("sum_marks")
    sum_marks = test1 + test2
    print(sum_marks)
    print("average_mark")
    average_mark = sum_marks / 2
    print(average_mark)
    final_mark = average_mark * 40/100
    print(f"marked out of 40: {final_mark}")
    final_exams = final_exams * 60/100
    print(f"marked out 60 : {final_exams}")
    total_mark = final_mark + final_exams
    print(f"The total mark : {total_mark}")
    total_mark = round(total_mark)
    
    return total_mark
print(mark_sheet())


# Using dynamic function together with input function create a program that can capture student deatils, one student at a time name, age, gender, program, course, year of study, capture test 1 & 2, course work mark and exam mark all those a variables capture from the keyboard using dynamic functions.
# Calculate the two best done among test 1 & 2, course work.
# Average best done tests 1 + 2 / 0.5 = course work mark.
# Finall course marks is marked out of 40.
# Exam mark is out of 60.
# Finall exam mark = exam out of 40 + marked out of 60


# def student_details():
