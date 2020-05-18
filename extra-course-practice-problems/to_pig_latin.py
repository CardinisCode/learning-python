#Pig Latin is a fictitious language. To translate a word into
#Pig Latin, you would take the consonants up until the first
#vowel, move them to the end, and add "ay" to the end.
#
#For example:
#
# pig -> igpay
# david -> avidday
# trash -> ashtray
# scram -> amscray
# translate -> anslatetray
#
#Write a function called to_pig_latin. to_pig_latin will take
#as input a single word, and return the Pig Latin version of
#the word.
#
#For the purposes of this problem, only a, e, i, o, and u are
#vowels: y is a consonant. You may assume that the word will 
#start with at least one consonant, that the letters to move to
#the end will always be the consonants until the first vowel,
#and that the string will be all lower-case.

import unittest
#Write your function here!

def find_first_vowel(word):
    vowels = ["a", "e", "i", "o", "u"]

    for index in range(0, len(word)):
        char =  word[index]
        if char in vowels:
            return index

def to_pig_latin(word):
    first_vowel = find_first_vowel(word)
 
    before_vowel = word[:first_vowel]
    after_vowel = word[first_vowel:]

    return after_vowel + before_vowel + "ay"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same results as in the examples above.
print(to_pig_latin("pig"))
print(to_pig_latin("david"))
print(to_pig_latin("trash"))
print(to_pig_latin("scram"))
print(to_pig_latin("translate"))


class TestToPigLatinTranslate(unittest.TestCase):
    def test_to_pig_latin_translation_with_pig(self):
        print("-----------------------------")
        expected = "igpay"
        actual = to_pig_latin("pig")

        self.assertEqual(expected, actual)


    def test_to_pig_latin_translation_with_david(self):
        print("-----------------------------")
        expected = "avidday"
        actual = to_pig_latin("david")

        self.assertEqual(expected, actual)


    def test_to_pig_latin_translation_with_2_consonants(self):
        print("-----------------------------")
        expected = "ashtray"
        actual = to_pig_latin("trash")

        self.assertEqual(expected, actual)

    def test_to_pig_latin_translation_with_3_consonants(self):
        print("-----------------------------")
        expected = "amscray"
        actual = to_pig_latin("scram")

        self.assertEqual(expected, actual)

    
    def test_to_pig_latin_translation_with_long_word(self):
        print("-----------------------------")
        expected = "anslatetray"
        actual = to_pig_latin("translate")

        self.assertEqual(expected, actual)





if __name__ == "__main__":
    unittest.main()

