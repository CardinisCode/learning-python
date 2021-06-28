import unittest
from main import Solution

class SolutionMethods(unittest.TestCase):
	##
	## /!\ Unit Tests are optional but highly recommended /!\
	##
	# First Example
	##
	#def test_example(self):
	#	self.assertEqual("this is an example", "this is an example")

	##
	# Second Example
	##
    def test_run_first_test(self):
        solution = Solution()
        expected_output = "2,1,0"
        self.assertEqual(solution.run(3, 3, [3, 1, 1]), expected_output)

    def test_run_second_test(self):
        solution = Solution()
        expected_output = "3,0,4"
        self.assertEqual(solution.run(5, 3, [4, 4, 5]), expected_output)

if __name__ == "__main__":
    unittest.main()
