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

def add_X_to_message_end(my_message_to_be_modified):
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
    broken_down_into_pairs = break_my_message_down_into_char_pairs(my_message_cleaned)
    x_added_to_end_message = add_X_to_message_end(broken_down_into_pairs)
    second_letter_replaced = find_double_pairs_in_message(x_added_to_end_message)

    return second_letter_replaced


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

        for index_row in range(0, len(CIPHER)):
            current_row = CIPHER[index_row]
            if first_letter in current_row and second_letter in current_row:
                updated_row_pair = process_row_case_switch(current_pair)
                my_updated_message += updated_row_pair
                found_pairs.append(current_pair)
                break

            current_column = [
                CIPHER[(index_row) % 5][0], 
                CIPHER[(index_row +1) % 5][0], 
                CIPHER[(index_row +2) % 5][0], 
                CIPHER[(index_row +3) % 5][0], 
                CIPHER[(index_row +4) % 5][0]
            ]
            if first_letter in current_column and second_letter in current_column:
                updated_column_pair = process_column_case_switch(current_pair)
                my_updated_message += updated_column_pair
                found_pairs.append(current_pair)
                break
            
        if not current_pair in found_pairs:
            updated_rect_pair = process_rectangle_case_switch(current_pair)
            my_updated_message += updated_rect_pair

    return my_updated_message