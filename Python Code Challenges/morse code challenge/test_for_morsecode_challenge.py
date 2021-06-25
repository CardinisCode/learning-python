import unittest
from morse_code_challenge_code import Solution

class SolutionMethods(unittest.TestCase):
    ## /!\ Unit Tests are optional but highly recommended /!\

    def test_empty_textToTranslate_when_true(self):
        solution = Solution()
        expected_output = "Invalid Morse Code Or Spacing"
        self.assertEqual(solution.run(True, ""), expected_output)
        
    def test_empty_textToTranslate_when_false(self):
        solution = Solution()
        expected_output = "Invalid Morse Code Or Spacing"

        self.assertEqual(solution.run(False, ""), expected_output)	
        
    def test_given_the_return_morse_translation(self):
        solution = Solution()
        expected_output = "- .... ."

        self.assertEqual(solution.run(False, "the"), expected_output)

    def test_given_two_english_words_return_morse(self):
        solution = Solution()
        expected_output = "- .... .   .-- .. --.. .- .-. -.."

        self.assertEqual(solution.run(False, "the wizard"), expected_output)

    def test_given_three_english_words_return_morse(self):
        solution = Solution()
        expected_output = "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--"

        self.assertEqual(solution.run(False, "the wizard quickly"), expected_output)

    def test_given_one_morse_word_return_english(self):
        solution = Solution()
        expected_output = "the"

        self.assertEqual(solution.run(True, "- .... ."), expected_output)

    def test_given_two_morse_words_return_english(self):
        solution = Solution()
        expected_output = "the wizard"

        self.assertEqual(solution.run(True, "- .... .   .-- .. --.. .- .-. -.."), expected_output)

    def test_given_three_morse_words_return_english(self):
        solution = Solution()
        expected_output = "the wizard quickly"

        self.assertEqual(solution.run(True, "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--"), expected_output)
 
	
	
	##
	## /!\ Unit Tests are optional but highly recommended /!\
	##
	# First Example
	##
	#def test_example(self):
	#	self.assertEqual("this is an example", "this is an example")

	##
	# Second Example
	##
	#def test_run(self):
	#	solution = Solution()
	#	self.assertEqual(solution.run(parameters), "expected_output")

if __name__ == "__main__":
	unittest.main()
