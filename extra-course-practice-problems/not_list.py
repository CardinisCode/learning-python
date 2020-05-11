#Write a function called not_list. not_list should have two
#parameters: a list of booleans and a list of integers.
#
#The list of integers will represent indices for the list of
#booleans. not_list should switch the values of all the
#booleans located at those indices.
#
#For example:
#
# bool_list = [True, False, False]
# index_list = [0, 2]
# not_list(bool_list, index_list) -> [False, False, True]
#
#After calling not_list, the booleans at indices 0 and 2
#have been switched.
#
#Note that it may be the case that the same index is present
#in the second twice. If this happens, you should switch the
#boolean at that index twice. For example:
#
# bool_list = [True, False, False]
# index_list = [0, 2, 2]
# not_list(bool_list, index_list) -> [False, False, False]
#
#2 is in index_list twice, so the boolean at index 2 is
#switched twice: False to True, then True back to False.
#
#Hint: Remember you can change a list in place! You don't
#need to create a new list. a_list[1] = False, for example,
#changes the item in a_list at index 1 to False.

# HINT TO SELF: 
# Dont switch the items around - think rather of a light switch! 
# When you "Flip" True -> It becomes False
# When you "Flip" False -> It becomes True
# Like Binary where theres only 0 and 1, Likewise, something can only be True or False. 


import unittest

#Write your function here!
def not_list(booleans, indices):
    for index in indices:
        if booleans[index] == True:
            booleans[index] = False
        else:
            booleans[index] = True
    
    return booleans


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[False, False, True]
#[False, False, False]
print(not_list([True, False, False], [0, 2]))
print()
print(not_list([True, False, False], [0, 2, 2]))



class TestNotList(unittest.TestCase):

    def test_switch_with_1_index(self):
        expected = [False, False, True]
        actual = not_list([True, False, True], [0])
        self.assertEqual(expected, actual)

    def test_switch_with_2_indices(self):
        expected = [False, True, True]
        actual = not_list([True, False, True], [0, 1])
        self.assertEqual(expected, actual)

    def test_switch_with_3_indices(self):
        expected = [False, False, False]
        actual = not_list([True, False, False], [0, 2, 2])
        self.assertEqual(expected, actual)





if __name__ == "__main__":
    unittest.main()