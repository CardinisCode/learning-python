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

# My second pass at this challenge: 
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

# This sort starts from the start of the list and compares the current value to every other value in the list. 
# when it finds a value higher than itself, the 2 values swop places in the list. 
# This allows me to modify the list without messing with the size of the list and thereby avoiding errors. 


# My first pass at this challenge: 

# def process_selection_sort(numbers_to_sort, sorted_numbers):
#     current_integer = numbers_to_sort[0]
#     highest_integer = current_integer
#     highest_index = 0

#     for comparison_index in range(1, len(numbers_to_sort)):
#         comparison_integer = int(numbers_to_sort[comparison_index])
        
#         if comparison_integer > highest_integer:
#             highest_integer = comparison_integer
#             highest_index = comparison_index

#     sorted_numbers.append(highest_integer)
#     del numbers_to_sort[highest_index]

#     return (numbers_to_sort, sorted_numbers)


# #Write your function here!
# def inverted_sort(numbers_to_sort):
#     sorted_numbers = []
#     running_count = 0
#     while len(numbers_to_sort) >= 1:
#         process_selection_sort(numbers_to_sort, sorted_numbers)
#         running_count +=1

#     return sorted_numbers

#The code below will test your function. Feel free to
#modify it. As written originally, it will print the list:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9]))


class TestInvertedSort(unittest.TestCase):
    def test_sorted_from_highest_to_lowest(self):
        print('----------------------------------------------')
        expected = [10, 5, 4]
        actual = inverted_sort([5, 4, 10])
        self.assertEqual(expected, actual)


    def test_sorted_from_highest_to_lowest_full_Version(self):
        print('----------------------------------------------')
        expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        actual = inverted_sort([5, 4, 10, 1, 7, 2, 3, 6, 8, 9])
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()