#Write a function called count_capital_consonants. This
#function should take as input a string, and return as output
#a single integer. The number the function returns should be
#the count of characters from the string that were capital
#consonants. For this problem, consider Y a consonant.
#
#For example:
#
# count_capital_consonants("Georgia Tech") -> 2
# count_capital_consonants("GEORGIA TECH") -> 6
# count_capital_consonants("gEOrgIA tEch") -> 0

import unittest
#Write your function here!
def count_capital_consonants(string):
    running_count = 0
    vowel_ordinals = [65, 69, 73, 79, 85]
    for letter in string:
        ordinal_value = ord(letter)
        if ordinal_value >= 66 and ordinal_value <= 90 and not ordinal_value in vowel_ordinals:
            running_count += 1

    return running_count


#The lines below will test your code. Feel free to modify
#them. If your code is working properly, these will print
#the same output as shown above in the examples.
print(count_capital_consonants("Georgia Tech"))
print(count_capital_consonants("GEORGIA TECH"))
print(count_capital_consonants("gEOrgIA tEch"))

class TestCountCapitalConsonants(unittest.TestCase):
    def test_found_no_capital_consanants(self):
        expected = 0
        actual = count_capital_consonants("gEOrgIA tEch")

        self.assertEqual(expected, actual)

    def test_found_two_capital_consonants(self):
        expected = 2
        actual = count_capital_consonants("Georgia Tech")

        self.assertEqual(expected, actual)

    def test_found_six_capital_consonants(self):
        expected = 6
        actual = count_capital_consonants("GEORGIA TECH")

        self.assertEqual(expected, actual)    



if __name__ == "__main__":
    unittest.main()
