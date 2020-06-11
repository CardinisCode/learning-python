#The line below will open a file containing information
#about every pokemon through Generation 7:


#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has 13 values, separated by commas.
#They are: 
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
#Use this dataset to answer the questions below.

import unittest

def unpacking_file_contents(filename):
    import_file = open(filename, "r")
    file_contents = import_file.readlines()
    import_file.close()
    return file_contents


class Pokemon:
    def __init__(self, number, name, type_1, type_2, hp, attack, defense, special_attack,     special_defense, speed, generation, legendary, mega):
        self.number = number
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp = int(hp)
        self.attack = int(attack)
        self.defense = int(defense)
        self.special_attack = int(special_attack)
        self.special_defense = int(special_defense)
        self.speed = int(speed)
        self.generation = int(generation)
        self.legendary = legendary
        self.mega = mega

    def __str__(self):
        return "%s: %s" % (self.number, self.name)
    
        
    def get_total_stats(self):
        total_stats = (self.hp + self.attack + self.defense + self.special_attack + self.special_defense + self.speed)
        return total_stats
     

def create_pokedex():
    file_contents = unpacking_file_contents('../resource/lib/public/pokedex.csv')
    pokedex = []
    for i in range(1, len(file_contents)):
        line = file_contents[i].rstrip()
        line_split = line.split(",")
        number, name, type_1, type_2, hp, attack, defense, special_attack = line_split[:8]
        special_defense, speed, generation, legendary, mega = line_split[8:]
        current_pokemon = Pokemon(number, name, type_1, type_2, hp, attack, defense, special_attack, special_defense, speed, generation, legendary, mega)
        pokedex.append(current_pokemon)

    return pokedex

pokedex = create_pokedex()        
        
        
def find_weakest_legendary_pokemon(pokedex):
    if len(pokedex) == 0:
        return None

    weakest_total_stat = None
    weakest_pokemon = None

    for indiv_pokemon in pokedex:
        name = indiv_pokemon.name
        legendary = indiv_pokemon.legendary
        total_stats = indiv_pokemon.get_total_stats()
        
        if legendary == "FALSE":
            continue

        elif weakest_pokemon == None or total_stats < weakest_total_stat:
            weakest_pokemon = name
            weakest_total_stat = total_stats

    return weakest_pokemon
        
 


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.


# Correct answer for Q5 in their dataset: Psychic
class TestPokedex(unittest.TestCase):
    def test_the_answer(self):
        pokedex = create_pokedex()
        expected = "Cosmog"
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual) 



if __name__ == "__main__":
    unittest.main()

#file_contents = unpack_file('../resource/lib/public/pokedex.csv')