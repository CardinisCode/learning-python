#Write a function called garble_this. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#garble_this should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all vowels with the next vowel in order (a -> e,
#   e -> i, i -> o, o -> u.
# - Replace all consonants with the next consonant, b -> c,
#   c -> d, d -> f, etc.) Replace z with b.
# - Leave everything else in the file unchanged.
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# this is some text. woo text yay!
#
#Then garble_this would write this text to output_file (the
#first parameter):
#
# vjot ot tuni viyv. xuu viyv zez!
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text. You may assume
#the input file will be all lower-case.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.
#
#Hints: 
# - Remember, you can increment a letter by 1 by finding its
#   ordinal, adding one, and converting it back to a letter.
#   If a_char is a character, then chr(ord(a_char) + 1) would
#   give you the next character.
# - You might also use dictionaries to establish what each
#   letter gets replaced by.
# - In ASCII, the character that comes after "z" is "{". You
#   want to replace "z" with "a", though.
# - Consider writing multiple functions! You could (but you
#   do not have to) write a dedicated function called
#   change_letter that handles a single letter, then
#   repeatedly call it to handle the file as a whole.


#Write your function here!
def garble_this(outputfile, inputfile):
    incoming_file = open(inputfile, "r")
    outgoing_file = open(outputfile, "w")
    incoming_file_contents = incoming_file.readlines()
    incoming_file.close()

    vowels = ["a", "e", "i", "o", "u"]
    for line in incoming_file_contents:
        updated_line = ""
        for char in line:
            ordinal_value = ord(char)
            if char in vowels:
                updated_char = replace_vowel_with_next_vowel_in_order(char)
                updated_line += updated_char

            elif ordinal_value >= 98 and ordinal_value <= 122:
                updated_char = replace_consonant_with_next_consonant_in_order(char)
                # print("Our updated consonant:", updated_char)
                updated_line += updated_char
            
            else:
                updated_line += char
        updated_line = updated_line.rstrip()
        updated_line += "\n"
        outgoing_file.write(updated_line)


    outgoing_file.close()


def replace_vowel_with_next_vowel_in_order(letter):
    vowels = ["a", "e", "i", "o", "u"]
    for index in range(0, len(vowels)):
        current_vowel = vowels[index]
        if letter == current_vowel:
            return vowels[(index +1) % 5]


def replace_consonant_with_next_consonant_in_order(letter):
    ordinal_value = ord(letter)
    vowel_ordinals = [97, 101, 105, 111, 117]
    next_letter_ord = ordinal_value + 1

    if ordinal_value == 122:
        return "b"

    elif next_letter_ord in vowel_ordinals:
        return chr(ordinal_value + 2)

    else: 
        return chr(next_letter_ord)




    
    






# Before editing, the input file contains this:
# abcdefg
# hijklmn
# opqrstu
# vwxyz.!
# 1234567
# 890&$%#



#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#ecdfigh
#joklmnp
#uqrstva
#wxyzb.!
#1234567
#890&$%#


# ecdfigh
# joklmnp
# uqrstva
# wxyza.!
# 1234567
# 890&$%#





input_file = "extra-course-practice-problems/garble_this.inputfile.txt"
output_file = "extra-course-practice-problems/garble_this.outputfile.txt"

garble_this(output_file, input_file)
print("Done running! Check anOutputFile.txt for the result.")

