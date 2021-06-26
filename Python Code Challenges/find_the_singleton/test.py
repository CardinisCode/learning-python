import unittest
from main import Solution


class SolutionMethods(unittest.TestCase):
    def test_given_single_number_return_number(self):
        solution = Solution()
        expected_output = 1
        self.assertEqual(solution.run([1]), expected_output)

    def test_given_three_students_return_single_student(self):
        solution = Solution()
        expected_output = 2
        self.assertEqual(solution.run([1, 2, 1]), expected_output)

    def test_given_five_students_return_single_student(self):
        solution = Solution()
        expected_output = 5
        self.assertEqual(solution.run([2,4,5,4,2]), expected_output)

if __name__ == "__main__":
    unittest.main()