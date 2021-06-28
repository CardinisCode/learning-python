import unittest
from main import Solution


class SolutionMethods(unittest.TestCase):
    ##
    ## /!\ Unit Tests are optional but highly recommended /!\
    def test_run(self):
      solution = Solution()
      expected_output = "Sun-2016 Fri-2020 Sat-2021 Sun-2022 Fri-2026 Sat-2027 Sat-2032 Sun-2033 Fri-2037 Sat-2038 Sun-2039 Fri-2043 Sun-2044 Fri-2048 Sat-2049 Sun-2050 Fri-2054 Sat-2055 Sat-2060 Sun-2061 Fri-2065"
      self.assertEqual(solution.run("23-10"), expected_output)

if __name__ == "__main__":
	unittest.main()
