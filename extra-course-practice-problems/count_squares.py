#Write a function called count_squares. This function
#should take as input a list of integers, and return as
#output a single integer. The number the function returns
#should be the number of perfect squares it found in the
#list of integers. You may assume every number in the list
#is between 1 and 1 billion (1,000,000,000).
#
#For example:
#
# count_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) -> 3
# count_squares([1, 4, 9, 16, 25, 36, 49, 64]) -> 8
# count_squares([2, 3, 5, 6, 7, 8, 10, 11]) -> 0
#
#For this problem, 0 is considered a square.
#
#Hint: Don't get caught up trying to "remember" how to
#calculate if a number is a square: we've never done it
#before, but we've covered all the tools you need to do it
#in one of several different ways.

import unittest
import math
print()
#Write your function here!
def count_squares(number_list):
    number_of_squares = 0

    for i in number_list:
        number_sqrt = math.sqrt(i)
        number_sqrt = str(number_sqrt)
        number_split_by_dot = number_sqrt.split(".")

        if number_split_by_dot[1] == "0":
            number_of_squares += 1


    return number_of_squares

#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.
# print(count_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(count_squares([1, 4, 9, 16, 25, 36, 49, 64]))
#print(count_squares([2, 3, 5, 6, 7, 8, 10, 11]))


class TestCountSquares(unittest.TestCase):
    def test_no_squares_found(self):
        expected = 0
        actual = count_squares([2, 3, 5, 6, 7, 8, 10, 11])

        self.assertEqual(expected, actual)


    def test_found_3_perfect_squares(self):
        expected = 3
        actual = count_squares([1, 2, 3, 4, 5, 6, 7, 8, 9])

        self.assertEqual(expected, actual)
    

    def test_found_8_perfect_squares(self):
        expected = 8
        actual = count_squares([1, 4, 9, 16, 25, 36, 49, 64])

        self.assertEqual(expected, actual)


    def test_found_3_perfect_squares_longer_values(self):
        num_list = [883652530, 634215344, 118831801, 923916888, 926147742]
        expected = 1
        actual = count_squares(num_list)

        self.assertEqual(expected, actual)

    def test_0_in_list_found_to_be_perfect_square(self):
        expected = 1
        actual = count_squares([0, 2, 3, 5, 6, 7, 8, 10, 11])

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()