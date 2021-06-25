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
    def test_run(self):
    	solution = Solution()
    	self.assertEqual(solution.run(parameters), "expected_output")


if __name__ == "__main__":
	unittest.main()
