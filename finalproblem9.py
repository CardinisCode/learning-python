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


# Among Legendary Pokemon, what is the most common type? 
# Include both Type1 and Type2 in your count.






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
print(pokemon_with_highest_defense)



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



if __name__ == "__main__":
    unittest.main()