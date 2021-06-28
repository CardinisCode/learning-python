class Solution:

    def run(self, n):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        #
        n_in_roman_alphabet = ""

        roman_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        while n > 0:
            for number, roman in roman_dict.items():
                if n >= number:
                    n_in_roman_alphabet += roman
                    n -= number
                    break

        return n_in_roman_alphabet