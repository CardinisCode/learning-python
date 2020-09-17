import unittest
from mario import print_pyramid

class MarioTests(unittest.TestCase):
    def test_main_given_1_prints_a_pyramid_size_1(self):
        expected = "#  #"
        actual = print_pyramid(1)

        self.assertEqual(actual, expected)

    def test_print_pyramid_given_2_prints_a_pyramid_size_2(self):
        expected = " #  #\n##  ##"
        actual = print_pyramid(2)

        self.assertEqual(actual, expected)
    
    def test_print_pyramid_given_3_prints_a_pyramid_size_3(self):
        expected = "  #  #\n ##  ##\n###  ###"
        actual = print_pyramid(3)

        self.assertEqual(actual, expected)

    def test_main_successfully_prints_pyramid_given_pyramid_size_5(self):
        expected = "    #  #\n   ##  ##\n  ###  ###\n ####  ####\n#####  #####"
        actual = print_pyramid(5)

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()