import unittest

def unpacking_file_contents(filename):
    import_file = open(filename, "r")
    file_contents = import_file.readlines()
    import_file.close()
    return file_contents


class Pokemon:
    def __init__(self, number, name, type_1, type_2, hp, attack, defense, special_attack, special_defense, speed, generation, legendary, mega):
        self.number = number
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.generation = generation
        self.legendary = legendary
        self.mega = mega

    def __str__(self):
        return "%s: %s" % (self.number, self.name)




# Number,Name,Type1,Type2,HP,Attack,Defense,SpecialAtk,SpecialDef,Speed,Generation,Legendary,Mega
def create_pokedex():
    file_contents = unpacking_file_contents("sample_pokemon.csv")
    pokedex = []
    for i in range(1, len(file_contents)):
        line = file_contents[i].rstrip()
        line_split = line.split(",")
        number, name, type_1, type_2, hp, attack, defense, special_attack = line_split[:8]
        special_defense, speed, generation, legendary, mega = line_split[8:]
        current_pokemon = Pokemon(number, name, type_1, type_2, hp, attack, defense, special_attack, special_defense, speed, generation, legendary, mega)
        pokedex.append(current_pokemon)

    return pokedex

#Q1: How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
def calculate_total_pokemon_with_only_1_type():
    pokedex = create_pokedex()
    total_pokemon = 0

    for pokemon in pokedex:
        type_2 = pokemon.type_2
        if type_2 == "":
            total_pokemon += 1

    return total_pokemon


def find_the_elementals():
    pokedex = create_pokedex()
    elementals = []

    for pokemon_char in pokedex:
        elemental_1 = pokemon_char.type_1
        elemental_2 = pokemon_char.type_2
        if not elemental_1 in elementals:
            elementals.append(elemental_1)
        if not elemental_2 in elementals:
            elementals.append(elemental_2)

    for i in elementals:
        if i == "":
            elementals.remove(i)

    return elementals


# Q2: What is the most common type? Include both Type1 and Type2 in your count.
def find_most_common_type():
    pokedex = create_pokedex()
    elementals = find_the_elementals()
    most_common_type = None
    most_common_count = None

    for elemental in elementals:
        count = 0
        for pokemon in pokedex:
            type_1 = pokemon.type_1
            type_2 = pokemon.type_2
            if type_1 == elemental or type_2 == elemental:
                count += 1
        if most_common_count == None or count > most_common_count:
            most_common_count = count
            most_common_type = elemental

    return most_common_type



class TestPokemon(unittest.TestCase):
    # Correct answer for Q1 in their dataset: 420
    def test_calculate_total_pokemon_with_only_1_type(self):
        expected = 10
        actual = calculate_total_pokemon_with_only_1_type()
        self.assertEqual(expected, actual)

    
    def test_find_most_common_type(self):
        expected = "Poison"
        actual = find_most_common_type()
        self.assertEqual(expected, actual)        



if __name__ == "__main__":
    unittest.main()