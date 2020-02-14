import unittest

#Write a function called "load_file" that accepts one 
#parameter: a filename. The function should open the
#file and return the contents.#
#
# X If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# X Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.

def load_file(fileName):
    inputFile = open(fileName, "r")
    contents = inputFile.readline()
    inputFile.close()
    return return_content_in_type(contents)

def return_content_in_type(contents):
    try:
        return int(contents)
    except:
        pass

    try: 
        return float(contents)
    except: 
        return str(contents)
        
    
class TestReturnContentInType(unittest.TestCase):
    def test_should_return_int_when_given_int(self):
        self.assertEqual(type(return_content_in_type("1")), int)

    def test_should_return_float_when_given_float(self):
        self.assertEqual(type(return_content_in_type("1.1")), float)

    def test_should_return_string_if_actually_string(self):
        self.assertEqual(type(return_content_in_type("hello.world")), str)


if __name__ == '__main__':
    unittest.main()