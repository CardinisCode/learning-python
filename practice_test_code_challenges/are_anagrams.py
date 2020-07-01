#Write a function called are_anagrams. The function should
#have two parameters, a pair of strings. The function should
#return True if the strings are anagrams of one another,
#False if they are not.
#
#Two strings are considered anagrams if they have only the
#same letters, as well as the same count of each letter. For
#this problem, you should ignore spaces and capitalization.
#
#So, for us: "Elvis" and "Lives" would be considered
#anagrams. So would "Eleven plus two" and "Twelve plus one".
#
#Note that if one string can be made only out of the letters
#of another, but with duplicates, we do NOT consider them
#anagrams. For example, "Elvis" and "Live Viles" would not
#be anagrams.

import unittest
#Write your function here!

# My 2nd take at this challenge:
def sort_my_string(current_string):
    current_string = current_string.lower()
    string_ordinals_as_list = []
    
    for letter in current_string:
        ordinal_value = ord(letter)
        if ordinal_value >= 97 and ordinal_value <= 122:
            string_ordinals_as_list.append(ordinal_value)
            
    string_ordinals_as_list.sort()
    sorted_string = ""
    
    for ordinal in string_ordinals_as_list:
        chr_value = chr(ordinal)
        sorted_string += chr_value
    
    return sorted_string
    

def are_anagrams(first_string, second_string):
    first_string = sort_my_string(first_string)
    second_string = sort_my_string(second_string)
    
    if first_string == second_string:
        return True
    
    return False


# MY first take at this challenge: 

# def remove_unwanted_characters(string):
#     updated_string = ""

#     for letter in string:
#         ordinal_value = ord(letter)
#         if ordinal_value >= 65 and ordinal_value <= 90:
#             updated_string += letter.lower()
#         elif ordinal_value >= 97 and ordinal_value <= 122:
#             updated_string += letter

#     return  updated_string


# def sort_my_string(string):
#     updated_string = ""
#     ordinal_list = []

#     for letter in string:
#         ordinal_value = ord(letter)
#         ordinal_list.append(ordinal_value)

#     ordinal_list.sort()

#     for ordinal in ordinal_list:
#         updated_string += chr(ordinal)

#     return updated_string



# def are_anagrams(string_1, string_2):
#     updated_string_1 = remove_unwanted_characters(string_1)
#     updated_string_2 = remove_unwanted_characters(string_2)

#     updated_string_1 = sort_my_string(updated_string_1)
#     updated_string_2 = sort_my_string(updated_string_2)
    
#     if updated_string_1 == updated_string_2:
#         return True

#     return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False, each on their own line.

# print(are_anagrams("Elvis", "Lives")) -> True
# print(are_anagrams("Elvis", "Live Viles")) -> False
# print(are_anagrams("Eleven plus two", "Twelve plus one")) -> True
# print(are_anagrams("Nine minus seven", "Five minus three")) -> False


class TestCheckForAnagrams(unittest.TestCase):
    def test_found_anagram(self):
        print("--------------------------")
        expected = True
        actual = are_anagrams("Elvis", "Lives")

        self.assertEqual(expected, actual)

    def test_found_no_anagram(self):
        print("--------------------------")
        expected = False
        actual = are_anagrams("Elvis", "Live Viles")

        self.assertEqual(expected, actual)

    # This test only works with my first attempt. This functionality was covered by the sort_my_string() function. 
    # def test_remove_unwanted_characters(self):
    #     print("--------------------------")
    #     expected = "elvis"
    #     actual = remove_unwanted_characters("Elvis")

    #     self.assertEqual(expected, actual)

    def test_sorting_characters_in_string(self):
        print("--------------------------")
        expected = "eilsv"
        actual = sort_my_string("elvis")

        self.assertEqual(expected, actual)

    def test_found_anagram_longer_string(self):
        print("--------------------------")
        expected = True
        actual = are_anagrams("Eleven plus two", "Twelve plus one")

        self.assertEqual(expected, actual)
    

    def test_found_no_anagram_longer_string(self):
        print("--------------------------")
        expected = False
        actual = are_anagrams("Nine minus seven", "Five minus three")

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
