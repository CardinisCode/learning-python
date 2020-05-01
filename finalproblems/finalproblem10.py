# #To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
import unittest

CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



#Add your code here!
# Convert the string to uppercase. Done! 
# - Replace all Js with Is. - Done! 
# - Remove all non-letter characters. - Done! 

def clean_my_string(message_to_encryp):
    my_message = message_to_encryp.upper()
    updated_string = ""
    for character in my_message:
        ord_char = ord(character)
        if ord_char == 74:
            ord_char = 73
        if ord_char >= 65 and ord_char <= 90: 
            updated_string += chr(ord_char)

    return updated_string


# - Break the string into character pairs. - DONE
# - Add an X to the end if the length if odd
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).

def structure_my_message(my_message_cleaned):
    structured_message = ""

    for index in range(0, len(my_message_cleaned)):
        current_letter = my_message_cleaned[index]
        # print(index, ":", current_letter)
        if index % 2 ==1:
            structured_message += current_letter + " "
        else:
            structured_message += current_letter

    structured_message = structured_message.rstrip()
    print("My structured_message:", structured_message)
    print("Its length is:", len(structured_message))

    # listed_message = []

    # for index in range(0, len(structured_message)):
    #     current_letter = structured_message[index]
    #     listed_message.append(current_letter)





    return structured_message



# def encrypt(my_message_cleaned):



#     return "Work in progress"



message_to_encryp = "PS. Hello, world"
my_message_cleaned = clean_my_string(message_to_encryp)
my_message_structured = structure_my_message(my_message_cleaned)
print(my_message_structured)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX

#print(encrypt(message_to_encryp))

# print(decrypt("QLGRQTVZIBTYQZ"))


class CheckMyPokemonCollection(unittest.TestCase):
    message = "PS. Hello, world"
    
    # def test_encrypt(self):
    #     expected = "QLGRQTVZIBTYQZ"
    #     actual = encrypt(self.message)

    #     self.assertEqual(expected, actual)


    def test_clean_my_string_upper_casing_everything(self):
        expected = "HELLO"
        actual = clean_my_string("hello")

        self.assertEqual(expected, actual)

    def test_clean_my_string_with_non_letter_characters_removed(self):
        expected = "HELLOWORLD"
        actual = clean_my_string("Hello. world")
        self.assertEqual(expected, actual)

    def test_clean_my_string_by_replacing_Js_with_Is(self):
        expected = "HELLOIELLY"
        actual = clean_my_string("Hello. Jelly")
        self.assertEqual(expected, actual)


    def test_structure_my_message_by_splitting_it_into_pairs(self):
        expected = "HE LL OW OR LD"
        actual = structure_my_message("HELLOWORLD")
        self.assertEqual(expected, actual)


    def test_adding_X_when_message_length_is_odd(self):
        expected = "HE LL OW OR LD SX"
        actual = structure_my_message("HELLOWORLDS")
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()