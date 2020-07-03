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


#Write your function here!
def format_my_string(current_string):
    updated_string = ""
    ordinal_values = []

    for letter in current_string:
        ordinal_value = ord(letter)
        ordinal_values.append(ordinal_value)
        if ordinal_value >= 65 and ordinal_value <= 90:
            updated_string += chr(ordinal_value + 32)
        elif ordinal_value >= 97 and ordinal_value <= 122:
            updated_string += letter

    return updated_string


def sort_my_string(current_string):
    print("Before sorting:", current_string)
    sorted_string = ""
    ordinal_values = []

    for letter in current_string:
        ordinal_values.append(ord(letter))
    
    ordinal_values = sorted(ordinal_values)
    print("ORdinals after sort:", ordinal_values)

    for ordinal in ordinal_values:
        sorted_string += chr(ordinal)

    return sorted_string



def create_palindrome(possible_palidrome):
    string_after_formating = format_my_string(possible_palidrome)
    mid_point = len(possible_palidrome) // 2

    first_half = possible_palidrome[:mid_point]
    if len(possible_palidrome) % 2 == 0: # Even numbers
        second_half = possible_palidrome[mid_point:]
    
    elif len(possible_palidrome) % 2 == 1: #Odd numbers
        second_half = possible_palidrome[mid_point +1:]
 
    first_half = sort_my_string(first_half)
    second_half = sort_my_string(second_half)

    if first_half == second_half:
        return possible_palidrome

    new_palidrome = possible_palidrome + possible_palidrome[::-1]

    return new_palidrome




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
print()
print(create_palindrome("Madam in Eden, I'm Adam"))
print()
print(create_palindrome("Mister in Eden, I'm Eve"))
print()
print(create_palindrome("Tarrat"))



