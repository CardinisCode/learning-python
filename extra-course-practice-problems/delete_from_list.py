#Write a function called delete_from_list. delete_from_list
#should have two parameters: a list of strings and a list of
#integers.
#
#The list of integers represents the indices of the items to
#delete from the list of strings. Delete the items from the
#list of strings, and return the resulting list.
#
#For example:
#
# delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5])
#
#...would return the list ["c", "d"]. "a" is at index 0, "b" at 1,
#"e" at 4, and "f" at 5, so they would all be removed.
#
#Remember, though, as you delete items from the list, the
#indices of the remaining items will change. For example, once
#you delete "a" at index 0, the list will be ["b", "c", "d",
#"e", "f"], and now "c" will be at index 1 instead of "b". The
#list of indices to delete gives those values' _original_
#positions.
#
#You may assume that there are no duplicate items in the list
#of strings.
#
#There is more than one way to do this, so if you find yourself
#struggling with one way, try a different one!

import unittest
#Write your function here!
def delete_from_list(current_list, indices):
    updated_list = []
    if len(indices) == 0:
        return current_list

    for index in range(0, len(current_list)):
        current_element = current_list[index]
        if not index in indices:
            updated_list.append(current_element) 

    return updated_list


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#['c', 'd']
#['a', 'b', 'e', 'f']
# print(delete_from_list(["a", "b", "c", "d", "e", "f"], [0, 1, 4, 5])) ----> ['c', 'd']
# print(delete_from_list(["a", "b", "c", "d", "e", "f"], [2, 3])) ---> ['a', 'b', 'e', 'f']

class TestDeletingItems(unittest.TestCase):
    # current_list = ["a", "b", "c", "d", "e", "f"]
    current_list = ["insight", "dispensate", "Layton", "airdrop", "dogtrot", "councilmen"]

    def test_no_items_to_delete_returns_original_list(self):
        print("----------------------------------------")
        expected = ["insight", "dispensate", "Layton", "airdrop", "dogtrot", "councilmen"]
        actual = delete_from_list(self.current_list, [])

        self.assertEqual(expected, actual)


    def test_deletes_1_item_from_original_list(self):
        print("----------------------------------------")
        expected = ["insight", "Layton", "airdrop", "dogtrot", "councilmen"]
        actual = delete_from_list(self.current_list, [1])

        self.assertEqual(expected, actual)   

    
    def test_deletes_2_items_from_original_list(self):
        print("----------------------------------------")
        expected = ["insight", "dispensate", "dogtrot", "councilmen"]
        actual = delete_from_list(self.current_list, [2, 3])

        self.assertEqual(expected, actual) 


    def test_deletes_4_items_from_original_list(self):
        print("----------------------------------------")
        expected = ["Layton", "airdrop"]
        actual = delete_from_list(self.current_list, [0, 1, 4, 5])

        self.assertEqual(expected, actual)     




if __name__ == "__main__":
    unittest.main()