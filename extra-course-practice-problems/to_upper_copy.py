#Write a function called to_upper_copy. This function should
#take two parameters, both strings. The first string is the
#filename of a file to which to write (output_file), and the
#second string is the filename of a file from which to read
#(input_file).
#
#to_upper_copy should copy the contents of input_file into
#output_file, capitalizing all letters (not just all words,
#each individual letter). You may use the .upper() method
#from the string class.
#
#For example, if these were the contents of input_file (the
#second parameter):
#
# This is some text. Yay text.
#
#Then to_upper_copy would write this text to output_file (the
#first parameter):
#
# THIS IS SOME TEXT. YAY TEXT.
#
#No other characters should be changed. Note that the file
#to be copied will have multiple lines of text.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.


#Write your function here!
def to_upper_copy(new_file, prev_file):
    incoming_file = open(prev_file, "r")
    outgoing_file = open(new_file, "w")
    incoming_file_contents = incoming_file.readlines()
    incoming_file.close()

    for line in incoming_file_contents:
        print("Before editing:", line)
        updated_line = ""
        for char in line:
            ordinal_value = ord(char)
            if ordinal_value >= 97 and ordinal_value <= 122:
                updated_letter = chr(ordinal_value - 32)
                print(char, "Vs", updated_letter)
                updated_line += updated_letter
            else:
                updated_line += char
        print("After editting:", updated_line)
        print(updated_line, end="", file=outgoing_file)




#The code below will test your function. You can find the two
#files it references in the drop-down in the top left.

my_input_file = "extra-course-practice-problems/my_input_file.txt"
my_output_file = "extra-course-practice-problems/my_new_output_file.txt"

to_upper_copy(my_output_file, my_input_file)
print("Done running! Check anOutputFile.txt for the result.")

