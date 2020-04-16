#A common problem in academic settings is plagiarism
#detection. Fortunately, software can make this pretty easy!
#
#In this problem, you'll be given two files with text in
#them. Write a function called check_plagiarism with two
#parameters, each representing a filename. The function
#should find if there are any instances of 5 or more
#consecutive words appearing in both files. If there are,
#return the longest such string of words (in terms of number
#of words, not length of the string). If there are not,
#return the boolean False.
#
#For simplicity, the files will be lower-case text and spaces
#only: there will be no punctuation, upper-case text, or
#line breaks.
#
#We've given you three files to experiment with. file_1.txt
#and file_2.txt share a series of 5 words: we would expect
#check_plagiarism("file_1.txt", "file_2.txt") to return the
#string "if i go crazy then". file_1.txt and file_3.txt
#share two series of 5 words, and one series of 11 words:
#we would expect check_plagiarism("file_1.txt", "file_3.txt")
#to return the string "i left my body lying somewhere in the
#sands of time". file_2.txt and file_3.txt do not share any
#text, so we would expect check_plagiarism("file_2.txt",
#"file_3.txt") to return the boolean False.
#
#Be careful: there are a lot of ways to do this problem, but
#some would be massively time- or memory-intensive. If you
#get a MemoryError, it means that your solution requires
#storing too much in memory for the code to ever run to
#completion. If you get a message that says "KILLED", it
#means your solution takes too long to run.

import unittest

"""
    check_plagiarism 
        this loads files and turns them into lists
        calls compare

    compare
        takes two lists and compares them

    when testing
    def test_blah
        compare([], [])


    def test_blahq
        compare([1,2], [1])
"""

def unpack_a_files_contents_into_list(filename):
    current_file = open(filename, "r")
    file_contents = current_file.read()
    current_file.close()
    # current_file_contents_in_a_list = file_contents.split(" ")
    # return current_file_contents_in_a_list
    return file_contents


#Add your code here!
def check_plagiarism(file1, file2):
    first_file_contents = unpack_a_files_contents_into_list(file1)
    second_file_contents = unpack_a_files_contents_into_list(file2)

    desired_string = comparing_two_files_for_plagiarism(first_file_contents, second_file_contents)

    return desired_string

def comparing_two_files_for_plagiarism(first_file_contents, second_file_contents):
    if first_file_contents == second_file_contents:
        return first_file_contents

    elif first_file_contents in second_file_contents:
        return first_file_contents

    elif second_file_contents in first_file_contents:
        return second_file_contents

    first_list = first_file_contents.split(" ")
    second_list = second_file_contents.split(" ")
    search_string = ""
    longest_string = ""

    for i in range(0, len(first_list)):
        # current_word = first_list[i]
        for j in range(0, len(second_list)):
            current_index = 0
            while first_list[i + current_index] == second_list[j + current_index] \
             and current_index + i < len(first_list) and current_index + j < len(second_list):
                if current_index == (len(first_list) -1):
                    search_string += " " + first_list[i + current_index]
                    break
                else: 
                    search_string += " " + first_list[i + current_index]
                    current_index += 1

            if search_string > longest_string: 
                longest_string = search_string
                search_string = ""
    
    if len(longest_string) >=1:
        return longest_string.lstrip()
     
    return False

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#if i go crazy then
#i left my body lying somewhere in the sands of time
#False

class CheckPlagiarism(unittest.TestCase):
    def test_both_files_are_indentical(self):
        # file_contents = "i dont care if i go crazy then one two three four five switch crazy go i if care dont i five four three two one and switch"
        file_1_contents = "i took a walk around the world"
        file_2_contents = file_1_contents

        actual = comparing_two_files_for_plagiarism(file_1_contents, file_2_contents)

        self.assertEqual("i took a walk around the world", actual)

    def test_both_files_do_not_match(self):
        contents_1 = "happy dogs live free today"
        contents_2 = "there are unicorns somewhere out there"

        actual = comparing_two_files_for_plagiarism(contents_1, contents_2)
        
        self.assertEqual(False, actual)

    def test_first_five_words_match(self):
        contents_1 = "happy dogs live free today"
        contents_2 = contents_1 + " and forever"

        actual = comparing_two_files_for_plagiarism(contents_1, contents_2)

        self.assertEqual(contents_1, actual)

    def test_if_last_five_words_match(self):
        contents_1 = "happy dogs live free today"
        contents_2 = "we shall forever have " + contents_1

        actual = comparing_two_files_for_plagiarism(contents_1, contents_2)

        self.assertEqual(contents_1, actual) 

    def test_if_middle_five_words_match(self):
        contents_1 = "happy dogs live free today"
        contents_2 = "we shall forever have " + contents_1 + " and forever more"

        actual = comparing_two_files_for_plagiarism(contents_1, contents_2)

        self.assertEqual(contents_1, actual) 

    def test_if_both_file_contents_share_a_common_search_string(self):
        print("test_if_both_file_contents_share_a_common_search_string")
        print("-------------------------------------------------------")
        contents_1 = "my delightful happy dogs live free today in our yard"
        contents_2 = "Our happy dogs live free today in our grand garden"
        expected = "happy dogs live free today in our"

        actual = comparing_two_files_for_plagiarism(contents_1, contents_2)

        print("-------------------------------------------------------")
        self.assertEqual(expected, actual)

    def test_compare_file_one_with_file_two(self):
        self.assertEqual("if i go crazy then", check_plagiarism("file_1.txt", "file_2.txt"))

    def test_compare_file_one_with_file_three(self):
        self.assertEqual("i left my body lying somewhere in the sands of time", 
        check_plagiarism("file_1.txt", "file_3.txt"))

    def test_compare_file_two_with_file_three(self):
        self.assertEqual(False, check_plagiarism("file_2.txt", "file_3.txt"))





if __name__ == "__main__":
    unittest.main()