#Write a function called is_palindrome. The function should
#have one parameter, a string. The function should return
#True if the string is a palindrome, False if not.
#
#A palindrome is a sequence of letters that is the same
#forward and backward. For example, "racecar" is a
#palindrome. In determining whether a string is a palindrome
#or not, you should ignore punctuation, capitalization and
#spaces. For example, "Madam in Eden, I'm Adam" is a
#palindrome.
#
#You may assume that the only characters in the string will
#be letters, spaces, apostrophes, commas, periods, and
#question marks.
#
#Hint: Before checking if the string is a palindrome, get
#rid of the spaces and punctuation marks using the replace()
#method and convert the entire string to upper or lower
#case using the upper() or lower() methods.
#
#Hint 2: There are multiple ways to do this! If you're stuck
#on one way, try a different one. You could use string
#slicing, a for loop, or some string methods. Or, try
#printing the string at different stages to see what's going
#wrong!

import unittest

# My 2nd attempt at this challenge:
# (Note I have decided not to comment out my first attempt
#  as I want my tests to remain connected/relevant to my first attempt's code)
# For this reason I've included my 2nd attempt as a comment:

# def format_string(string):
#     updated_string = ""
#     for letter in string:
#         ordinal_value = ord(letter)
#         if ordinal_value >= 65 and ordinal_value <= 90:
#             updated_string += letter.lower()
#         elif ordinal_value >= 97 and ordinal_value <= 122:
#             updated_string += letter

#     return updated_string


# def sort_my_string(string):
#     updated_string = ""
#     ordinal_list = []
#     for letter in string:
#         ordinal_list.append(ord(letter))
#     ordinal_list.sort()
    
#     for ordinal in ordinal_list:
#         updated_string += chr(ordinal)

#     return updated_string
    
    
# def is_palindrome(string):
#     updated_string = format_string(string)
#     print(updated_string)
#     mid_point = len(updated_string) // 2
    
#     if len(updated_string) % 2 == 0:
#         first_half = updated_string[0:mid_point]
#         second_half = updated_string[mid_point:]
        
#     elif len(updated_string) % 2 == 1:
#         first_half = updated_string[0:mid_point]
#         second_half = updated_string[mid_point+1:]
       
#     first_half = sort_my_string(first_half)
#     second_half = sort_my_string(second_half)
    
#     if first_half == second_half:
#         return True

#     return False


#Write your function here!

# My first attempt - also linked to my unittests. 
def remove_unwanted_characters(string_to_check):
    letters_only_string = ""
    for char in string_to_check:
        ordinal_value = ord(char)

        if ordinal_value >= 97 and ordinal_value <= 122:
            letters_only_string += char
        elif ordinal_value >= 65 and ordinal_value <= 90: 
            letters_only_string += char.lower()

    return letters_only_string


def check_for_palidrome_in_odd_length_string(string_to_be_checked):
    palidrome = True
    length_of_string = len(string_to_be_checked)
    midway_point = length_of_string //2

    for index in range(0, midway_point):
        starting_point = index + 1
        letter_to_left = string_to_be_checked[midway_point - starting_point]
        letter_to_right = string_to_be_checked[midway_point + starting_point]

        if not letter_to_left == letter_to_right:
            return False
        starting_point += 1

    return palidrome


def check_for_palidrome_in_even_length_string(string_to_be_checked):
    length_of_string = len(string_to_be_checked)
    midway_point = length_of_string //2

    for index in range(0, midway_point):
        start_point_left = index +1
        start_point_right = index
        letter_to_left = string_to_be_checked[midway_point - start_point_left]
        letter_to_right = string_to_be_checked[midway_point + start_point_right]

        if not letter_to_left == letter_to_right:
            return False
        start_point_left += 1
        start_point_right += 1

    return True



def is_palindrome(string_to_check):
    palidrome = None
    letters_only_string = remove_unwanted_characters(string_to_check)
    length_of_string = len(letters_only_string)

    if length_of_string % 2 == 1:
        palidrome = check_for_palidrome_in_odd_length_string(letters_only_string)
        return palidrome

    else:
        palidrome = check_for_palidrome_in_even_length_string(letters_only_string)
        return palidrome



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, each on their own line.
print(is_palindrome("racecar"))
print(is_palindrome("Madam in Eden, I'm Adam"))
print(is_palindrome("tsHannahst"))
print(is_palindrome("Mister in Eden, I'm Eve"))



class TestIsPalidrome(unittest.TestCase):
    def test_palidrome_is_true(self):
        expected = True
        actual = is_palindrome("racecar")
        self.assertEqual(expected, actual)


    def test_remove_unwanted_characters(self):
        expected = "madaminedenimadam"
        actual = remove_unwanted_characters("Madam in Eden, I'm Adam")
        self.assertEqual(expected, actual)


    def test_check_for_palidrome_in_odd_length_string(self):
        expected = True
        actual = check_for_palidrome_in_odd_length_string("madaminedenimadam")
        self.assertEqual(expected, actual)



    def test_check_for_palidrome_in_even_length_string(self):
        expected = True
        actual = check_for_palidrome_in_even_length_string("tshannahst")
        self.assertEqual(expected, actual)


    def test_no_palidrome_found(self):
        expected = False
        actual = check_for_palidrome_in_even_length_string("Mister in Eden, I'm Eve")
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()