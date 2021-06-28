import unittest
from main import Solution

class SolutionMethods(unittest.TestCase):
    ##
    ## /!\ Unit Tests are optional but highly recommended /!\

    def test_given_1_return_I(self):
        solution = Solution()
        expected_output = "I"
        self.assertEqual(solution.run(1), expected_output)

    def test_given_2_return_II(self):
        solution = Solution()
        expected_output = "II"
        self.assertEqual(solution.run(2), expected_output)

    def test_given_3_return_III(self):
        solution = Solution()
        expected_output = "III"
        self.assertEqual(solution.run(3), expected_output)

    def test_given_4_return_IV(self):
        solution = Solution()
        expected_output = "IV"
        self.assertEqual(solution.run(4), expected_output)

    def test_given_5_return_V(self):
        solution = Solution()
        expected_output = "V"
        self.assertEqual(solution.run(5), expected_output)
    
    def test_given_6_return_VI(self):
        solution = Solution()
        expected_output = "VI"
        self.assertEqual(solution.run(6), expected_output)

    def test_given_8_return_VIII(self):
        solution = Solution()
        expected_output = "VIII"
        self.assertEqual(solution.run(8), expected_output)
    
    def test_given_9_return_IX(self):
        solution = Solution()
        expected_output = "IX"
        self.assertEqual(solution.run(9), expected_output)

    def test_given_10_return_X(self):
        solution = Solution()
        expected_output = "X"
        self.assertEqual(solution.run(10), expected_output)
    
    def test_given_15_return_XV(self):
        solution = Solution()
        expected_output = "XV"
        self.assertEqual(solution.run(15), expected_output)
    
    def test_given_19_return_XIX(self):
        solution = Solution()
        expected_output = "XIX"
        self.assertEqual(solution.run(19), expected_output)
    
    def test_given_49_return_IL(self):
        solution = Solution()
        expected_output = "XLIX"
        self.assertEqual(solution.run(49), expected_output)

    def test_given_50_return_L(self):
        solution = Solution()
        expected_output = "L"
        self.assertEqual(solution.run(50), expected_output)

    def test_given_99_return_IC(self):
        solution = Solution()
        expected_output = "XCIX"
        self.assertEqual(solution.run(99), expected_output)

    def test_given_100_return_C(self):
        solution = Solution()
        expected_output = "C"
        self.assertEqual(solution.run(100), expected_output)

    def test_given_400_return_CD(self):
        solution = Solution()
        expected_output = "CD"
        self.assertEqual(solution.run(400), expected_output)
    
    def test_given_500_return_D(self):
        solution = Solution()
        expected_output = "D"
        self.assertEqual(solution.run(500), expected_output)

    def test_given_900_return_CM(self):
        solution = Solution()
        expected_output = "CM"
        self.assertEqual(solution.run(900), expected_output)

    def test_given_1000_return_M(self):
        solution = Solution()
        expected_output = "M"
        self.assertEqual(solution.run(1000), expected_output)

    def test_given_1954_return_MCMLIV(self):
        solution = Solution()
        expected_output = "MCMLIV"
        self.assertEqual(solution.run(1954), expected_output)

    def test_given_1990_return_MCMXC(self):
        solution = Solution()
        expected_output = "MCMXC"
        self.assertEqual(solution.run(1990), expected_output)

    def test_given_2014_return_MMXIV(self):
        solution = Solution()
        expected_output = "MMXIV"
        self.assertEqual(solution.run(2014), expected_output)


if __name__ == "__main__":
	unittest.main()
