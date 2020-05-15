import unittest

#A palindrome is a sequence of letters that is the same
#forward and backward. For example, "racecar" is a
#palindrome.
#
#Write a function called create_palindrome. The function should
#have one parameter, a string. The function should return the
#string as a palindrome.
#
#If the string was not already a palindrome, the function should
#return a new string made from the original string and the
#reverse of the original string. For example:
#
# create_palindrome("abc") -> "abccba"
#
#However, if the string _is_ already a palindrome, the function
#should just return the original string by itself. For example:
#
# create_palindrome("racecar") -> "racecar"
#
#In determining whether a string is a palindrome or not, you
#should ignore punctuation, capitalization and spaces. For
#example:
#
# create_palindrome("Madam in Eden, I'm Adam") -> "Madam in Eden, I'm Adam"
#
#In creating a palindrome, though, you should use the original
#formatting:
#
# create_palindrome("Hello there!") -> "Hello there!!ereht olleH"
#
#You may assume that the only characters in the string will
#be letters, spaces, apostrophes, commas, periods, and
#question marks.
#
#Hint: Before checking if the string is a palindrome, get
#rid of the spaces and punctuation marks using the replace()
#method and convert the entire string to upper or lower
#case using the upper() or lower() methods. Remember, though,
#to keep the original string as your result should preserve
#the original punctuation and capitalization.
#
#Hint 2: There are multiple ways to do this! If you're stuck
#on one way, try a different one. You could use string
#slicing, a for loop, or some string methods. Or, try
#printing the string at different stages to see what's going
#wrong!

# Note: 
# I copied all the code I wrote for is_palindrome. 
# So all I had to write is the code for create_palindrome()
# create_palindrome() first checks if a string is a palidrome
# If yes, it just returns the string
# Else:
# I create a reverse copy of the string, add this copy to the original string
# and return the result. 


#Write your function here!
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


def create_palindrome(string_to_check):
    string_is_palidrome = is_palindrome(string_to_check)
    if string_is_palidrome:
        return string_to_check

    string_in_reverse = ""
    for index in range(len(string_to_check)-1, -1, -1):
        string_in_reverse += string_to_check[index]

    return string_to_check + string_in_reverse



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#racecar
#Madam in Eden, I'm Adam
#Mister in Eden, I'm EveevE m'I ,nedE ni retsiM
print(create_palindrome("racecar"))
print(create_palindrome("Madam in Eden, I'm Adam"))
print(create_palindrome("Mister in Eden, I'm Eve"))


# print(is_palindrome("racecar"))
# print(is_palindrome("Madam in Eden, I'm Adam"))
# print(is_palindrome("Mister in Eden, I'm Eve"))







class TestCreatePalidrome(unittest.TestCase):
    def test_string_is_palidrome(self):
        expected = "racecar"
        actual = create_palindrome("racecar")

        self.assertEqual(expected, actual)

    
    def test_create_palidrome(self):
        expected = "Mister in Eden, I'm EveevE m'I ,nedE ni retsiM"
        actual = create_palindrome("Mister in Eden, I'm Eve")

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()