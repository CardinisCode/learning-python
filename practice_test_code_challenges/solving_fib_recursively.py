import unittest

def solve_fib_recursively(index):
    if index == 0 or index == 1:
        return 1
    else:
        return solve_fib_recursively(index -1) + solve_fib_recursively(index -2)


class TestSolveFibRecursively(unittest.TestCase):
    def test_index_3_returns_3(self):
        expected = 3
        actual = solve_fib_recursively(3)
        self.assertEqual(expected, actual)

    def test_index_5_returns_8(self):
        expected = 8
        actual = solve_fib_recursively(5)
        self.assertEqual(expected, actual)

    def test_index_7_returns_21(self):
        expected = 21
        actual = solve_fib_recursively(7)
        self.assertEqual(expected, actual)            



if __name__ == "__main__":
    unittest.main()