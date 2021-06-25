import unittest
from main import Solution

class SolutionMethods(unittest.TestCase):
    ##
    ## /!\ Unit Tests are optional but highly recommended /!\
    ##
    # First Example
    ##
    #def test_example(self):
    #   self.assertEqual("this is an example", "this is an example")

    ##
    # Second Example
    # def test_zero_returns_false(self):
    #     solution = Solution()
    #     expected_output = False
    #     self.assertEqual(solution.run(0), expected_output)

    def test_given_4_return_true(self):
        solution = Solution()
        expected_output = True
        self.assertEqual(solution.run(4), expected_output)

    def test_given_6_return_true(self):
        solution = Solution()
        expected_output = True
        self.assertEqual(solution.run(6), expected_output)




if __name__ == "__main__":
    unittest.main()
