import unittest



def unpacking_file_contents(filename):
    import_file = open(filename, "r")
    file_contents = import_file.readlines()
    import_file.close()
    return file_contents


class BabyNames:
    def __init__(self, name):
        self.name = name
        self.baby_count = 0
        self.gender = "Neutral"

    def __str__(self):
        return "%s: %s, %s" % (self.name, self.baby_count, self.gender)


class BabyBoys(BabyNames):
    def __init__(self, name, baby_count, gender):
        super().__init__(name)
        self.baby_count = baby_count
        self.gender = gender

class BabyGirls(BabyNames):
    def __init__(self, name, baby_count, gender):
        super().__init__(name)
        self.baby_count = baby_count
        self.gender = gender


def create_baby_names_database():
    record_file = unpacking_file_contents("baby_names_sample.csv")
    baby_names_database = {}

    for line in record_file:
        line = line.rstrip()
        name, baby_count, gender = line.split(",")
        if not name in baby_names_database.keys():
            baby_names_database[name] = {
                "Boy": 0,
                "Girl": 0,
                "Both Genders": 0,
                "Name Count": 0,
                "Total Babies Count": 0
            }
        baby_names_database[name]["Name Count"] += 1

        if gender == "Boy":
            baby_names_database[name]["Boy"] += int(baby_count)
        else:
            baby_names_database[name]["Girl"] += int(baby_count)
        baby_names_database[name]["Total Babies Count"] += int(baby_count)
        
    for name in baby_names_database.keys():
        baby_boy_count = baby_names_database[name]["Boy"]
        baby_girl_count = baby_names_database[name]["Girl"]
        if baby_boy_count >= 1 and baby_girl_count >= 1:
            baby_names_database[name]["Both Genders"] += baby_boy_count + baby_girl_count

    return baby_names_database



#Q1: How many total names are listed in the database?
def find_total_names_in_database():
    total_names = 0
    baby_names_database = create_baby_names_database()
    for name in baby_names_database.keys():
        name_count = baby_names_database[name]["Name Count"]
        total_names += name_count

    return total_names


#Q2: How many total births are covered by the names in the database?
def calculate_total_births():
    baby_names_database = create_baby_names_database()
    total_births = 0
    for name in baby_names_database.keys():
        if baby_names_database[name]["Both Genders"] >= 1:
            total_births += baby_names_database[name]["Both Genders"]
        elif baby_names_database[name]["Girl"] >= 1:
            total_births += baby_names_database[name]["Girl"]
        else:
            total_births += baby_names_database[name]["Boy"]

    return total_births


# Q3: How many different boys' names are there that begin with the letter Z? (Count the names, not the people.)
def find_quantity_boy_names_starting_with_z():
    baby_names_database = create_baby_names_database()
    count = 0
    for name in baby_names_database.keys():
        first_letter = name[0]
        if baby_names_database[name]["Boy"] >= 1 and first_letter == "Z":
            count += 1

    return count


#Q4: What is the most common girl's name that begins with the letter Q?
def find_most_common_girls_name_starting_with_Q():
    baby_names_database = create_baby_names_database()
    girls_name = None
    highest_count = None

    for name in baby_names_database.keys():
        first_letter = name[0]
        girls_baby_count = baby_names_database[name]["Girl"]
        if (highest_count == None or girls_baby_count > highest_count) and first_letter == "Q":
            highest_count = girls_baby_count
            girls_name = name

    return girls_name


# Q5: How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?
def calculate_total_babies_with_names_starting_and_ending_with_vowels():
    baby_names_database = create_baby_names_database()
    total_babies_count = 0
    vowels = ["A", "E", "I", "O", "U"]

    for name in baby_names_database.keys():
        first_letter = name[0]
        last_letter = name[-1].upper()
        if first_letter in vowels and last_letter in vowels:
            total_babies_count += baby_names_database[name]["Total Babies Count"]

    return total_babies_count

# For Q6, we need the total number of babies for every letter of the alphabet.
# But we have to also make sure that a letter only gets added if there's at least 1 name starting with that letter. 
# So I have created this dictionary to iterate through the names in create_baby_names_database() dictionary 
# And add up the total_baby_count per letter. 

def create_dictionary_of_baby_count_by_first_letter():
    baby_names_database = create_baby_names_database()
    baby_count_by_first_letter = {}
    for name in baby_names_database.keys():
        first_letter = name[0]
        baby_count = baby_names_database[name]["Total Babies Count"]
        if not first_letter in baby_count_by_first_letter.keys():
            baby_count_by_first_letter[first_letter] = 0
        baby_count_by_first_letter[first_letter] += baby_count

    return baby_count_by_first_letter


# Q6: What letter is the least common first letter of a baby's name 
# (in terms of number of babies with names starting with that letter, not number of names)?
def find_least_common_first_letter_of_a_babys_name():
    baby_names_by_first_letter = create_dictionary_of_baby_count_by_first_letter()
    least_common_first_letter = None
    lowest_count = None

    for first_letter in baby_names_by_first_letter.keys():
        baby_count = baby_names_by_first_letter[first_letter]

        if lowest_count == None or baby_count < lowest_count:
            lowest_count = baby_count
            least_common_first_letter = first_letter

    return least_common_first_letter


# Q7: How many babies were born with names starting with that least-common letter?
def find_total_baby_count_for_least_common_letter():
    baby_names_by_first_letter = create_dictionary_of_baby_count_by_first_letter()
    least_common_letter = find_least_common_first_letter_of_a_babys_name()

    return baby_names_by_first_letter[least_common_letter]


# Q8: What letter is the most common first letter of a baby's name 
# (in terms of number of babies with names starting with that letter, not number of names)?
def find_most_common_first_letter_of_a_babys_name():
    baby_names_by_first_letter = create_dictionary_of_baby_count_by_first_letter()
    most_common_first_letter = None
    highest_count = None

    for first_letter in baby_names_by_first_letter.keys():
        baby_count = baby_names_by_first_letter[first_letter]

        if highest_count == None or baby_count > highest_count:
            highest_count = baby_count
            most_common_first_letter = first_letter

    return most_common_first_letter


# Q9: How many babies were born with names starting with that most-common letter?
def find_total_baby_count_for_most_common_letter():
    baby_names_by_first_letter = create_dictionary_of_baby_count_by_first_letter()
    most_common_letter = find_most_common_first_letter_of_a_babys_name()

    return baby_names_by_first_letter[most_common_letter]


# Q10: By default, the Social Security Administration's data separates out names by gender. For example, Jamie is listed separately for girls and for boys. 
# If you were to remove this separation, what would be the most common name in the 2010s regardless of gender?



class TestBabyNames(unittest.TestCase):

    # Correct Answer (#1) in their dataset: 15790
    def test_find_total_names_in_database(self):
        print("-----------------------------------")
        expected = 23
        actual = find_total_names_in_database()
        self.assertEqual(expected, actual)

    # Correct Answer (#2) in their dataset: 7030332
    def test_calculate_total_births(self):
        expected = 401703
        actual = calculate_total_births()
        self.assertEqual(expected, actual)

    # Correct Answer (#3) in their dataset: 159
    def test_find_quantity_boy_names_starting_with_z(self):
        expected = 1
        actual = find_quantity_boy_names_starting_with_z()
        self.assertEqual(expected, actual)

    # Correct Answer (#4) in their dataset: Quinn
    def test_find_most_common_girls_name_starting_with_Q(self):
        expected = "Quinn"
        actual = find_most_common_girls_name_starting_with_Q()
        self.assertEqual(expected, actual)

    # Correct Answer (#5) in their dataset: 672960
    def test_calculate_total_babies_with_names_starting_and_ending_with_vowels(self):
        expected = 150463
        actual = calculate_total_babies_with_names_starting_and_ending_with_vowels()
        self.assertEqual(expected, actual)

    # Correct Answer (#6) in their dataset: U
    def test_find_least_common_first_letter_of_a_babys_name(self):
        expected = "Q"
        actual = find_least_common_first_letter_of_a_babys_name()
        self.assertEqual(expected, actual)        

    # Correct Answer (#7) in their dataset: 6283
    def test_find_total_baby_count_for_least_common_letter(self):
        expected = 3073
        actual = find_total_baby_count_for_least_common_letter()
        self.assertEqual(expected, actual) 

    # Correct Answer (#8) in their dataset:
    def test_find_most_common_first_letter_of_a_babys_name(self):
        expected = "A"
        actual = find_most_common_first_letter_of_a_babys_name()
        self.assertEqual(expected, actual)         


    def test_find_total_baby_count_for_most_common_letter(self):
        expected = 73053
        actual = find_total_baby_count_for_most_common_letter()
        self.assertEqual(expected, actual)           




if __name__ == "__main__":
    unittest.main()

    
