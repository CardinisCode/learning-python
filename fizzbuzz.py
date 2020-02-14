# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print "Fizz" instead of the number and for 
# the multiples of five print "Buzz". and a number that is a
# multiple of of 3 and 5 return "FizzBuzz"

import unittest

def fizz_buzz(number):
    result = ""

    if number % 3 == 0:
        result += "Fizz"

    if number % 5 == 0:
        result += "Buzz"

    if len(result) > 0:
        return result
    
    return str(number)

class TestFizzBuss(unittest.TestCase):
    def test_when_given_number_one_should_return_string_one(self):
        self.assertEquals(fizz_buzz(1), "1")

    def test_when_given_number_two_should_return_string_two(self):
        self.assertEquals(fizz_buzz(2), "2")

    def test_when_given_three_should_return_fizz(self):
        self.assertEquals(fizz_buzz(3), "Fizz")

    def test_when_given_six_return_fizz(self):
        self.assertEquals(fizz_buzz(6), "Fizz")

    def test_when_given_9_return_fizz(self):
        self.assertEquals(fizz_buzz(9), "Fizz")
    
    def test_when_given_5_return_buzz(self):
        self.assertEquals(fizz_buzz(5), "Buzz")

    def test_when_given_10_return_buzz(self):
        self.assertEquals(fizz_buzz(10), "Buzz")

    def test_when_given_15_return_fizzbuzz(self):
        self.assertEquals(fizz_buzz(15), "FizzBuzz")

    def test_when_given_30_return_fizzBuzz(self):
        self.assertEquals(fizz_buzz(30), "FizzBuzz")

    def test_when_given_45_return_FizzBuzz(self):
        self.assertEquals(fizz_buzz(45), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()