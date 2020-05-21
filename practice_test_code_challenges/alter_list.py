#Write a function called alter_list. alter_list should have
#two parameters: a list of strings and a list of integers.
#
#The list of integers will represent indices for the list of
#strings. alter_list should alter the capitalization of all
#the words at the designated indices. If the word was all
#capitals, it should become all lower case. If it was all
#lower case, it should become all capitals. You may assume
#that the words will already be all-caps or all-lower case.
#
#For example:
#
# string_list = ["hello", "WORLD", "HOW", "are", "you"]
# index_list = [0, 2]
# alter_list(string_list, index_list) -> 
#                ["HELLO", "WORLD", "how", "are", "you"]
#
#After calling alter_list, the strings at indices 0 and 2
#have switched their capitalization. 
#
#Note that it may be the case that the same index is present
#in the second twice. If this happens, you should switch the
#text at that index twice. For example:
#
# string_list = ["hello", "WORLD", "HOW", "are", "you"]
# index_list = [0, 2, 2]
# alter_list(string_list, index_list) -> 
#                ["HELLO", "WORLD", "HOW", "are", "you"]
#
#2 is in index_list twice, so the string at index 2 is
#switched twice: capitals to lower case, then back to
#capitals.

import unittest
#Write your function here!
def alter_list(random_strings, indices):
    for index in indices:
        current_word = random_strings[index]
        updated_word = ""
        first_letter = current_word[0]
        
        if ord(first_letter) >= 65 and ord(first_letter) <= 90:
            updated_word = current_word.lower()
        elif ord(first_letter) >= 97 and ord(first_letter) <= 122:
            updated_word = current_word.upper()
        
        random_strings[index] = updated_word

    return random_strings


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#["hello", "WORLD", "HOW", "are", "you"]
#["HELLO", "WORLD", "HOW", "are", "you"]
# print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2])) -> ["HELLO", "WORLD", "how", "are", "you"]
# print(alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2, 2])) -> ["HELLO", "WORLD", "HOW", "are", "you"]

class TestAlterList(unittest.TestCase):
    def test_switching_capitalization_with_two_indices(self):
        print("--------------------------")
        expected = ["HELLO", "WORLD", "how", "are", "you"]
        actual = alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2])

        self.assertEqual(expected, actual)

    
    def test_switching_capitalization_with_duplicated_index(self):
        print("--------------------------")
        expected = ["HELLO", "WORLD", "HOW", "are", "you"]
        actual = alter_list(["hello", "WORLD", "HOW", "are", "you"], [0, 2, 2])

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()
