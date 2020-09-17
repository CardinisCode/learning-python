import unittest
from readability import main, count_letters_in_input, count_words_in_input, count_sentences_in_input, calculate_coleman_liau_index
#, count_words_in_input, count_sentences_in_input, calculate_coleman_liau_index

class TestCountLetters(unittest.TestCase):
    def test_no_letters_given_returns_0(self):
        expected = 0
        user_input = ""
        
        actual = count_letters_in_input(user_input)

        self.assertEqual(actual, expected)


    def test_given_only_numbers_returns_0(self):
        expected = 0
        user_input = "20 99883"

        actual = count_letters_in_input(user_input)

        self.assertEqual(actual, expected)

    
    def test_given_5_letters_returns_5(self):
        expected = 5
        user_input = "Hello"

        actual = count_letters_in_input(user_input)

        self.assertEqual(actual, expected)


class TestWordCount(unittest.TestCase):
    def test_given_empty_string_returns_0(self):
        expected = 0
        user_input = ""

        actual = count_words_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_no_spaces_returns_1(self):
        expected = 1
        user_input = "Hello"

        actual = count_words_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_1_spaces_returns_2(self):
        expected = 2
        user_input = "Hello Johnny"

        actual = count_words_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_14_words_returns_14(self):
        expected = 14
        user_input = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"

        actual = count_words_in_input(user_input)
        
        self.assertEqual(actual, expected)


    
class TestSentence_count(unittest.TestCase):
    def test_given_no_punctuation_returns_0(self):
        expected = 0
        user_input = "Hello Johnny"

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_1_full_stop_returns_1(self):
        expected = 1
        user_input = "Hello Johnny."

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_1_question_mark_returns_1(self):
        expected = 1
        user_input = "How are you?"

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_1_exlamation_point_returns_1(self):
        expected = 1
        user_input = "Pleasure to meet you!"

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_2_full_stops_returns_2(self):
        expected = 2
        user_input = "Welcome Johnny. We're happy to have you."

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_a_full_stop_and_exclamation_point_returns_2(self):
        expected = 2
        user_input = "Welcome Johnny. We're happy to have you!"

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)

    def test_given_a_full_stop_and_exclamation_and_question_mark_returns_3(self):
        expected = 3
        user_input = "Hello Johnny. How are you? Glad to have you!"

        actual = count_sentences_in_input(user_input)

        self.assertEqual(actual, expected)


class TestColemanLiau_index(unittest.TestCase):
    def test_if_given_0_letters_returns_0(self):
        letter_count = 0
        word_count = 0
        sentence_count = 0
        expected = 0

        actual = calculate_coleman_liau_index(letter_count, word_count, sentence_count)

        self.assertEqual(actual, expected)

    def test_given_0_words_returns_0(self):
        letter_count = 0
        word_count = 0
        sentence_count = 0
        expected = 0

        actual = calculate_coleman_liau_index(letter_count, word_count, sentence_count)

        self.assertEqual(actual, expected)

    def test_given_0_sentences_returns_0(self):
        letter_count = 0
        word_count = 0
        sentence_count = 0
        expected = 0

        actual = calculate_coleman_liau_index(letter_count, word_count, sentence_count)

        self.assertEqual(actual, expected)

    def test_given_14words_65letters_4Sentences_returns_3(self):
        letter_count = 65
        word_count = 14
        sentence_count = 4
        expected = 3 

        actual = calculate_coleman_liau_index(letter_count, word_count, sentence_count)

        self.assertEqual(actual, expected)


class TestMain(unittest.TestCase):
    def test_given_empty_string_return_BeforeGrade1(self):
        expected = "Before Grade 1"
        user_input = ""

        actual = main(user_input)

        self.assertEqual(actual, expected)
    
    def test_given_basic_string_returns_BeforeGrade1(self):
        expected = "Before Grade 1"
        user_input =  "Hi Johnny"

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_1_string_returns_BeforeGrade1(self):
        expected = "Before Grade 1"
        user_input = "One fish. Two fish. Red fish. Blue fish."

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_2_string_returns_Grade_2(self):
        expected = "Grade 2"
        user_input = "Would you like them here or there? I would not like them here or there. I would not like them anywhere."

        actual = main(user_input)
        
        self.assertEqual(actual, expected)

    def test_given_grade_3_string_returns_Grade_3(self):
        expected = "Grade 3"
        user_input = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_5_string_returns_Grade_5(self):
        expected = "Grade 5"
        user_input = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_7_String_returns_Grade_7(self):
        expected = "Grade 7"
        user_input = "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_8_string_returns_Grade_8(self):
        expected = "Grade 8"
        user_input = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, and "what is the use of a book", thought Alice "without pictures or conversation?"'

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_9_string_returns_Grade_9(self):
        expected = "Grade 9"
        user_input = "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy."

        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_10_string_returns_Grade_10(self):
        expected = "Grade 10"
        user_input = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
        
        actual = main(user_input)

        self.assertEqual(actual, expected)

    def test_given_grade_16_plus_string_returns_Grade_16Plus(self):
        expected = "Grade 16+"
        user_input = "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."

        actual = main(user_input)

        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()