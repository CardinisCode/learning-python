import unittest

def unpacking_file_contents(filename):
    current_file = open(filename, "r")
    file_contents = current_file.readlines()
    current_file.close()

    return file_contents

def creating_dictionary_for_baby_names(file_contents):

    datebase_of_baby_names = {}
    for line in file_contents:
        current_line = line.rstrip()
        line_split = current_line.split(",")
        baby_name = line_split[0]
        occurrences = int(line_split[1])
        baby_gender = line_split[2]

        if not baby_name in datebase_of_baby_names:
            datebase_of_baby_names[baby_name] = {
                'Boy': 0, 
                'Girl': 0,
                'Total': 0,
            }
        if baby_gender == "Girl":
            datebase_of_baby_names[baby_name]['Girl'] += occurrences
        else: 
            datebase_of_baby_names[baby_name]['Boy'] += occurrences
        datebase_of_baby_names[baby_name]['Total'] += occurrences

    return datebase_of_baby_names

def find_total_baby_names_in_database(baby_names_database):
    total_baby_names = 0
    for name in baby_names_database.keys():
        if baby_names_database[name]['Girl'] > 0 and baby_names_database[name]['Boy'] > 0:
            total_baby_names += 2
        else: 
            total_baby_names += 1

    return total_baby_names


def find_total_births(baby_names_database):
    total_occurences = 0
    for name in baby_names_database.keys():
        occurances = baby_names_database[name]['Total']
        total_occurences += occurances

    return total_occurences


def find_number_of_boy_names_beginning_with_Z(baby_names_database):
    total_number_of_boys = 0
    for name in baby_names_database.keys():
        first_letter = name[0]
        if first_letter == "Z" and baby_names_database[name]['Boy'] > 0:
                total_number_of_boys += 1

    return total_number_of_boys


def find_most_common_girl_name_beginning_with_Q(baby_names_database):
    most_common_girl_name = ""
    most_occurences = 0
    for name in baby_names_database.keys():
        first_letter = name[0]
        if first_letter == "Q" and baby_names_database[name]['Girl'] > 0:
            current_name_occurences = baby_names_database[name]['Girl']
            if current_name_occurences > most_occurences:
                most_occurences = current_name_occurences
                most_common_girl_name = name

    return most_common_girl_name


def find_number_of_babies_starting_and_ending_with_a_vowel(baby_names_database):
    total_number_of_babies = 0
    vowels_first_letters = ["A", "E", "I", "O", "U"]
    vowels_last_letters = ["a", "e", "i", "o", "u"]
    for name in baby_names_database.keys():
        first_letter = name[0]
        last_letter = name[len(name)-1]
        total_occurences = baby_names_database[name]['Total']
        if first_letter in vowels_first_letters and last_letter in vowels_last_letters:
            total_number_of_babies += total_occurences

    return total_number_of_babies

def build_dictionary_from_A_to_Z(baby_names_database):
    baby_names_from_A_to_Z = {}

    for name in baby_names_database.keys():
        first_letter = name[0]
        occurances = baby_names_database[name]['Total']
        if not first_letter in baby_names_from_A_to_Z:
            baby_names_from_A_to_Z[first_letter] = 0
        baby_names_from_A_to_Z[first_letter] += occurances

    return baby_names_from_A_to_Z

def find_least_common_first_letter(baby_names_A_to_Z):
    least_common_letter = "A"
    least_number_of_births = baby_names_A_to_Z[least_common_letter]

    for letter in baby_names_A_to_Z.keys():
        number_of_births = baby_names_A_to_Z[letter]
        if number_of_births < least_number_of_births:
            least_number_of_births = number_of_births
            least_common_letter = letter

    return least_common_letter

def find_quantity_babies_with_least_common_letter(baby_names_A_to_Z, least_common_first_letter):
    number_babies = baby_names_A_to_Z[least_common_first_letter]
    return number_babies

def find_most_common_first_letter(baby_names_A_to_Z):
    most_common_letter = "A"
    most_number_of_births = baby_names_A_to_Z[most_common_letter]

    for letter in baby_names_A_to_Z.keys():
        number_of_births = baby_names_A_to_Z[letter]
        if number_of_births > most_number_of_births:
            most_number_of_births = number_of_births
            most_common_letter = letter

    return most_common_letter


def find_number_babies_most_common_first_letter(baby_names_A_to_Z, most_common_first_letter):
    number_of_babies = baby_names_A_to_Z[most_common_first_letter]
    return number_of_babies


def find_most_common_name(baby_names_database, file_contents):
    most_common_name = ""
    number_of_babies = 0

    for index in range(1, len(file_contents)):
        current_line = file_contents[index].rstrip()
        line_split = current_line.split(",")
        name = line_split[0]
        if index == 1: 
            most_common_name = name
            number_of_babies = baby_names_database[name]['Total']

    for name in baby_names_database.keys():
        current_number_of_babies = baby_names_database[name]['Total']
        if current_number_of_babies > number_of_babies:
            most_common_name = name
            number_of_babies = current_number_of_babies

    return (most_common_name, number_of_babies)


def build_dictionary_of_names_and_abs_differences(second_baby_names_database):
    names_and_abs_differences = {}
    for name in second_baby_names_database:
        number_of_boys = second_baby_names_database[name]['Boy']
        number_of_girls = second_baby_names_database[name]['Girl']
        abs_difference = 0
        
        if number_of_boys >= 1 and number_of_girls >= 1:
            abs_difference = abs(number_of_boys - number_of_girls)
            if not name in names_and_abs_differences.keys():
                names_and_abs_differences[name] = 0
            names_and_abs_differences[name] = abs_difference

    return names_and_abs_differences


def find_name_with_lowest_abs_difference(dictionary):
    name_with_lowest_abs_diff = ""
    lowest_abs_difference = None

    for name in dictionary.keys():
        abs_difference = dictionary[name]
        print("Name:", name, "abs_difference:", abs_difference, type(abs_difference))
        if lowest_abs_difference == None:
            lowest_abs_difference = abs_difference
            name_with_lowest_abs_diff = name
        
        elif abs_difference < lowest_abs_difference:
            lowest_abs_difference = abs_difference
            name_with_lowest_abs_diff = name

    return (name_with_lowest_abs_diff, lowest_abs_difference)

file_contents = unpacking_file_contents("samplesubset.csv")
file_contents_2 = unpacking_file_contents("samplesubset2.csv")

baby_names_database = creating_dictionary_for_baby_names(file_contents)
second_baby_names_database = creating_dictionary_for_baby_names(file_contents_2)
# print(baby_names_database)
total_baby_names = find_total_baby_names_in_database(baby_names_database)
total_births = find_total_births(baby_names_database)
number_of_boys_names_beginning_with_Z = find_number_of_boy_names_beginning_with_Z(baby_names_database)
most_common_girl_name_beginning_with_Q = find_most_common_girl_name_beginning_with_Q(baby_names_database)
number_of_babies_with_names_which_start_and_end_with_a_vowel = find_number_of_babies_starting_and_ending_with_a_vowel(baby_names_database)

baby_names_A_to_Z = build_dictionary_from_A_to_Z(baby_names_database)
least_common_first_letter = find_least_common_first_letter(baby_names_A_to_Z)
number_babies_with_least_common_letter =find_quantity_babies_with_least_common_letter(baby_names_A_to_Z, least_common_first_letter)
most_common_first_letter = find_most_common_first_letter(baby_names_A_to_Z)
number_babies_with_most_common_letter = find_number_babies_most_common_first_letter(baby_names_A_to_Z, most_common_first_letter)
most_common_name = find_most_common_name(baby_names_database, file_contents)[0]
quantity_people_with_most_common_name = find_most_common_name(baby_names_database, file_contents)[1]
dict_baby_names_with_abs_difference = build_dictionary_of_names_and_abs_differences(second_baby_names_database)
name_with_lowest_abs_difference = find_name_with_lowest_abs_difference(dict_baby_names_with_abs_difference)[0]




print()
print("Question 1: How many total names are listed in the database?")
print("Expected Answer #1 Using subset:", total_baby_names)
print("Expected Answer #1 Using their data: 15790")
print()
print()
print("Question 2: How many total births are covered by the names in the database?")
print(total_births)
print("Expected Answer #2 Using subset: 364646")
print("Expected Answer #2 Using their file: 7030332")
print()
print()
print("Question 3: How many different boys' names are there that begin with the letter Z? (Count the names, not the people.)")
print(number_of_boys_names_beginning_with_Z)
print("Expected Answer #3 Using subset: 2")
print("Expected Answer #3 Using their file: 159")
print()
print("Question 4: What is the most common girl's name that begins with the letter Q?")
print("Answer #4 using samplesubset:", most_common_girl_name_beginning_with_Q)
print("Answer #4 using their file: Quinn")
print()
print("Question #5: How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?")
print(number_of_babies_with_names_which_start_and_end_with_a_vowel)
print("Answer #5 using samplesubset: 143411")
print("Answer #5 using their file: 672960")
print()
print("Question #6: What letter is the least common first letter of a baby's name (in terms of number of babies with names starting with that letter, not number of names)?")
print("Answer #6 using samplesubset:", least_common_first_letter)
print("Answer #6 using their file: U")
print()
print()
print("Question 7: How many babies were born with names starting with that least-common letter?")
print("Answer #7 using subset:", number_babies_with_least_common_letter)
print("Answer #7 using their file: 6283")
print()
print()
print("Question 8: What letter is the most common first letter of a baby's name (in terms of number of babies with names starting with that letter, not number of names)?")
print("Answer #8:", most_common_first_letter)
print("Answer #8 using their file: A")
print()
print()
print("Question #9: How many babies were born with names starting with that most-common letter")
print("Answer #9 using sampleset: 76126")
print("Answer #9 using their file: 983627")

print()
print()
# By default, the Social Security Administration's data separates out names by gender. 
# For example, Jamie is listed separately for girls and for boys. 
# If you were to remove this separation, 
# what would be the most common name in the 2010s regardless of gender?
print("Question #10: By default, the Social Security Administration's data separates out names by gender. For example, Jamie is listed separately for girls and for boys. If you were to remove this separation, what would be the most common name in the 2010s regardless of gender?")
print("Answer #10 using samplesubset:", most_common_name)
print("Answer #10 using their file: Isabella")
print()
print()
print("Question #11: How many people would have that name?")
print("Answer #11 using samplesubset:", quantity_people_with_most_common_name)
print("Answer #11 using their file: 42623")
print()
print()
# What name that is used for both genders has the smallest difference 
# (in which gender holds the name most frequently)? 
# In case of a tie, enter any one of the correct answers.
print("Question 12: What name that is used for both genders has the smallest difference in which gender holds the name most frequently? In case of a tie, enter any one of the correct answers.")
print("Answer 12 using samplesubset:", name_with_lowest_abs_difference)
print("Answer 12 using their file: Kylin")



class CheckPlagiarism(unittest.TestCase):
    def test_find_total_number_of_baby_names(self):
        actual = find_total_baby_names_in_database(baby_names_database)
        self.assertEqual(13, actual)


    def test_total_births_in_database(self):
        actual = find_total_births(baby_names_database)
        self.assertEqual(477367, actual)


    def test_boy_names_beginning_with_Z(self):
        actual = find_number_of_boy_names_beginning_with_Z(baby_names_database)
        self.assertEqual(2, actual)


    def test_most_common_girl_name_with_Q(self):
        actual = find_most_common_girl_name_beginning_with_Q(baby_names_database)
        self.assertEqual("Queen", actual)


    def test_number_of_names_starting_and_ending_with_vowels(self):
        actual = find_number_of_babies_starting_and_ending_with_a_vowel(baby_names_database)
        self.assertEqual(143411, actual)


    def test_least_common_letter(self):
        actual = least_common_first_letter
        self.assertEqual("A", actual)


    def test_quantity_babies_born_with_least_common_letter(self):
        actual = number_babies_with_least_common_letter
        self.assertEqual(30765, actual)


    def test_baby_names_from_A_to_Z(self):
        actual = baby_names_A_to_Z
        expected = {
            'A': 30765, 
            'E': 70474,
            'I': 42567,
            'J': 76126,
            'M': 34195,
            'O': 34128,
            'Q': 41000,
            'S': 42261,
            'W': 34130,
            'Z': 71721,
        }
        self.assertEqual(expected, actual)


    def test_most_common_first_letter(self):
        actual = most_common_first_letter
        self.assertEqual("J", actual)


    def test_number_babies_with_most_common_first_letter(self):
        actual = number_babies_with_most_common_letter
        self.assertEqual(76126, actual)


    def test_most_common_name(self):
        actual = most_common_name
        self.assertEqual("Isabella", actual)


    def test_quantity_people_with_most_common_name(self):
        actual = quantity_people_with_most_common_name
        self.assertEqual(42567, actual)


    def test_name_with_lowest_abs_difference(self):
        actual = name_with_lowest_abs_difference
        self.assertEqual("Mason", actual)


if __name__ == "__main__":
    unittest.main()