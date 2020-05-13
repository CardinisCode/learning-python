#Imagine you're writing a program to check attendance on a
#classroom roster. The list of students in attendance comes
#in the form of a list of instances of the Student class.
#
#You don't have access to the code for the Student class.
#However, you know that it has at least two attributes:
#first_name and last_name.
#
#Write a function called check_attendance. check_attendance
#should take three parameters: a list of instances of
#Student representing the students in attendance, a first
#name as a string, and a last name as a string (in that
#order).
#
#The function should return True if any instance in the
#list has the same first and last name as the two
#arguments. It should return False otherwise.
#
#You may assume that the list of students is sorted
#alphabetically, by last name and then by first name. This
#allows you to solve this with a binary search. However,
#you may also solve this problem with a linear search if
#you would prefer.

#Note to self:
# - I solved this challenge using both a Linear Search and a Binary Search


import unittest

# Write your function here!
def check_attendance_using_Linear_Search(todays_attendance, first_name, last_name):
    for student in todays_attendance:
        if student.first_name == first_name and student.last_name == last_name:
            return True

    return False


def sort_my_list(todays_attendance):
    list_of_names = []

    for student in todays_attendance:
        student_first_name = student.first_name
        student_last_name = student.last_name
        list_of_names.append(student_last_name + " " + student_first_name)
    list_of_names.sort()
      
    return list_of_names
    # return sorted_list


def check_attendance(todays_attendance, first_name, last_name):
    updated_attendance = sort_my_list(todays_attendance)
    students_presence = check_attendance_using_Binary_Search(updated_attendance, first_name, last_name)

    return students_presence


def check_attendance_using_Binary_Search(todays_attendance, first_name, last_name):
    mid_index = len(todays_attendance) //2
    mid_student = todays_attendance[mid_index]
    compare_name = last_name + " " + first_name
    if len(todays_attendance)==1:
        if todays_attendance[0] == compare_name:
            return True
        return False

    if compare_name == mid_student:
        return True

    if mid_student > compare_name:
        return check_attendance_using_Binary_Search(todays_attendance[:mid_index], first_name, last_name)
        
    elif compare_name > mid_student:
        return check_attendance_using_Binary_Search(todays_attendance[mid_index:], first_name, last_name)

    return False



#If you would like, you may implement the Student class as
#described and use it to test your code. This is not
#necessary to complete the problem, but it may help you
#debug. If you create a Student class, all you need is
#a constructor that assigns values to two attributes:
#self.first_name and self.last_name.
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

todays_attendance = [
    Student("Ashtyn", "Luna"), 
    Student("Jackie", "Luna"),
    Student("Braylen", "Reed"),
    Student("Madisyn", "Sparks"),
    Student("Madisyn", "Macdonald"),
    Student("Sophie", "Sparks"),
    Student("Marguerite", "Luna"),
    Student("Gautam", "Foley"),
    Student("Franklin", "Foley"),
]


check_student_presence_using_linear_search = check_attendance_using_Linear_Search(todays_attendance, "Mary", "Poppins")
todays_attendance = sort_my_list(todays_attendance)
check_student_present_using_binary_search = check_attendance_using_Binary_Search(todays_attendance, "Mary", "Poppins")
print(check_student_present_using_binary_search)



class TestStudentAttendance(unittest.TestCase):
    todays_attendance = [Student("Harry", "Johns"), Student("Mary", "Poppins"), Student("Mary", "Smith")]

    def testing_student_is_present_using_Linear_Search(self):
        print("----------------------------------------")
        expected = True
        actual = check_attendance_using_Linear_Search(self.todays_attendance, "Mary", "Poppins")
        self.assertEqual(expected, actual)

    def testing_student_is_present_using_Binary_Search(self):
        print("----------------------------------------")
        expected = True
        actual = check_attendance_using_Binary_Search(todays_attendance, "Franklin", "Foley")
        self.assertEqual(expected, actual)

    def testing_Binary_search_when_students_name_isnt_in_the_middle(self):
        print("----------------------------------------")
        expected = True
        actual = check_attendance_using_Binary_Search(todays_attendance, "Franklin", "Foley")
        self.assertEqual(expected, actual)

    
    def testing_Binary_Search_where_name_isnt_present(self):
        print("----------------------------------------")
        expected = False
        actual = check_attendance_using_Binary_Search(todays_attendance, "John", "Smith")
        self.assertEqual(expected, actual)

    def test_bin_search_fail_case_alpha(self):
        attendance = [
            Student('Jackie', 'Conley'),
            Student('Jackie', 'Howell'),
            Student('Kelsie', 'Joyner'),
            Student('Lindsay', 'Luna'),
            Student('Kelsie', 'Macdonald'),
            Student('Lindsay', 'Macdonald'),
            Student('Lindsay', 'Pittman')
        ]

        actual = check_attendance_using_Binary_Search(sort_my_list(attendance), "Kelsie", "Macdonald")

        self.assertEqual(True, actual)



if __name__ == "__main__":
    unittest.main()
