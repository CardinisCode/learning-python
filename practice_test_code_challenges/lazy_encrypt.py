#Write a function called lazy_encrypt. This function should
#take three parameters: two strings and a dictionary. The
#first string is the filename of a file to which to write
#(output_file), the second string is the filename of a file
#from which to read (input_file), and the dictionary is a
#mapping of character:character pairs you should use to
#"encrypt" the contents of the input file before writing it
#to the output file.
#
#lazy_encrypt should go through every character in the
#input file. If the character is a key in the dictionary,
#then lazy_encrypt should write the value associated with
#that key to the output file. If it is not a key, it should
#write the original character.
#
#For example, imagine if the input file contained the text
#"Hello world", and the dictionary was {"e": "o", "o": "a"}.
#Then, lazy_encrypt would write "Holla warld" to the output
#file. Each letter is only substituted once. You should not
#ignore case: if the input file had instead contained the
#text "HELLO WORLD", then nothing should have been changed
#because the keys in the dictionary are lower-case.
#
#We've included two files for you to test on: anInputFile.txt
#and anOutputFile.txt. The test code below will copy the text
#from the first file to the second. Feel free to modify the
#first to test different setups.
import unittest

#Below is my first pass at this challenge. 
# def lazy_encrypt(output_file, input_file, vowels_dict):
#     incoming_file = open(input_file, "r")
#     outgoing_file = open(output_file, "w")
#     incoming_file_contents = incoming_file.readlines()
#     incoming_file.close()
#     print()

#     updated_line = ""
#     for index in range(0, len(incoming_file_contents)):
#         current_line = incoming_file_contents[index]
        
#         for character in current_line:
#             if character in vowels_dict.keys():
#                 updated_line += vowels_dict[character]
#             else:
#                 updated_line += character
#         if index == len(incoming_file_contents) -1:
#             updated_line = updated_line.rstrip()
#             updated_line += "\n"
#             outgoing_file.write(updated_line)

#     outgoing_file.close()

# My Second pass (weeks later):
def lazy_encrypt(output_file, input_file, encryption_dict):
    incoming_file = open(input_file, "r")
    outgoing_file = open(output_file, "w")
    incoming_file_contents = incoming_file.readlines()
    incoming_file.close()

    for line in incoming_file_contents:
        updated_line = ""
        for char in line: 
            if char in encryption_dict.keys():
                updated_letter = encryption_dict[char]
                updated_line += updated_letter
            else:
                updated_line += char
        outgoing_file.write(updated_line)

    outgoing_file.close()

# Much simpler and shorter :D 

# Me:
# Now I want to run a test to actually read the output file I'm writing to
# to see if it matches the expected contents of the output file.
# To make the test work, I have created this function below to actually return  the contents of the outputfile
# -> I call this function in my test: 
# test_lazy_encrypt_function(self)


def return_output_file_contents(output_file):
    file = open(output_file, "r")
    output_file_contents = file.read()
    output_file_contents = output_file_contents.rstrip()
    file.close()

    return output_file_contents

#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, the contents of anOutputFile.txt after running
#will be:
#Horo is a protty simplo mossago ta oncrypt
#Whon it's oncryptod, it will laak difforont


input_file = "lazy_encrypt_inputfile.txt"
output_file = "lazy_encrypt_outputfile.txt"
encryption_dict = {"e": "o", "o": "a"}

lazy_encrypt(output_file, input_file, encryption_dict)
print("Done running! Check anOutputFile.txt for the result.")

class TestLazyEncryp(unittest.TestCase):
    def test_lazy_encrypt_function(self):
        output_file = "lazy_encrypt_outputfile.txt"
        expect = "Horo is a protty simplo mossago ta oncrypt\nWhon it's oncryptod, it will laak difforont"
        actual = return_output_file_contents(output_file)

        self.assertEqual(expect, actual)



if __name__ == "__main__":
    unittest.main()