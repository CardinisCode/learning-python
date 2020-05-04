# #To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
import unittest





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


 
def break_my_message_down_into_char_pairs(my_message):
    structured_message = ""

    for index in range(0, len(my_message)):
        current_letter = my_message[index]
        if index % 2 ==1:
            structured_message += current_letter + " "
        else:
            structured_message += current_letter

    # structured_message = structured_message
    return structured_message.rstrip()

# - Add an X to the end if the length if odd - Done

def add_X_to_message_end_if_length_is_odd(my_message_to_be_modified):
    for index in range(0, len(my_message_to_be_modified)):
        current_letter = my_message_to_be_modified[index]
        if index == len(my_message_to_be_modified) -2:
            if current_letter == " ":
                my_message_to_be_modified += "X"

    return my_message_to_be_modified

# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX). Done 

def find_double_pairs_in_message(my_message_to_be_modified):
    updated_message = ""
    second_char_index = 1
    prev_index = 0
    for index in range(0, len(my_message_to_be_modified)):
        current_letter = my_message_to_be_modified[index]
        if index == second_char_index: 
            prev_letter = my_message_to_be_modified[prev_index]
            if current_letter == prev_letter:
                updated_message += "X"
            else:
                updated_message += current_letter

            second_char_index += 3
            prev_index += 3
        else:
            updated_message += current_letter

    return updated_message


def structure_my_message(my_message_cleaned):
    my_message_broken_down_into_pairs = break_my_message_down_into_char_pairs(my_message_cleaned)
    x_added_to_end_message_if_length_is_odd = add_X_to_message_end_if_length_is_odd(my_message_broken_down_into_pairs)
    second_letter_replaced_if_of_same_char_pair = find_double_pairs_in_message(x_added_to_end_message_if_length_is_odd)

    return second_letter_replaced_if_of_same_char_pair


def process_row_case_switch(character_pair):
    updated_pair = ""
    first_letter = character_pair[0]
    second_letter = character_pair[1]

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
            if current_letter == first_letter:
                cipher_letter = CIPHER[index_row][index_column + 1]
                updated_pair += cipher_letter
            elif current_letter == second_letter:
                if index_column == len(current_row)-1:
                    cipher_letter = CIPHER[index_row][0]
                else:
                    cipher_letter = CIPHER[index_row][index_column + 1]
                
                updated_pair += cipher_letter

    return updated_pair


def process_column_case_switch(character_pair):
    first_cipher_letter = ""
    second_cipher_letter = ""
    
    first_letter = character_pair[0]
    second_letter = character_pair[1]

    for index_row in range(0, len(CIPHER)):

        current_column = [
            CIPHER[0][index_row], 
            CIPHER[1][index_row], 
            CIPHER[2][index_row], 
            CIPHER[3][index_row], 
            CIPHER[4][index_row]
        ]

        for index_column in range(0, len(current_column)):
            current_letter = current_column[index_column]
            next_letter = current_column[(index_column +1) % 5]

            if current_letter == first_letter: 
                first_cipher_letter = next_letter
            elif current_letter == second_letter:
                second_cipher_letter = next_letter

    return first_cipher_letter + second_cipher_letter


def process_rectangle_case_switch(current_pair): 
    first_cipher_letter = ""
    second_cipher_letter = "" 

    first_letter_index = 0
    first_letter_row = None
    first_letter_column = None 

    second_letter_index = 0
    second_letter_row = None
    second_letter_column = None 



    return first_cipher_letter + second_cipher_letter

CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



def encrypt(my_message_structured):
    my_message_as_list = my_message_structured.split(" ")
    my_updated_message = ""

    for index in range(0, len(my_message_as_list)):
        current_pair = my_message_as_list[index]
        first_letter = current_pair[0]
        second_letter = current_pair[1]

        for index_row in range(0, len(CIPHER)):
            current_row = CIPHER[index_row]
            if first_letter in current_row and second_letter in current_row:
                updated_pair = process_row_case_switch(current_pair)
                my_updated_message += updated_pair

            current_column = [
                CIPHER[(index_row) % 5][0], 
                CIPHER[(index_row +1) % 5][0], 
                CIPHER[(index_row +2) % 5][0], 
                CIPHER[(index_row +3) % 5][0], 
                CIPHER[(index_row +4) % 5][0]
            ]
            if first_letter in current_column and second_letter in current_column:
                updated_pair = process_column_case_switch(current_pair)
                my_updated_message += updated_pair

            else:
                updated_pair = process_rectangle_case_switch(current_pair)

    return my_updated_message



message_to_encryp = "PS. Hello, world"
#PS HE LL OW OR LD
my_message_cleaned = clean_my_string(message_to_encryp)
my_message_structured = structure_my_message(my_message_cleaned)
my_message_encrypted = encrypt(my_message_structured)
print(my_message_encrypted)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX

#print(encrypt(message_to_encryp))

#QLGRQTVZIBTYQZ
#PS HE LX OW OR LD
#QL GR QT VZ IB TY QZ

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
        actual = break_my_message_down_into_char_pairs("HELLOWORLD")
        self.assertEqual(expected, actual)


    def test_adding_X_when_message_length_is_odd(self):
        expected = "HE LL OW OR LD SX"
        actual = add_X_to_message_end_if_length_is_odd("HE LL OW OR LD S")
        self.assertEqual(expected, actual)


    def test_find_double_pairs_in_message(self):
        expected = "HE LX OW OR LD SX"
        actual = find_double_pairs_in_message("HE LL OW OR LD SX")
        self.assertEqual(expected, actual)


    def test_my_structured_message(self):
        expected = "HE LX OW OR LD SX"
        actual = structure_my_message("HELLOWORLDS")
        self.assertEqual(expected, actual)


    def test_row_case_switch(self):
        expected = "QL"
        actual = process_row_case_switch("PS")
        self.assertEqual(expected, actual)   


    def test_column_case_switch(self):
        expected = "TY"
        actual = process_column_case_switch("LD")
        self.assertEqual(expected, actual) 


    def test_rectangle_case_switch(self):
        expected = "GR"
        actual = process_rectangle_case_switch("HE")
        self.assertEqual(expected, actual) 



if __name__ == "__main__":
    unittest.main()