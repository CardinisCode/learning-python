# Task #1: Find no. of vowels

class Solution:
    vowels = ["a", "e", "i", "o", "u"]

    def calculate_vowels_and_consonants(self, input_str):
        vowel_count = 0
        consonant_count = 0

        for letter in input_str:
            if letter.lower() in self.vowels:
                vowel_count += 1
            elif letter.isalpha():
                consonant_count += 1

        return "%s %s" % (vowel_count, consonant_count)

    def case_reverse(self, input_str):
        new_str = ""
        for letter in input_str:
            if letter.isupper():
                new_str += letter.lower()
            else: 
                new_str += letter.upper()
        
        split_list = new_str.split()
        return ' '.join(split_list[::-1])

    def dash_words(self, input_str):
        split_list = input_str.split()
        return "-".join(split_list)

    def add_pv_before_vowels(self, input_str):
        updated_str = ""
        for letter in input_str:
            if letter in self.vowels:
                updated_str += "pv" + letter
            else:
                updated_str += letter

        return input_str
