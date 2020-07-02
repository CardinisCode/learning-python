#Write a function called inverted_sort. inverted_ should
#take as input a list of integers, and return as output a
#list with the integers sorted from HIGHEST to LOWEST.
#
#You may use any sorting algorithm you want: bubble, merge,
#insertion, selection, a new sort that you learned on your
#own, or even one you created yourself. You may use loops,
#or you may use recursion.
#
#You may not use Python's native list sort or reverse 
#methods; you must write your own sort.

import unittest
#Write your function here!

# Using a inverted/reverse Selection sort: 

def inverted_sort(integers):
    for i in range(0, len(integers)):
        current_value = integers[i]
        highest_value = current_value
        highest_value_index = i

        for j in range(i, len(integers)):
            comparison_value = integers[j]

            if comparison_value > highest_value:
                highest_value = comparison_value
                highest_value_index = j

        swap = current_value
        integers[i] = highest_value
        integers[highest_value_index] = swap
        
    return integers



#The code below will test your function. Feel free to
#modify it. As written originally, it will print the list:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))

# class TestInvertedSort(unittest.TestCase):
    
    # def test_empty_list_returns_empty_list(self):
    #     print("---------------------------")
    #     unsorted_list = []
    #     expected = []

    #     actual = inverted_sort(unsorted_list)

    #     self.assertEqual(expected, actual)        


    # def test_sorting_a_list_from_highest_down_to_lowest_value(self):
    #     unsorted_list = [5, 4, 10, 1, 7, 2, 3, 6, 8, 9]
    #     expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    #     actual = inverted_sort(unsorted_list)

    #     self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()


