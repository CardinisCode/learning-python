

# from cs50 import get_string

def main(user_input):
    #user_input = get_string("Text: ")
    letter_count = count_letters_in_input(user_input)
    word_count = count_words_in_input(user_input)
    sentence_count = count_sentences_in_input(user_input)
    print("Letter count:", letter_count, "Word Count:", word_count, "Sentences:", sentence_count)
    index = calculate_coleman_liau_index(letter_count, word_count, sentence_count)
    print("The index:", index)

    if index < 1: 
        return "Before Grade 1"
    elif index >= 16:
        return "Grade 16+"
    else:
        return "Grade " + str(index)


def count_letters_in_input(user_input):
    running_letter_count = 0.0
    for letter in user_input:
        if ord(letter) in range(65, 91) or ord(letter) in range(97, 123):
            running_letter_count += 1
    
    return running_letter_count


def count_words_in_input(user_input):
    word_count = 0.0

    if user_input == "":
        return word_count

    for i in range(len(user_input)):
        if ord(user_input[i]) == 32:
            if ord(user_input[i - 1]) in range(65, 91) or ord(user_input[i - 1]) in range(97, 123):
                word_count += 1
            else: 
                continue

        if ord(user_input[i]) in [33, 34, 44, 46, 63]:
            if ord(user_input[i - 1]) in range(65, 91) or ord(user_input[i - 1]) in range(97, 123):
                word_count += 1
            else:
                continue 
    
    # If valid punctuation (Specifically: ".", "?", "!", '"") is found in the text, 
    # we can just return our running word_count as it is:
    if "." in user_input or "!" in user_input or "?" in user_input or '"' in user_input:
        return word_count
    # Otherwise we can assume there are just letters and spaces, so we can add +1:
    return word_count + 1


def count_sentences_in_input(user_input):
    sentence_count = 0.0
    for i in range(len(user_input)):
        if ord(user_input[i]) in [33, 46, 63]:
            sentence_count += 1
    
    return sentence_count


def calculate_coleman_liau_index(letter_count, word_count, sentence_count):
    # Before we go do mathematical operations, let's first make sure we aren't dealing with any 0 values:
    if letter_count == 0 or word_count == 0 or sentence_count == 0: 
        return 0

    # L = the Avg no. of letters per 100 words
    L = letter_count / word_count * 100

    # S = The Avg. no. of sentences per 100 words
    S = sentence_count / word_count * 100

    # index = 0.0588 * L - 0.296 * S - 15.8
    index = 0.0588 * L - 0.296 * S - 15.8

    print("L:", L, "S:", S, "Index:", index)
    return round(index)

if __name__=="__main__":
    user_input = input("Text: ")
    print(main(user_input))
