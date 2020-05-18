#Write a function called copy_pointlessly. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#copy_pointlessly should copy the contents of input_file into
#output_file, but make the following changes:
#
# - Replace all instances of the letter A (either capital or
#   lower case) with the at sign, @
# - Replace all instances of the letter M (either capital or
#   lower case) with the character sequence |\/|
# - Replace all instances of the letter W with the character
#   sequence \/\/
# - Replace all instances of the letter O (either capital
#   or lower case) with the numeral 0
# - Alternate the case for every remaining letter in the
#   string (hint: the_string.swapcase() returns the string
#   with the case of all letters swapped)
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# This is some text. Woo text yay!
#
#Then to_upper_copy would write this text to output_file (the
#first parameter):
#
# tHIS IS S0|\/|E TEXT. \/\/00 TEXT Y@Y!
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.


#Write your function here!
def copy_pointlessly(output_file, input_file):
    opening_output_file = open(output_file, "w")
    opening_input_file = open(input_file, "r")
    input_file_contents = opening_input_file.readlines()
    opening_input_file.close()

    for index in range(0, len(input_file_contents)):
        line_to_write = ""
        current_line = input_file_contents[index]
        for char in current_line:
            ordinal_char = ord(char)
            if not ordinal_char >= 65 and not ordinal_char <= 90 \
            or not ordinal_char >= 97 and not ordinal_char <= 122:
                line_to_write += char + " "
                
            if ordinal_char == 65 or ordinal_char == 97:
                line_to_write += "@"
            elif ordinal_char == 77 or ordinal_char == 109:
                line_to_write += "|\/|"
            elif ordinal_char == 87 or ordinal_char == 119:
                line_to_write += "\/\/"
            elif ordinal_char == 79 or ordinal_char == 111:
                line_to_write += "0"
            else:
                line_to_write += char.swapcase()

        if index == len(input_file_contents) -1:
            line_to_write = line_to_write.rstrip()
            line_to_write += "\n"
        
        opening_output_file.write(line_to_write)


    opening_output_file.close()

#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, anOutputFile.txt should have the text:
#TEST @N @, TEST @N @
#TEST @N 0, TEST @N 0
#TEST @N |\/|, TEST @N |\/|
#TEST @ \/\/, TEST @ \/\/

# TEST @N @, TEST @N @
# TEST @N 0, TEST @N 0
# TEST @N |\/|, TEST @N |\/|
# TEST @ \/\/, TEST @ \/\/





incoming_file = "extra-course-practice-problems/copy_pointlessly.inputfile.txt"
output_file = "extra-course-practice-problems/copy_pointlessly.outputfile.txt"

copy_pointlessly(output_file, incoming_file)
print("Done running! Check anOutputFile.txt for the result.")

