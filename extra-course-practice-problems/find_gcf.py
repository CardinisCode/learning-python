#The Greatest Common Factor (GCF) of two numbers is the
#largest number that divides evenly into those two
#numbers. For example, the Greatest Common Factor of 48
#and 18 is 6. 6 is the largest number that divides evenly
#into 48 (48 / 6 = 8) and 18 (18 / 6 = 3).
#
#Write a function called find_gcf. find_gcf should have
#two parameters, both integers. find_gcf should return
#the greatest common factor of those two numbers.
#
#For example:
#
# find_gcf(48, 18) -> 6
# find_gcf(21, 7) -> 7
# find_gcf(47, 17) -> 1
#
#If one number is a multiple of the other, the greatest
#common factor is the smaller number (e.g. 21 and 7). If
#the numbers have no common factors, then their greatest
#common factor is 1 (e.g. 47 and 17).

import unittest
#Write your function here!
def find_gcf(integer_1, integer_2):
    greatest_common_factor = 1
    larger_integer = 0

    if integer_1 >= integer_2:
        larger_integer = integer_1
    else:
        larger_integer = integer_2

    for i in range(1, larger_integer +1):
        integer1_division_by_i = str(integer_1/i)
        integer2_division_by_i = str(integer_2/i)

        integer1_division_split = integer1_division_by_i.split(".")
        integer2_division_split = integer2_division_by_i.split(".")

        if integer1_division_split[1] == "0" and integer2_division_split[1] == "0":
            greatest_common_factor = i

    return greatest_common_factor


#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.

print(find_gcf(48, 18))
print(find_gcf(21, 7))
print(find_gcf(47, 17))



class TestFindGCF(unittest.TestCase):
    def test_finds_1_gcf(self):
        print("------------------------------")
        expected = 1
        actual = find_gcf(47, 17)

        self.assertEqual(expected, actual)


    def test_finds_6_is_gcf(self):
        print("------------------------------")
        expected = 6
        actual = find_gcf(48, 18)

        self.assertEqual(expected, actual)

    
    def test_finds_7_is_greatest_common_factor(self):
        print("------------------------------")
        expected = 7
        actual = find_gcf(21, 7)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()