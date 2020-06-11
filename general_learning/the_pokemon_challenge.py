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

    # #Q6: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)
    def get_total_stats(self):
        total_stats = self.hp + self.attack + self.defense + self.special_attack + self.special_defense + self.speed
        return total_stats
        


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

pokedex = create_pokedex()


def check_if_my_pokedex_is_empty(pokedex):
    if len(pokedex) == 0:
        return None
    return pokedex

pokedex = check_if_my_pokedex_is_empty(pokedex)

class TestCreatePokedex(unittest.TestCase):
    def test_return_none_if_pokedex_is_empty(self):
        pokedex = []
        expected = None
        actual = check_if_my_pokedex_is_empty(pokedex)

        self.assertEqual(expected, actual)



#Q1: How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
def calculate_total_pokemon_with_only_1_type(pokedex):
    total_pokemon = 0

    for pokemon in pokedex:
        type_2 = pokemon.type_2
        if type_2 == "":
            total_pokemon += 1

    return total_pokemon


# Correct answer for Q1 in their dataset: 420
class TestPokemonWithOneType(unittest.TestCase):

    def test_return_0_when_there_are_only_pokemon_with_2_types(self):
        expected = 0
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE")
        ]

        actual = calculate_total_pokemon_with_only_1_type(pokedex)

        self.assertEqual(expected, actual)

    def test_return_1_when_there_is_a_pokemon_with_1_type(self):
        expected = 1
        pokedex = [
            Pokemon(1,"NullDesaur","Grass","",45,49,49,65,65,45,1,"FALSE","FALSE")
        ]

        actual = calculate_total_pokemon_with_only_1_type(pokedex)

        self.assertEqual(expected, actual)

    def test_return_1_when_there_is_a_matching_pokeomon(self):
        expected = 1
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(1,"NullDesaur","Grass","",45,49,49,65,65,45,1,"FALSE","FALSE")
        ]

        actual = calculate_total_pokemon_with_only_1_type(pokedex)

        self.assertEqual(expected, actual)

    def test_with_full_pokedex(self):
        expected = 11
        pokedex = create_pokedex()

        actual = calculate_total_pokemon_with_only_1_type(pokedex)

        self.assertEqual(expected, actual)

# ---------------------------------------------------------------------------------------------------------

# Q2: What is the most common type? Include both Type1 and Type2 in your count.
def find_the_elementals(pokedex):
    elementals = {}

    for pokemon_char in pokedex:
        elemental_1 = pokemon_char.type_1
        elemental_2 = pokemon_char.type_2
        speed = pokemon_char.speed

        elementals.setdefault(elemental_1, {})
        if elemental_2 != "":
            elementals.setdefault(elemental_2, {})

        elementals[elemental_1].setdefault("Count", 0)
        elementals[elemental_1]["Count"] += 1
        elementals[elemental_1].setdefault("Total Speed", 0)
        elementals[elemental_1]["Total Speed"] += speed
        elementals[elemental_1].setdefault("Avg Speed", 0)
        
        if elemental_2 != "":
            elementals[elemental_2].setdefault("Count", 0)
            elementals[elemental_2]["Count"] += 1
            elementals[elemental_2].setdefault("Total Speed", 0)
            elementals[elemental_2]["Total Speed"] += speed
            elementals[elemental_2].setdefault("Avg Speed", 0)

    return elementals


elementals = find_the_elementals(pokedex)


def find_most_common_type(pokedex, elementals):
    most_common_type = None
    most_common_count = None

    if len(pokedex) == 0 or len(elementals) == 0:
        return "None"

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


# Correct answer for Q2 in their dataset: Water
class TestFindMostCommonType(unittest.TestCase):
    #elementals = ["Fire", "Water", "Dragon", "Bug", "Grass", "Poison", "Normal", "Flying"]
    elementals = {
        "Grass": 4, 
        "Poison": 8,
        "Fire": 5, 
        "Flying": 7, 
        "Dragon": 1,
        "Water": 4, 
        "Bug": 7,
        "Normal": 6,
        "Ice": 1
    }

    def test_return_None_if_there_are_no_elementals(self):
        elementals = {}
        pokedex = []
        expected = "None"

        actual = find_most_common_type(pokedex, elementals)
        
        self.assertEqual(expected, actual)         

    def test_return_elemental_if_only_1_elemental_and_1_pokemon_with_1_type(self):
        elementals = {"Grass": 1}
        pokedex = [Pokemon(1,"Bulbasaur","Grass","",45,49,49,65,65,45,1,"FALSE","FALSE")]
        expected = "Grass"

        actual = find_most_common_type(pokedex, elementals)
        
        self.assertEqual(expected, actual)  


    def test_return_elemental_if_only_3_pokemon_with_1_type(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","",45,49,49,65,65,45,1,"FALSE","FALSE"), 
            Pokemon(4,"Charmander","Fire","",39,52,43,60,50,65,1,"FALSE","FALSE"),
            Pokemon(5,"Charmeleon","Fire","",58,64,58,80,65,80,1,"FALSE","FALSE")
            ]
        expected = "Fire"

        actual = find_most_common_type(pokedex, self.elementals)
        
        self.assertEqual(expected, actual)


    def test_return_elemental_if_only_3_pokemon_with_more_than_1_type(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"), 
            Pokemon(4,"Charmander","Fire","Dragon",39,52,43,60,50,65,1,"FALSE","FALSE"),
            Pokemon(6,"Charizard","Fire","Flying",78,84,78,109,85,100,1,"FALSE","FALSE")
            ]
        expected = "Fire"

        actual = find_most_common_type(pokedex, self.elementals)
        
        self.assertEqual(expected, actual)


    def test_return_elemental_with_complete_pokedex(self):
        pokedex = create_pokedex()
        expected = "Poison"

        actual = find_most_common_type(pokedex, self.elementals)
        
        self.assertEqual(expected, actual)


# ---------------------------------------------------------------------------------------------------------

#Q3: What Pokemon has the highest HP statistic?
def find_pokemon_with_highest_hp(pokedex):
    if len(pokedex) == 0:
        return "None"

    highest_hp  = None
    pokemon_with_highest_hp = None

    for pokemon_char in pokedex:
        name = pokemon_char.name
        hp = pokemon_char.hp

        if pokemon_with_highest_hp == None or hp > highest_hp:
            highest_hp = hp
            pokemon_with_highest_hp = name

    return pokemon_with_highest_hp


# Correct answer for Q3 in their dataset: Blissey
class TestFindPokemon_with_highest_HP(unittest.TestCase):

    def test_return_pokemon_with_only_1_pokemon_in_pokedex(self):
        pokedex = [Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE")]
        expected = "Bulbasaur"
        actual = find_pokemon_with_highest_hp(pokedex)

        self.assertEqual(expected, actual)


    def test_return_pokemon_with_highest_HP_when_only_2_pokemon_in_pokedex(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","FALSE")
            ]
        expected = "Ivysaur"
        actual = find_pokemon_with_highest_hp(pokedex)

        self.assertEqual(expected, actual)

    def test_return_pokemon_with_highest_HP_when_only_3_pokemon_in_pokedex(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","FALSE"),
            Pokemon(3,"Venusaur","Grass","Poison",80,82,83,100,100,80,1,"FALSE","FALSE")
            ]
        expected = "Venusaur"
        actual = find_pokemon_with_highest_hp(pokedex)

        self.assertEqual(expected, actual)


    def test_return_pokemon_with_highest_HP_with_complete_pokedex(self):
        pokedex = create_pokedex()
        expected = "Articuno"
        actual = find_pokemon_with_highest_hp(pokedex)

        self.assertEqual(expected, actual)   


# ---------------------------------------------------------------------------------------------------------

#Q4: Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?
def find_pokemon_with_highest_defense_stats(pokedex):
    if len(pokedex) == 0:
        return "None"

    highest_defense = None
    pokemon_highest_defense = None

    for pokemon_char in pokedex:
        name = pokemon_char.name
        defense = pokemon_char.defense
        mega = pokemon_char.mega
        legendary = pokemon_char.legendary

        if mega == "TRUE" or legendary == "TRUE":
            continue

        elif pokemon_highest_defense == None or defense > highest_defense:
            highest_defense = defense
            pokemon_highest_defense = name

    return pokemon_highest_defense


# Correct answer for Q4 in their dataset: Shuckle
class TestFindPokemon_with_highest_defense_stats_excl_Mega_and_legendary(unittest.TestCase): 

    def test_return_pokemon_when_there_is_one_pokemon(self):
        pokedex = [Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE")]
        expected = "Bulbasaur"
        actual = find_pokemon_with_highest_defense_stats(pokedex)

        self.assertEqual(expected, actual) 


    def test_return_pokemon_when_there_are_2_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","FALSE")
            ]
        expected = "Ivysaur"
        actual = find_pokemon_with_highest_defense_stats(pokedex)

        self.assertEqual(expected, actual) 
             

    def test_return_pokemon_when_there_are_3_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","FALSE"),
            Pokemon(3,"Venusaur","Grass","Poison",80,82,83,100,100,80,1,"FALSE","FALSE")
            ]
        expected = "Venusaur"
        actual = find_pokemon_with_highest_defense_stats(pokedex)

        self.assertEqual(expected, actual) 


    def test_return_pokemon_with_complete_pokedex(self):
        pokedex = create_pokedex()
        expected = "Blastoise"
        actual = find_pokemon_with_highest_defense_stats(pokedex)

        self.assertEqual(expected, actual) 


# ---------------------------------------------------------------------------------------------------------

#Q5: Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.
def create_legendary_pokedex_by_type(pokedex):
    legendary_pokedex = {}

    for pokemon_char in pokedex:
        legendary = pokemon_char.legendary
        type_1 = pokemon_char.type_1
        type_2 = pokemon_char.type_2

        if not type_1 in legendary_pokedex.keys() and type_1 != "":
            legendary_pokedex[type_1] = 0
        if not type_2 in legendary_pokedex.keys() and type_2 != "":
            legendary_pokedex[type_2] = 0
        
        if legendary == "FALSE":
            continue
        else: 
            if type_1 != "":
                legendary_pokedex[type_1] += 1
            if type_2 != "":
                legendary_pokedex[type_2] += 1

    return legendary_pokedex

legendary_pokedex_by_type = create_legendary_pokedex_by_type(pokedex)


def find_most_common_type_among_legendary_pokemon(pokedex, legendary_pokedex_by_type):
    if len(pokedex) == 0:
        return None

    most_common_type = None 
    most_occurences = None

    for pokemon_type in legendary_pokedex_by_type.keys():
        occurences = legendary_pokedex_by_type[pokemon_type]

        if (most_common_type == None or occurences > most_occurences):
            most_occurences = occurences
            most_common_type = pokemon_type

    if most_occurences == 0:
        return None

    return most_common_type


# Correct answer for Q5 in their dataset: Psychic
# find_most_common_type_among_legendary_pokemon(pokedex)
class TestFindMostCommonType_among_legendary_pokemon(unittest.TestCase):
    
    def test_return_none_when_there_are_no_legendary_pokemon(self):
        pokedex = [Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE")]
        legendary_pokedex_by_type = {'Grass': 0, 'Poison': 0, 'Fire': 0, 'Flying': 0, 'Dragon': 0, 'Water': 0, 'Bug': 0, 'Normal': 0, 'Ice': 0}
        expected = None
        actual = find_most_common_type_among_legendary_pokemon(pokedex, legendary_pokedex_by_type)

        self.assertEqual(expected, actual)

    def test_return_most_common_type_when_given_full_pokedex(self):
        pokedex = create_pokedex()
        legendary_pokedex_by_type = create_legendary_pokedex_by_type(pokedex)
        expected = "Ice"
        actual = find_most_common_type_among_legendary_pokemon(pokedex, legendary_pokedex_by_type)

        self.assertEqual(expected, actual)

# ---------------------------------------------------------------------------------------------------------

#Q6: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), 
# what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.
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


# Correct answer for Q6 in their dataset: Cosmog
class TestFindWeakestLegendaryPokemon(unittest.TestCase):

    def test_return_none_when_there_are_no_legendary_pokemon(self):
        pokedex = [Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE")]
        expected = None
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)      


    def test_return_pokemon_if_only_1_legendary_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(144,"Articuno","Ice","",90,85,100,95,125,85,1,"TRUE","FALSE")
            ]
        expected = "Articuno"
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual) 

    def test_return_pokemon_with_weakest_stat_when_there_are_2_legendary_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"TRUE","FALSE"),
            Pokemon(144,"Articuno","Ice","",90,85,100,95,125,85,1,"TRUE","FALSE")
            ]
        expected = "Bulbasaur"
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)         


    def test_return_pokemon_with_weakest_stat_when_there_are_multiple_legendary_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"TRUE","FALSE"),
            Pokemon(144,"Articuno","Ice","",90,85,100,95,125,85,1,"TRUE","FALSE"), 
            Pokemon(3,"Venusaur","Grass","Poison",80,82,83,100,100,80,1,"TRUE","FALSE"),
            Pokemon(4,"Charmander","Fire","",39,52,43,60,50,65,1,"TRUE","FALSE"), 
            Pokemon(5,"Charmeleon","Fire","",58,64,58,80,65,80,1,"TRUE","FALSE")
            ]
        expected = "Charmander"
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)   


    def test_return_pokemon_with_weakest_stat_with_sample_pokemon(self):
        pokedex = create_pokedex()
        expected = "Articuno"
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)
    
    

# ---------------------------------------------------------------------------------------------------------

#Q7: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), 
# what is the strongest non-Legendary, non-Mega Pokemon? If there is a tie, list any of the tying Pokemon.

def find_strongest_non_mega_non_legendary_pokemon(pokedex):
    strongest_pokemon = None
    strongest_stats = None

    for indiv_pokemon in pokedex:
        name = indiv_pokemon.name
        legendary = indiv_pokemon.legendary
        mega = indiv_pokemon.mega
        total_stats = indiv_pokemon.get_total_stats()

        if legendary == "TRUE" or mega == "TRUE":
            continue
        elif strongest_pokemon == None or total_stats > strongest_stats:
            strongest_stats = total_stats
            strongest_pokemon = name


    return strongest_pokemon


#  Correct answer for Q7 in their dataset: Slaking
class TestStrongestNonMegaNonLegendaryPokemon(unittest.TestCase):
    def test_return_none_if_all_pokemon_are_legendary(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"TRUE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"TRUE","FALSE"),
        ]
        expected = None 
        actual = find_strongest_non_mega_non_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)

    def test_return_none_if_all_pokemon_are_mega(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","TRUE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","TRUE"),
        ]
        expected = None 
        actual = find_strongest_non_mega_non_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)


    def test_return_pokemon_if_there_is_1_non_mega_non_legendary_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","TRUE"),
        ]
        expected = "Bulbasaur" 
        actual = find_strongest_non_mega_non_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)


    def test_return_pokemon_with_highest_stat_among_non_mega_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"FALSE","TRUE"),
            Pokemon(3,"Venusaur","Grass","Poison",80,82,83,100,100,80,1,"FALSE","FALSE")
        ]
        expected = "Venusaur" 
        actual = find_strongest_non_mega_non_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)        


    def test_return_pokemon_with_highest_stat_among_non_legendary_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"FALSE","FALSE"),
            Pokemon(2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,1,"TRUE","FALSE"),
            Pokemon(3,"Venusaur","Grass","Poison",80,82,83,100,100,80,1,"FALSE","FALSE")
        ]
        expected = "Venusaur" 
        actual = find_strongest_non_mega_non_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual) 

    
    def test_return_pokemon_with_highest_stat_with_full_pokedex(self):
        "----------------------------------------------------------------"
        pokedex = create_pokedex()
        expected = "Charizard" 
        actual = find_strongest_non_mega_non_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual)       


# ---------------------------------------------------------------------------------------------------------

#Q8: What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.

def find_type_with_highest_avg_speed(elementals):
    if len(elementals) == 0:
        return None

    type_with_highest_avg_speed = None
    highest_avg_speed = None
    
    for elemental, stats in elementals.items():
        count = stats["Count"]
        speed = stats["Total Speed"]
        avg_speed = round(speed / count)
        stats["Avg Speed"] = avg_speed

        if type_with_highest_avg_speed == None or avg_speed > highest_avg_speed:
            highest_avg_speed = avg_speed
            type_with_highest_avg_speed = elemental
    
    return type_with_highest_avg_speed


class TestFindTypeWithHighestAvgSpeed(unittest.TestCase):

    def test_return_none_when_there_are_no_types(self):
        elementals = {}
        expected = None
        actual = find_type_with_highest_avg_speed(elementals)

        self.assertEqual(expected, actual)

    def test_return_type_when_there_is_only_1_type(self):
        elementals = {"Water": {"Count": 4, "Total Speed": 257, "Avg Speed": 64}}
        expected = "Water"
        actual = find_type_with_highest_avg_speed(elementals)

        self.assertEqual(expected, actual)


    def test_return_type_with_highest_avg_when_there_are_2_types(self):
        elementals = {
            "Water": {"Count": 4, "Total Speed": 257, "Avg Speed": 64}, 
            "Grass": {"Count": 4, "Total Speed": 265, "Avg Speed": 66}
            }
        expected = "Grass"
        actual = find_type_with_highest_avg_speed(elementals)

        self.assertEqual(expected, actual)        


    def test_return_type_with_highest_avg_when_given_all_elementals(self):
        pokedex = create_pokedex()
        elementals = find_the_elementals(pokedex)
        expected = "Dragon"
        actual = find_type_with_highest_avg_speed(elementals)

        self.assertEqual(expected, actual)      


# ---------------------------------------------------------------------------------------------------------






if __name__ == "__main__":
    unittest.main()