# Challenge: String Theory (Hackajob)

# For a given sentence p, return the following:

# -   how many vowels and consonants p has, we do not count Y and W as vowels
# -   p with reversed words order and reversed cases (any upper-case letter will be lower-case and every lower-case letter will be upper-case)
# -   every word in p separated by a dash ('-')
# -   p with inserted string "pv" before any vowel in the sentence

# Take into consideration that p can have any kind of characters.

# You have to return a string containing the above queries, separated by double colon ("::")

# INPUT
# string p

# OUTPUT
# string combined_queries

# This is how combined_queries should look like:

# nr_vowels nr_consonants::reversed_p_with_reversed_cases::every-word-in-p::p_wpvith_inspvertpved_strpving_pv
# EXAMPLE
# Input
# "ThIs is p"

# Output
# 2 5::P IS tHiS::ThIs-is-p::ThpvIs pvis p


import unittest
from main import Solution


class TestStringTheory(unittest.TestCase):
    solution = Solution()

    def test_given_p_returns_0_1(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("p"), "0 1")

    def test_given_two_consonants_returns_0_2(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("pp"), "0 2")   

    def test_given_a_return_1_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("a"), "1 0")   

    def test_given_e_return_1_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("e"), "1 0") 

    def test_given_i_return_1_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("i"), "1 0") 
    
    def test_given_o_return_1_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("o"), "1 0") 
    
    def test_given_u_return_1_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("u"), "1 0") 

    def test_given_aa_return_2_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("aa"), "2 0")  

    def test_given_aaa_return_3_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("aaa"), "3 0")  

    def test_given_aaaa_return_4_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("aaaa"), "4 0") 
    
    def test_given_A_return_1_0(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("A"), "1 0")   
    
    def test_given_a__b_return_1_1(self):
        self.assertEqual(self.solution.calculate_vowels_and_consonants("a b"), "1 1") 

    def test_case_reverse_given_a_letter_return_opposite_case(self):
        test_cases = [
            ['p', 'P'],
            ['q', 'Q'],
            ['t', 'T'], 
            ['pp', 'PP'], 
            ['P', 'p'], 
            ['Q', 'q'],
            ['T', 't'], 
            ['PP', 'pp'],
            ['pP', 'Pp'],
            ['p p', 'P P']
        ]

        for phrase, expected in test_cases:
            with self.subTest(i = phrase):
                self.assertEqual(self.solution.case_reverse(phrase), expected)

    def test_case_reverse_given_multiple_words_return_reverse_order_of_words(self):
        test_cases = [
            ['a b', 'B A'],
            ['aa bb', 'BB AA'],
            ['aaa bbb', 'BBB AAA'], 
            ['the way', 'WAY THE'],
            ['is the way', 'WAY THE IS'],
            ['this is the way', 'WAY THE IS THIS']
        ]

        for phrase, expected in test_cases:
            with self.subTest(i = phrase):
                self.assertEqual(self.solution.case_reverse(phrase), expected)


# -   every word in p separated by a dash ('-')
    def test_dash_words_add_dash_between_words(self):
        test_cases = [
            ['this', 'this'],
            ['this is', 'this-is'],
            ['the way', 'the-way'],
            ['is the', 'is-the'], 
            ['this is the', 'this-is-the'],
            ['this is the way', 'this-is-the-way']
        ]

        for phrase, expected in test_cases:
            with self.subTest(i = phrase):
                self.assertEqual(self.solution.dash_words(phrase), expected)

# -   p with inserted string "pv" before any vowel in the sentence
    def test_add_pv_before_vowels_given_vowels_add_pv(self):
        test_cases = [
            ['p', 'p'],
            ['a', 'pva'],
            ['e', 'pve'],
            ['i', 'pvi'],
            ['o', 'pvo'], 
            ['u', 'pvu'],
            ['aa', 'pvapva']
        ]

        for phrase, expected in test_cases:
            with self.subTest(i = phrase):
                self.assertEqual(self.solution.add_pv_before_vowels(phrase), expected)


if __name__ == "__main__":
    unittest.main()  