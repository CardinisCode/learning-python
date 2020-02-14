def course_info(aList_of_tuples):
    list_of_students_names = []
    total_student_ages = 0
    number_of_students = len(aList_of_tuples)

    for (student, age) in aList_of_tuples:
        list_of_students_names.append(student)
        total_student_ages += age

    average_age = total_student_ages/number_of_students
    course_dict = {} 
    course_dict["students"] = list_of_students_names
    course_dict["avg_age"] = average_age

    return course_dict









print(course_info([("Jackie", 20), ("Marguerite", 21)]))