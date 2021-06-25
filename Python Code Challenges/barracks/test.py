import unittest
from main import Solution


class SolutionMethods(unittest.TestCase):
    def test_given_zero_n_returns_zero(self):
        solution = Solution()
        self.assertEqual(solution.run(0, 1), 0)

    def test_given_zero_k_returns_zero(self):
        solution = Solution()
        self.assertEqual(solution.run(1, 0), 0)

    def test_given_one_k_return_1(self):
        solution = Solution()
        self.assertEqual(solution.run(5, 1), 1)

    def test_given_3n_and_2k_returns_4(self):
        solution = Solution()
        self.assertEqual(solution.run(3, 2), 4)

    def test_given_5n_and_2k_returns_8(self):
        solution = Solution()
        self.assertEqual(solution.run(5, 2), 8)      




if __name__ == "__main__":
    unittest.main()