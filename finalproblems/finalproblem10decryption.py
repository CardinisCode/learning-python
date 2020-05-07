import unittest

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


CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))


def process_row_case_switch(character_pair):
    updated_pair = ""
    first_letter = character_pair[0]
    second_letter = character_pair[1]

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
            if current_letter == first_letter:
                cipher_letter = CIPHER[index_row][index_column - 1]
                updated_pair += cipher_letter

    for index_row in range(0, len(CIPHER)):
        current_row = CIPHER[index_row]
        for index_column in range(0, len(current_row)):
            current_letter = current_row[index_column]
            if current_letter == second_letter:
                if index_column == len(current_row)-1:
                    cipher_letter = CIPHER[index_row][0]
                else:
                    cipher_letter = CIPHER[index_row][index_column - 1]
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



def decrypt(message_to_decrypt):
    my_message_structured = break_my_message_down_into_char_pairs(message_to_decrypt)
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
                updated_row_pair = process_row_case_switch(current_pair)
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
            print(current_column)
            if first_letter in current_column and second_letter in current_column:
                print(first_letter, second_letter)
                updated_column_pair = process_column_case_switch_for_decryption(current_pair)
                my_updated_message += updated_column_pair
                found_pairs.append(current_pair)
                break
            
        if not current_pair in found_pairs:
            updated_rect_pair = process_rectangle_case_switch(current_pair)
            my_updated_message += updated_rect_pair

    return my_updated_message


message_to_decrypt = "KAXNDCABYWDZQRYXNRVHCX"

my_message_split_into_pairs = break_my_message_down_into_char_pairs(message_to_decrypt)
print("My message to decrypt broken down into pairs:")
print(my_message_split_into_pairs)
print()

expected_output = "FOURTYONETOTHIRTYEIGHT"
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

# expected_output = "GWGRPNHRLKQREQMZUZABARXYNFQOXDEGRHBRVYNPONPY"
# expected_split_into_pairs = break_my_message_down_into_char_pairs(expected_output)











class CheckMyDecryption(unittest.TestCase):
    message = "KAXNDCABYWDZQRYXNRVHCX"
    
    def test_decrypt(self):
        expected = "FOURTYONETOTHIRTYEIGHT"
        actual = decrypt(self.message)

        self.assertEqual(expected, actual)


    def test_structure_my_message_by_splitting_it_into_pairs(self):
        expected = "HE LL OW OR LD"
        actual = break_my_message_down_into_char_pairs("HELLOWORLD")
        self.assertEqual(expected, actual)


    def test_row_case_switch(self):
        expected = "PS"
        actual = process_row_case_switch("QL")
        self.assertEqual(expected, actual)   


    def test_column_case_switch(self):
        expected = "HI"
        actual = process_column_case_switch_for_decryption("QR")
        self.assertEqual(expected, actual) 


    def test_rectangle_case_switch(self):
        expected = "HE"
        actual = process_rectangle_case_switch("GR")
        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()