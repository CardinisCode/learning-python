import unittest
from main import Solution

class SolutionMethods(unittest.TestCase):
	## /!\ Unit Tests are optional but highly recommended /!\

    def test_given_two_letters_return_query(self):
        solution = Solution()
        expected_output = "1 1::Pa::pA::ppvA"
        self.assertEqual(solution.run("pA"), expected_output)

    def test_given_string_return_actual_query(self):
        solution = Solution()
        expected_output = "2 5::P IS tHiS::ThIs-is-p::ThpvIs pvis p"
        self.assertEqual(solution.run("ThIs is p"), expected_output)   

if __name__ == "__main__":
	unittest.main()