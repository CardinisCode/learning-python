#Remember that Fibonacci's sequence is a sequence of numbers
#where every number is the sum of the previous two numbers.
#
#Joynernacci numbers are similar to Fibonacci numbers, but
#with two differences:
#
# - Fibonacci numbers are famous, Joynernacci numbers are
#   not (yet).
# - In Joynernacci numbers, even-indexed numbers are the
#   sum of the previous two numbers, while odd-indexed
#   numbers are the absolute value of the difference
#   between the previous two numbers.
#
#For example: the Joynernacci sequence starts with 1 and 1
#as the numbers at index 1 and 2. 3 is an odd index, so
#the third number would be 0 (1 - 1 = 0). 4 is an even
#index, so the fourth number would be 1 (0 + 1). 5 is an
#odd index, so the fifth number would be 1 (1 - 0). And
#so on.
#
#The first several Joynernacci numbers (and their indices)
#are thus:
#
# 1  1  0  1  1  2  1  3  2  5  3  8  5 13  8 21 13 34 21
# 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
#
#Write a function called joynernacci that returns the nth
#Joynernacci number. For example:
#
# joynernacci(5) -> 1
# joynernacci(12) -> 8
#
#We recommend implementing joynernacci recursively, but it
#is not required.

import unittest
#Write your code here!

# Solved with iteration: 
def joynernacci_iterative(number):
    joynernacci_sequence = [0, 1, 1]

    for index in range(3, number +1):
        two_steps_back = joynernacci_sequence[index-2]
        one_step_back = joynernacci_sequence[index-1] 

        if index % 2 == 0:
            current_number = one_step_back + two_steps_back
        elif index % 2 == 1:
            current_number = abs(two_steps_back - one_step_back)
        joynernacci_sequence.append(current_number)

        if index == number:
            return joynernacci_sequence[index]

# With Recursion (1st pass):
# def joynernacci_recursive(index):
#     if index == 1 or index == 2:
#         return 1
    
#     elif index % 2 == 0:
#         return joynernacci_recursive(index -1) + joynernacci_recursive(index -2)

#     elif index % 2 == 1:
#         return abs(joynernacci_recursive(index -1) - joynernacci_recursive(index -2))
        

# My second attempt at this challenge seems to be shorter:
def joynernacci(n):
    if n <= 1:
        return n
    elif n % 2 == 1:
        return abs(joynernacci(n -1) - joynernacci(n -2))
    elif n % 2 == 0:
        return joynernacci(n -1) + joynernacci(n -2)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 1, then 8
print(joynernacci_iterative(3))
print(joynernacci_iterative(5))
print(joynernacci_iterative(12))

print(joynernacci(3))
print(joynernacci(5))
print(joynernacci(12))
print(joynernacci(19))


class TestJoyneracci(unittest.TestCase):
    def test_third_index_returns_0_with_iteration(self):
        print("----------------------------------")
        expected = 0
        actual = joynernacci_iterative(3)

        self.assertEqual(expected, actual)

    
    def test_fifth_index_returns_one_with_iteration(self):
        print("----------------------------------")
        expected = 1
        actual = joynernacci_iterative(5)

        self.assertEqual(expected, actual) 


    def test_twelth_index_returns_eight_with_iteration(self):
        print("----------------------------------")
        expected = 8
        actual = joynernacci_iterative(12)

        self.assertEqual(expected, actual)  


    def test_third_index_returns_0_with_recursion(self):
        print("----------------------------------")
        expected = 0
        actual = joynernacci(3)

        self.assertEqual(expected, actual)

    
    def test_fifth_index_returns_one_with_recursion(self):
        print("----------------------------------")
        expected = 1
        actual = joynernacci(5)

        self.assertEqual(expected, actual) 


    def test_twelth_index_returns_eight_with_recursion(self):
        print("----------------------------------")
        expected = 8
        actual = joynernacci(12)

        self.assertEqual(expected, actual)     


    def test_ninetheenth_index_returns_21_with_recursion(self):
        expected = 21
        actual = joynernacci(19) 

        self.assertEqual(expected, actual) 


if __name__ == "__main__":
    unittest.main()

