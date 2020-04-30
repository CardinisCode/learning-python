import unittest

def unpacking_file_contents(filename):
    current_file = open(filename, "r")
    file_contents = current_file.readlines()
    current_file.close()

    return file_contents

def create_pokemon_collection(file_contents):
    my_pokemon_collection = {}

    for index in range(1, len(file_contents)):
        current_line = file_contents[index].rstrip()
        current_line_split = current_line.split(",")
        pokemon_name = current_line_split[1]

        my_pokemon_collection[pokemon_name] = Pokemon(pokemon_name, {
            "Pokemon ID" : current_line_split[0],
            "Type1" : current_line_split[2],
            "Type2" : current_line_split[3],
            "HP" : current_line_split[4],
            "Attack" : current_line_split[5],
            "Defense" : current_line_split[6],
            "SpecialAtk" : current_line_split[7],
            "SpecialDef" : current_line_split[8],
            "Speed" : current_line_split[9],
            "Generation" : current_line_split[10],
            "Legendary" : current_line_split[11],
            "Mega" : current_line_split[12],
        })
    
    return my_pokemon_collection

def create_pokemon_deck(my_pokemon_collection):
    my_pokemon_deck = []
    for name in my_pokemon_collection.keys():
        my_pokemon_deck.append(name)

    return my_pokemon_deck


def find_total_pokemon_only_single_type(my_pokemon_collection):
    pokemon_count = 0
    for pokemon in my_pokemon_collection.values():
        type2 = pokemon.type2
        if type2 == '':
            pokemon_count += 1

    return pokemon_count


def create_type_dictionary(my_pokemon_collection):
    type_dictionary = {}

    for pokemon in my_pokemon_collection.values():
        type1 = pokemon.type1
        type2 = pokemon.type2
        if not type1 in type_dictionary.keys():
            type_dictionary[type1] = 0
        if not type2 == '' and not type2 in type_dictionary.keys():
            type_dictionary[type2] = 0

        type_dictionary[type1] += 1
        if not type2 == '': 
            type_dictionary[type2] += 1

    return type_dictionary


# What is the most common type? Include both Type1 and Type2 in your count.
def find_most_common_type(pokemon_type_dictionary):
    most_common_type = None
    most_common_type_count = None

    for skill_type, count in pokemon_type_dictionary.items():
        if most_common_type == None: 
            most_common_type = skill_type
            most_common_type_count = count
        elif count > most_common_type_count:
            most_common_type = skill_type
            most_common_type_count = count

    return most_common_type


def find_pokemon_with_highest_hp(my_pokemon_collection):
    pokemon_with_highest_HP = None
    highest_hp = None
    for pokemon in my_pokemon_collection.values():
        current_pokemon = pokemon.name
        current_hp = pokemon.hp
        if highest_hp == None: 
            highest_hp = current_hp
            pokemon_with_highest_HP = current_pokemon
        elif current_hp > highest_hp:
            highest_hp = current_hp
            pokemon_with_highest_HP = current_pokemon

    return pokemon_with_highest_HP


#Q4: Excluding Pokemon that are either Mega or Legendary, 
# what Pokemon has the highest Defense statistic?
def find_pokemon_with_highest_defense(my_pokemon_collection):
    pokemon_with_highest_defense = None
    highest_defense = None
    for pokemon in my_pokemon_collection.values():
        current_pokemon = pokemon.name
        current_defense = pokemon.defense
        if not "Mega" in current_pokemon and not "Legendary" in current_pokemon:
            if highest_defense == None:
                highest_defense = current_defense
                pokemon_with_highest_defense = current_pokemon
            elif current_defense > highest_defense:
                highest_defense = current_defense
                pokemon_with_highest_defense = current_pokemon

    return pokemon_with_highest_defense


def create_legendary_dictionary_with_types(my_pokemon_collection):
    legendary_pokemon_dictionary = {}
    for pokemon in my_pokemon_collection.values():
        type1 = pokemon.type1
        type2 = pokemon.type2
        legendary = pokemon.legendary

        if not type1 in legendary_pokemon_dictionary.keys():
            legendary_pokemon_dictionary[type1] = 0
        if not type2 in legendary_pokemon_dictionary.keys() and not type2 == "":
            legendary_pokemon_dictionary[type2] = 0

        if legendary == "TRUE": 
            legendary_pokemon_dictionary[type1] += 1
            if not type2 == "":
                legendary_pokemon_dictionary[type2] += 1

    return legendary_pokemon_dictionary


def find_most_common_type_among_legendary_pokemon(legendary_dict_with_types):
    most_common_type = None
    most_common_type_occurences = 0

    for pokemon_type, quantity in legendary_dict_with_types.items():
        if quantity > most_common_type_occurences:
            most_common_type_occurences = quantity
            most_common_type = pokemon_type

    return most_common_type


def create_legendary_dict_with_total_stats(my_pokemon_collection):
    legendary_dict_with_total_stats = {}

    for pokemon in my_pokemon_collection.values():
        pokemon_name = pokemon.name
        total_stats = pokemon.get_total_power()
        legendary = pokemon.legendary
        
        if legendary == "TRUE":
            legendary_dict_with_total_stats[pokemon_name] = total_stats

    return legendary_dict_with_total_stats

def find_weakest_legendary_pokemon(legendary_dict_with_total_stats):
    weakest_legendary_pokemon = None
    lowest_total_stat = None

    for pokemon, total_stat in legendary_dict_with_total_stats.items():
        if lowest_total_stat == None: 
            lowest_total_stat = total_stat
            weakest_legendary_pokemon = pokemon
        elif total_stat < lowest_total_stat:
            lowest_total_stat = total_stat
            weakest_legendary_pokemon = pokemon

    return weakest_legendary_pokemon


# In terms of the sum of all six stats 
# (HP, Attack, Defense, Special Attack, Special Defense, and Speed), 
# what is the strongest non-Legendary, non-Mega Pokemon? 
# If there is a tie, list any of the tying Pokemon.

def create_dict_for_ordinary_pokemon_by_total_power(my_pokemon_collection):
    ordinary_pokemon_by_total_power = {}
    for pokemon in my_pokemon_collection.values():
        pokemon_name = pokemon.name
        total_power = pokemon.get_total_power()
        legendary = pokemon.legendary
        mega = pokemon.mega

        if mega == "FALSE" and legendary == "FALSE": 
            # print(pokemon_name, ":", total_power)
            ordinary_pokemon_by_total_power[pokemon_name] = total_power

    return ordinary_pokemon_by_total_power


def find_strongest_pokemon_by_total_power(ordinary_pokemon_by_total_power):
    strongest_pokemon = None
    highest_total_power = None
    for pokemon in ordinary_pokemon_by_total_power.keys():
        total_power = ordinary_pokemon_by_total_power[pokemon]
        
        if highest_total_power == None or total_power > highest_total_power:
            highest_total_power = total_power
            strongest_pokemon = pokemon

    return strongest_pokemon


def create_type_dict_with_speed_and_occurences(my_pokemon_collection):
    type_dict_with_highest_avg_speed = {}
    for pokemon in my_pokemon_collection.values():
        type1 = pokemon.type1
        type2 = pokemon.type2
        speed = pokemon.speed

        if not type1 in type_dict_with_highest_avg_speed.keys():
            type_dict_with_highest_avg_speed[type1] = {
                "Total Speed": 0, 
                "Total Occurences": 0,
            }
        type_dict_with_highest_avg_speed[type1]["Total Speed"] += int(speed)
        type_dict_with_highest_avg_speed[type1]["Total Occurences"] += 1

        if not type2 == "" and not type2 in type_dict_with_highest_avg_speed.keys():
            type_dict_with_highest_avg_speed[type2] = {
                "Total Speed": 0, 
                "Total Occurences": 0,
            }
        if not type2 == "":
            type_dict_with_highest_avg_speed[type2]["Total Speed"] += int(speed)
            type_dict_with_highest_avg_speed[type2]["Total Occurences"] += 1

    return type_dict_with_highest_avg_speed


def find_type_with_highest_avg_speed(type_dict_with_speed_and_occurences):
    type_with_highest_avg_speed = None
    highest_avg_speed = None

    for pokemon_type in type_dict_with_speed_and_occurences.keys():
        total_speed = type_dict_with_speed_and_occurences[pokemon_type]["Total Speed"]
        total_occurences = type_dict_with_speed_and_occurences[pokemon_type]["Total Occurences"]
        average_speed = round(total_speed / total_occurences)
        
        if highest_avg_speed == None: 
            highest_avg_speed = average_speed
            type_with_highest_avg_speed = pokemon_type
        
        elif average_speed > highest_avg_speed:
            highest_avg_speed = average_speed
            type_with_highest_avg_speed = pokemon_type

    return (type_with_highest_avg_speed, highest_avg_speed)


def create_dict_by_generation(my_pokemon_collection):
    generational_dict = {}

    for pokemon in my_pokemon_collection.values(): 
        generation = pokemon.generation
        total_power = pokemon.get_total_power()

        if not generation in generational_dict.keys():
            generational_dict[generation] ={
                "Overall Power": 0, 
                "Quantity": 0, 
                "Average Power": 0,
            }

        generational_dict[generation]["Overall Power"] += total_power
        generational_dict[generation]["Quantity"] += 1
    
    for generation in generational_dict.keys():
        overall_power = generational_dict[generation]["Overall Power"]
        total_pokemon = generational_dict[generation]["Quantity"]
        generational_dict[generation]["Average Power"] = round(overall_power / total_pokemon)

    return generational_dict


def find_generation_with_highest_avg_total(generational_dict):
    generation_with_highest_avg_total = None
    highest_avg_total = None
    second_highest_avg = None

    for generation in generational_dict.keys():
        average_power = generational_dict[generation]["Average Power"]
        # print(generation, ":", average_power)

        if highest_avg_total == None or average_power > highest_avg_total: 
            highest_avg_total = average_power
            generation_with_highest_avg_total = generation


    for generation in generational_dict.keys():
        average_power = generational_dict[generation]["Average Power"]
        if not generation == generation_with_highest_avg_total:
            print(generation, ":", average_power)
            if second_highest_avg == None or average_power > second_highest_avg: 
                second_highest_avg = average_power

    difference_between_avgs =  round(highest_avg_total - second_highest_avg)

    return (generation_with_highest_avg_total, difference_between_avgs)


# Q12: Rounded to the nearest integer, 
# how much higher is the average sum of all six stats among Mega Pokemon 
# than their non-Mega versions? Note that Mega Pokemon share the same Number 
# (the first column) as their non-Mega versions, 
# which will allow you to find all Pokemon that have a Mega version.





class Pokemon:
    def __init__(self, name, stats):
        self.name = name
        self.id = stats["Pokemon ID"]
        self.type1 = stats["Type1"]
        self.type2 = stats["Type2"]
        self.hp = int(stats["HP"])
        self.attack = int(stats["Attack"])
        self.defense = int(stats["Defense"])
        self.special_attack = int(stats["SpecialAtk"])
        self.special_defense = int(stats["SpecialDef"])
        self.speed = int(stats["Speed"])
        self.generation = stats["Generation"]
        self.legendary = stats["Legendary"]
        self.mega = stats["Mega"]

    def get_total_power(self):
        total_power = self.hp + self.attack + self.defense + self.special_attack + self.special_defense + self.speed
        return total_power

    def __str__(self):
        return "%s: %s" % (self.name, self.defense)




file_contents = unpacking_file_contents("sample9.csv")
print()
my_pokemon_collection = create_pokemon_collection(file_contents)
# print(my_pokemon_collection)

total_pokemon_with_single_type = find_total_pokemon_only_single_type(my_pokemon_collection)
pokemon_type_dictionary = create_type_dictionary(my_pokemon_collection)
most_common_type = find_most_common_type(pokemon_type_dictionary)
pokemon_with_highest_HP = find_pokemon_with_highest_hp(my_pokemon_collection)
pokemon_with_highest_defense = find_pokemon_with_highest_defense(my_pokemon_collection)
legendary_dict_with_types = create_legendary_dictionary_with_types(my_pokemon_collection)
most_common_legendary_type = find_most_common_type_among_legendary_pokemon(legendary_dict_with_types)
legendary_dict_with_total_stats = create_legendary_dict_with_total_stats(my_pokemon_collection)
weakest_legendary_pokemon = find_weakest_legendary_pokemon(legendary_dict_with_total_stats)
ordinary_pokemon_by_total_power = create_dict_for_ordinary_pokemon_by_total_power(my_pokemon_collection)
strongest_pokemon_by_total_power = find_strongest_pokemon_by_total_power(ordinary_pokemon_by_total_power)
type_dict_with_speed_and_occurences = create_type_dict_with_speed_and_occurences(my_pokemon_collection)
type_with_highest_avg_speed = find_type_with_highest_avg_speed(type_dict_with_speed_and_occurences)[0]
highest_avg_speed = find_type_with_highest_avg_speed(type_dict_with_speed_and_occurences)[1]
generational_dict = create_dict_by_generation(my_pokemon_collection)
generation_with_highest_avg_total = find_generation_with_highest_avg_total(generational_dict)[0]
difference_between_averages = find_generation_with_highest_avg_total(generational_dict)[1]
print(difference_between_averages)

# Rounded to the nearest integer, 
# how much higher was that statistic than the next-closest generation's average sum
#  of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?





class CheckMyPokemonCollection(unittest.TestCase):
    def test_how_many_pokemon_have_no_type2(self):
        expected = 10
        actual = total_pokemon_with_single_type 
        self.assertEqual(expected, actual)

    def test_most_common_type(self):
        expected = "Poison"
        actual = most_common_type
        self.assertEqual(expected, actual)
        

    def test_pokemon_highest_hp(self):
        expected = "Mega Pidgeot"
        actual = pokemon_with_highest_HP
        self.assertEqual(expected, actual)

    
    def test_pokemon_highest_defense(self):
        expected = "Blastoise"
        actual = pokemon_with_highest_defense
        self.assertEqual(expected, actual)

    
    def test_legendary_pokemon_most_common_type(self):
        expected = "Bug"
        actual = most_common_legendary_type
        self.assertEqual(expected, actual)

    
    def test_weakest_legendary_pokemon(self):
        expected = "Legendary Caterpie"
        actual = weakest_legendary_pokemon
        self.assertEqual(expected, actual)


    def test_type_with_highest_avg_speed(self):
        expected = "Dragon"
        actual = type_with_highest_avg_speed
        self.assertEqual(expected, actual)


    def test_strongest_pokemon_by_total_power(self):
        expected = "Charizard"
        actual = strongest_pokemon_by_total_power
        self.assertEqual(expected, actual)


    def test_highest_avg_speed(self):
        expected = 100
        actual = highest_avg_speed
        self.assertEqual(expected, actual)


    def test_generation_with_highest_avg_total(self):
        expected = "4"
        actual = generation_with_highest_avg_total
        self.assertEqual(expected, actual)


    def test_find_diff_between_avgs(self):
        expected = 197
        actual = difference_between_averages
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()