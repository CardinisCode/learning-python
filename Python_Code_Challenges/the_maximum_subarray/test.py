import unittest
from main import Solution


class SolutionMethods(unittest.TestCase):

    def test_given_mixed_array_return_6(self):
        solution = Solution()
        expected_output = 6
        self.assertEqual(solution.run([-2,1,-3,4,-1,2,1,-5,4]), expected_output)

if __name__ == "__main__":
	unittest.main()
