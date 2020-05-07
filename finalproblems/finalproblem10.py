import unittest

CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))


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


def add_X_to_message_end(my_message_to_be_modified):
    for index in range(0, len(my_message_to_be_modified)):
        current_letter = my_message_to_be_modified[index]
        if index == len(my_message_to_be_modified) -2:
            if current_letter == " ":
                my_message_to_be_modified += "X"

    return my_message_to_be_modified


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
    my_message_broken_down = break_my_message_down_into_char_pairs(my_message_cleaned)
    x_added_to_end_message = add_X_to_message_end(my_message_broken_down)
    second_letter_replaced = find_double_pairs_in_message(x_added_to_end_message)

    return second_letter_replaced


def process_row_case_switch_for_encryption(character_pair):
    updated_pair = ""
    first_letter = character_pair[0]
    second_letter = character_pair[1]

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
            if current_letter == first_letter:
                cipher_letter = CIPHER[index_row][(index_column +1) % 5]
                updated_pair += cipher_letter

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
    
            if current_letter == second_letter:
                if index_column == len(current_row)-1:
                    cipher_letter = CIPHER[index_row][0]
                else:
                    cipher_letter = CIPHER[index_row][(index_column +1) % 5]
                updated_pair += cipher_letter

    return updated_pair


def process_column_case_switch_for_encryption(character_pair):
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

        for index_column in range(0, len(current_column)):
            current_letter = current_column[index_column]
            next_letter = current_column[(index_column +1) % 5]

            if current_letter == second_letter: 
                second_cipher_letter = next_letter

    return first_cipher_letter + second_cipher_letter


def process_rectangle_case_switch(current_pair): 
    first_letter = current_pair[0]
    first_letter_row = 0
    first_letter_column = 0 

    second_letter = current_pair[1]
    second_letter_row = 0
    second_letter_column = 0 

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        if first_letter in current_row: 
            first_letter_row = index_row
            for index_column in range(0, len(current_row)):
                current_letter = current_row[index_column]
                if current_letter == first_letter:
                    first_letter_column = index_column

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        if second_letter in current_row: 
            second_letter_row = index_row
            for index_column in range(0, len(current_row)):
                current_letter = current_row[index_column]
                if current_letter == second_letter:
                    second_letter_column = index_column
    
    first_cipher_letter = CIPHER[first_letter_row][second_letter_column]
    second_cipher_letter = CIPHER[second_letter_row][first_letter_column] 

    return first_cipher_letter + second_cipher_letter


def encrypt(message_to_encryp):
    my_message_cleaned = clean_my_string(message_to_encryp)
    my_message_structured = structure_my_message(my_message_cleaned)
    my_message_as_list = my_message_structured.split(" ")
    my_updated_message = ""
    found_pairs = []

    for index in range(0, len(my_message_as_list)):
        current_pair = my_message_as_list[index]
        first_letter = current_pair[0]
        second_letter = current_pair[1]
        # print(current_pair, ":", first_letter, second_letter)

        for index_row in range(0, len(CIPHER)):
            current_row = CIPHER[index_row]
            if first_letter in current_row and second_letter in current_row:
                updated_row_pair = process_row_case_switch_for_encryption(current_pair)
                my_updated_message += updated_row_pair
                found_pairs.append(current_pair)
                break

            current_column = [
                CIPHER[(index_row) % 5][index_row], 
                CIPHER[(index_row +1) % 5][index_row], 
                CIPHER[(index_row +2) % 5][index_row], 
                CIPHER[(index_row +3) % 5][index_row], 
                CIPHER[(index_row +4) % 5][index_row]
            ]

            if first_letter in current_column and second_letter in current_column:
                updated_column_pair = process_column_case_switch_for_encryption(current_pair)
                my_updated_message += updated_column_pair
                found_pairs.append(current_pair)
                break
            
        if not current_pair in found_pairs:
            updated_rect_pair = process_rectangle_case_switch(current_pair)
            my_updated_message += updated_rect_pair

    return my_updated_message


def process_row_case_switch_for_decrypt(character_pair):
    updated_pair = ""
    first_letter = character_pair[0]
    second_letter = character_pair[1]

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
            if current_letter == first_letter:
                cipher_letter = CIPHER[index_row][(index_column - 1) %5]
                updated_pair += cipher_letter

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
            if current_letter == second_letter:
                print(current_letter, ":", index_column)
                if index_column == 0:
                    cipher_letter = CIPHER[index_row][(index_column - 1) %5]
                else:
                    cipher_letter = CIPHER[index_row][(index_column - 1) %5]
                    print("cipher_letter",cipher_letter, "vs current_letter:", current_letter)

                updated_pair += cipher_letter

    return updated_pair


def process_column_case_switch_for_decryption(character_pair):
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
            next_letter = current_column[(index_column -1) % 5]

            if current_letter == first_letter: 
                first_cipher_letter = next_letter


        for index_column in range(0, len(current_column)):  
            current_letter = current_column[index_column]
            next_letter = current_column[(index_column -1) % 5]

            if current_letter == second_letter:
                second_cipher_letter = next_letter

    return first_cipher_letter + second_cipher_letter


def decrypt(message_to_encryp):
    my_message_structured = break_my_message_down_into_char_pairs(message_to_encryp)
    my_message_as_list = my_message_structured.split(" ")
    my_updated_message = ""
    found_pairs = []

    for index in range(0, len(my_message_as_list)):
        current_pair = my_message_as_list[index]
        first_letter = current_pair[0]
        second_letter = current_pair[1]

        for index_row in range(0, len(CIPHER)):
            current_row = CIPHER[index_row]
            if first_letter in current_row and second_letter in current_row:
                updated_row_pair = process_row_case_switch_for_decrypt(current_pair)
                my_updated_message += updated_row_pair
                found_pairs.append(current_pair)
                break

            current_column = [
                CIPHER[(index_row) % 5][index_row], 
                CIPHER[(index_row +1) % 5][index_row], 
                CIPHER[(index_row +2) % 5][index_row], 
                CIPHER[(index_row +3) % 5][index_row], 
                CIPHER[(index_row +4) % 5][index_row]
            ]
            if first_letter in current_column and second_letter in current_column:
                updated_column_pair = process_column_case_switch_for_decryption(current_pair)
                my_updated_message += updated_column_pair
                found_pairs.append(current_pair)
                break
            
        if not current_pair in found_pairs:
            updated_rect_pair = process_rectangle_case_switch(current_pair)
            my_updated_message += updated_rect_pair

    return my_updated_message

message_to_encryp = "PS. Hello, worlds"
my_message_encrypted = encrypt(message_to_encryp)
message_to_decrypt = "QMDNMNRHHDQGRB"
my_message_decrypted = decrypt(message_to_decrypt)



my_message_split_into_pairs = break_my_message_down_into_char_pairs(message_to_decrypt)
print("My message to decrypt broken down into pairs:")
print(my_message_split_into_pairs)
print()

expected_output = "PLAYFAIRCIPHER"
expected_split_into_pairs = break_my_message_down_into_char_pairs(expected_output)
print("Their expected output split into pairs:")
print(expected_split_into_pairs)
print()


my_message_decrypted = decrypt(message_to_decrypt)

my_output_broken_down_into_pairs = break_my_message_down_into_char_pairs(my_message_decrypted)
print("My current output broken down into pairs:")
print(my_output_broken_down_into_pairs)
print()


if my_message_decrypted == expected_output:
    print("Well done! Message successfully decrypted!")







class CheckMyEncryption_and_Decryption(unittest.TestCase): 
    encrypt_message = "PS. Hello, worlds"
    decrypt_message = "QMDNMNRHHDQGRB"
    
    def test_encrypt(self):
        expected = "QLGRQTVZIBTYQZ"
        actual = encrypt(self.encrypt_message)

        self.assertEqual(expected, actual)


    def test_decrypt(self):
        expected = "PLAYFAIRCIPHER"
        actual = decrypt(self.decrypt_message)

        self.assertEqual(expected, actual)
    

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
        actual = add_X_to_message_end("HE LL OW OR LD S")
        self.assertEqual(expected, actual)


    def test_find_double_pairs_in_message(self):
        expected = "HE LX OW OR LD SX"
        actual = find_double_pairs_in_message("HE LL OW OR LD SX")
        self.assertEqual(expected, actual)


    def test_my_structured_message(self):
        expected = "HE LX OW OR LD SX"
        actual = structure_my_message("HELLOWORLDS")
        self.assertEqual(expected, actual)


    def test_row_case_switch_for_encryption(self):
        expected = "QL"
        actual = process_row_case_switch_for_encryption("PS")
        self.assertEqual(expected, actual)   


    def test_row_case_switch_for_decryption(self):
        expected = "PS"
        actual = process_row_case_switch_for_decrypt("QL")
        self.assertEqual(expected, actual)  


    def test_column_case_switch_for_encryption(self):
        expected = "TY"
        actual = process_column_case_switch_for_encryption("LD")
        self.assertEqual(expected, actual) 


    def test_column_case_switch_for_decryption(self):
        expected = "LD"
        actual = process_column_case_switch_for_decryption("TY")
        self.assertEqual(expected, actual) 


    def test_rectangle_case_switch(self):
        expected = "GR"
        actual = process_rectangle_case_switch("HE")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()