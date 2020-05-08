import unittest

#Write a function called count_positive_evens. This function
#should take as input a list of integers, and return as
#output a single integer. The number the function returns
#should be the count of numbers from the list that were both
#positive and even.
#
#For example:
#
# count_positive_evens([5, 7, 9, 8, -1, -2, -3]) -> 1
# count_positive_evens([2, 4, 6, 8, 10, 12, 15]) -> 6
# count_positive_evens([-2, -4, -6, -8, -10, 1]) -> 0
#
#0 should be not counted as a positive even number.
#
#Hint: Remember, even numbers are numbers that have a
#remainder of 0 when divided by 2.


#Write your function here!
def count_positive_evens(my_integer_list):
    running_count = 0
    for integer in my_integer_list:
        if integer >= 2 and integer % 2 == 0:
            running_count += 1

    return running_count






class TestCountPositiveEvens(unittest.TestCase):
    def test_no_evens_found(self):
        expected = 0
        actual = count_positive_evens([-2, -4, -6, -8, -10, 1])
        self.assertEqual(expected, actual)

    def test_found_evens_in_list(self):
        expected = 1
        actual = count_positive_evens([5, 7, 9, 8, -1, -2, -3])
        self.assertEqual(expected, actual)





#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.



print("#1:", count_positive_evens([5, 7, 9, 8, -1, -2, -3]))
print("#2:", count_positive_evens([2, 4, 6, 8, 10, 12, 15]))
print("#3:", count_positive_evens([-2, -4, -6, -8, -10, 1]))















if __name__ == "__main__":
    unittest.main()