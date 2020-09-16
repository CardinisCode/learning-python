def main():
    credit_card_number = str(input("Number: "))
    user_input_validity = check_user_input(credit_card_number)
    if user_input_validity == False: 
        return "INVALID\n"

    card_type = determine_card_type(credit_card_number)
    valid_card = luhns_algorithm(credit_card_number)

    if valid_card:
        return card_type
        
    return "INVALID\n"


def check_user_input(credit_card_number):
    if not len(credit_card_number) in [13, 15, 16]:
        return False

    for i in range(0, len(credit_card_number)):
        if not int(credit_card_number[i]) in range(0, 10):
            return False
    return True


def determine_card_type(card_number):
    card_length = len(card_number)

    if card_length == 15:
        first_two_values = card_number[:2]
        if first_two_values == "37" or first_two_values == "34":
            return "AMEX\n"
        return "INVALID\n"

    if card_length == 16:
        if int(card_number[:2]) in range(51, 56): 
            return "MASTERCARD\n"

        elif card_number[0] == "4": 
            return "VISA\n"

        return "INVALID\n"

    if card_length == 13 and card_number[0] == "4":
        return "VISA\n"

    return "INVALID\n"


def luhns_algorithm(card_number):
    alt_numbers_str = ""

    # Let's start by grabbing every alternative number, Multiplying by 2 and adding it to a new string:
    for i in range(len(card_number) - 2, -1, -2):
        alt_numbers_str += str(int(card_number[i]) * 2)
        # current_number = int(card_number[i]) * 2
        # alt_numbers_str += str(current_number)

    # I need a running sum going forward:
    running_sum = 0

    # Now we have our new string, let's add every number to our running sum
    for i in range(len(alt_numbers_str)):
        running_sum += int(alt_numbers_str[i])

    # Now to grab every number not added to the prior string, and add them to our running sum:
    for i in range(len(card_number) - 1, -1, -2):
        running_sum += int(card_number[i])

    # Finally we just need to check if our running sum total is divisible by 10:
    if running_sum % 10 == 0:
        return True
    return False


print(main())