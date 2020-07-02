#Write a function called check_value. check_value should
#take as input two parameters: a dictionary and a string.
#Both the keys and the values in the dictionary will be
#strings. The string parameter will be the key to look up in
#the dictionary.
#
#check_value should look up the string in the dictionary and
#get its value. Its current value will always be a string;
#however, check_value should try to convert it to an integer
#and a float, then return a message indicating the success
#of those conversions:
#
# - If the key is not found in the dictionary, check_value
#   should return the string: "Not found!"
# - If the value corresponding to the key can be converted
#   to an integer, check_value should return the string:
#   "Integer!"
# - Otherwise, if the value corresponding to the key can be
#   converted to a float, check_value should return the
#   string: "Float!"
# - Otherwise, check_value should return the string:
#   "String!"
#
#You do not need to check for any other types. We suggest
#using error handling to try to convert the values to the
#corresponding data types.
#
#For example, given this dictionary:
#
# d = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}
#
#Here are some calls and their results:
#
# - check_value(d, "k1") -> "Float!"
# - check_value(d, "k2") -> "Integer!"
# - check_value(d, "k3") -> "String!"
# - check_value(d, "k4") -> "String!"
# - check_value(d, "k5") -> "Not found!"
#
#Hint: The error that arises when trying to convert a
#string to a type it can't convert to (e.g. "ABC" to a
#float) is a ValueError. The error that arises when
#trying to access a key that doesn't exist in a
#dictionary is a KeyError.

import unittest

#Write your function here!
# My 2nd pass at this challenge: 
def check_value(myDict, search_string):
    try:
        current_string = myDict[search_string]
        current_string = int(current_string)
        return "Integer!"
        
        
    except KeyError:
        return "Not found!"
    
    except ValueError:
        try:
            current_string = float(current_string)
            return "Float!"
        except: 
            return "String!"




# My first pass at this challenge: 

# def check_value(dictionary, search_key):
    # try: 
    #     current_value = dictionary[search_key]
    #     current_value = float(current_value)
    #     current_value_as_string = str(current_value)
    #     last_digit = current_value_as_string[len(current_value_as_string)-1]

    #     if last_digit == "0":
    #         return "Integer!"

    #     else:
    #         return "Float!"

    # except KeyError:
    #     return "Not found!"
    
    # except ValueError:
    #     return "String!"




#The lines below will test your code. Their output should
#match the examples above.
d = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}


print("k1:", check_value(d, "k1"))
print("k2:", check_value(d, "k2"))
print("k3:", check_value(d, "k3"))
print("k4:", check_value(d, "k4"))
print("k5:", check_value(d, "k5"))


class TestCheckValue(unittest.TestCase):
    dictionary = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}

    def test_for_key_not_found_in_dictionary(self):
        expected = "Not found!"
        actual = check_value(self.dictionary, "k5")
        self.assertEqual(expected, actual)

    
    def test_key_is_a_string(self):
        expected = "String!"
        actual = check_value(self.dictionary, "k4")
        self.assertEqual(expected, actual)


    def test_value_if_integer(self):
        expected = "Integer!"
        actual = check_value(self.dictionary, "k2")
        self.assertEqual(expected, actual)

    
    def test_value_if_float(self):
        expected = "Float!"
        actual = check_value(self.dictionary, "k1")
        self.assertEqual(expected, actual)







if __name__ == "__main__":
    unittest.main()