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

print()
print("Q1:", calculate_total_pokemon_with_only_1_type(pokedex))
print("Correct answer for Q1 in their dataset: 420")
print()

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

print("Q2:", find_most_common_type(pokedex, elementals))
print("Correct answer for Q2 in their dataset: Water")
print()

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

print("Q3:", find_pokemon_with_highest_hp(pokedex))
print("Correct answer for Q3 in their dataset: Blissey")
print()

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

print("Q4:", find_pokemon_with_highest_defense_stats(pokedex))
print("Correct answer for Q4 in their dataset: Shuckle")
print()

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

print("Q5:", find_most_common_type_among_legendary_pokemon(pokedex, legendary_pokedex_by_type))
print("Correct answer for Q5 in their dataset: Psychic")
print()

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
    
    
print("Q6:", find_weakest_legendary_pokemon(pokedex))
print("Correct answer for Q6 in their dataset: Cosmog")
print()

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


print("Q7:", find_strongest_non_mega_non_legendary_pokemon(pokedex))
print("Correct answer for Q7 in their dataset: Slaking")
print() 

# ---------------------------------------------------------------------------------------------------------

#Q8: What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.
#Q9: Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation

def find_type_with_highest_avg_speed_and_highest_avg_speed(elementals):
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
    
    return (type_with_highest_avg_speed, highest_avg_speed)


type_with_highest_avg_speed = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)[0]
highest_avg_speed = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)[1]

print("Q8:", type_with_highest_avg_speed)
print("Correct answer for Q8 in their dataset: Flying")
print()
print("Q9:", highest_avg_speed)
print("Correct answer for Q9 in their dataset: 85")
print()



class TestFindTypeWithHighestAvgSpeed(unittest.TestCase):

    def test_return_none_when_there_are_no_types(self):
        elementals = {}
        expected = None
        actual = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)

        self.assertEqual(expected, actual)

    def test_return_type_when_there_is_only_1_type(self):
        elementals = {"Water": {"Count": 4, "Total Speed": 257, "Avg Speed": 64}}
        expected = "Water"
        actual = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)[0]

        self.assertEqual(expected, actual)


    def test_return_type_with_highest_avg_when_there_are_2_types(self):
        elementals = {
            "Water": {"Count": 4, "Total Speed": 257, "Avg Speed": 64}, 
            "Grass": {"Count": 4, "Total Speed": 265, "Avg Speed": 66}
            }
        expected = "Grass"
        actual = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)[0]

        self.assertEqual(expected, actual)        


    def test_return_type_with_highest_avg_when_given_all_elementals(self):
        pokedex = create_pokedex()
        elementals = find_the_elementals(pokedex)
        expected = "Dragon"
        actual = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)[0]

        self.assertEqual(expected, actual) 


    def test_return_highest_avg_when_given_all_elementals(self):
        pokedex = create_pokedex()
        elementals = find_the_elementals(pokedex)
        expected = 100
        actual = find_type_with_highest_avg_speed_and_highest_avg_speed(elementals)[1]

        self.assertEqual(expected, actual)              


# ---------------------------------------------------------------------------------------------------------

# Q10: Among all 7 Pokemon generations, 
# which generation had the highest average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

# Q11: Rounded to the nearest integer, 
# how much higher was that statistic than the next-closest generation's average sum of all six stats 
# (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

def create_pokedex_by_generation(pokedex):
    pokedex_by_generation = {}
    
    for pokemon_char in pokedex:
        total_stats = pokemon_char.get_total_stats()
        generation = pokemon_char.generation
        pokedex_by_generation.setdefault(generation, {})
        pokedex_by_generation[generation].setdefault("Count", 0)
        pokedex_by_generation[generation]["Count"] += 1
        pokedex_by_generation[generation].setdefault("Total Stats", 0)
        pokedex_by_generation[generation]["Total Stats"] += total_stats

    for generation in pokedex_by_generation.keys():
        total_stats = pokedex_by_generation[generation]["Total Stats"]
        count = pokedex_by_generation[generation]["Count"]
        avg_stat = round(total_stats / count)
        pokedex_by_generation[generation].setdefault("Avg Stat", 0)
        pokedex_by_generation[generation]["Avg Stat"] = avg_stat

    return pokedex_by_generation

pokedex_by_generation = create_pokedex_by_generation(pokedex)
# print("pokedex_by_generation:", pokedex_by_generation)

def find_generation_with_highest_avg_total_stat(pokedex_by_generation):
    if len(pokedex_by_generation) == 0:
        return None

    highest_avg_stat = None
    generation_with_highest_stat = None
    generations_present = []

    for generation, stats in pokedex_by_generation.items():
        avg_stat = stats["Avg Stat"]
        generations_present.append(generation)

        if generation_with_highest_stat == None or avg_stat > highest_avg_stat:
            highest_avg_stat = avg_stat
            generation_with_highest_stat = generation

    second_highest_avg_stat = None
    generation_with_2nd_highest_stat = None
    difference = None

    for generation, stats in pokedex_by_generation.items():
        avg_stat = stats["Avg Stat"]

        if generation == generation_with_highest_stat:
            continue

        elif generation_with_2nd_highest_stat == None or avg_stat > second_highest_avg_stat:
            second_highest_avg_stat = avg_stat
            generation_with_2nd_highest_stat = generation    

    if second_highest_avg_stat != None:
        difference = abs(highest_avg_stat - second_highest_avg_stat)

    return (generation_with_highest_stat, difference)

print("Q10:", find_generation_with_highest_avg_total_stat(pokedex_by_generation)[0])
print("Correct answer for Q10 in their dataset: 7")
print()
difference_between_the_highest_and_2nd_highest_stat = find_generation_with_highest_avg_total_stat(pokedex_by_generation)[1]
print("Q11:", difference_between_the_highest_and_2nd_highest_stat)
print("Note my answer to Q11 is:", difference_between_the_highest_and_2nd_highest_stat, "because the sample_pokemon.csv only has 1 generation")
print("Correct answer for Q11 in their dataset: 2")
print()

class TestFindGenerationWithHighestAvgTotalStat(unittest.TestCase):
    def test_return_none_if_there_are_no_generations(self):
        pokedex = {}
        expected = None
        actual = find_generation_with_highest_avg_total_stat(pokedex)

        self.assertEqual(expected, actual)


    def test_if_return_generation_if_there_is_only_1(self):
        pokedex = {1: {"Count": 5, "Total Stats": 1000, "Avg Stat": 200}}
        expected = 1
        actual = find_generation_with_highest_avg_total_stat(pokedex)[0]

        self.assertEqual(expected, actual)


    def test_returns_generation_with_highest_avg_stat_when_there_are_2_generations(self):
        pokedex = {
            1: {"Count": 5, "Total Stats": 1000, "Avg Stat": 200}, 
            2: {"Count": 2, "Total Stats": 500, "Avg Stat": 250}
            }
        expected = 2
        actual = find_generation_with_highest_avg_total_stat(pokedex)[0]

        self.assertEqual(expected, actual)        

    def test_return_generation_with_highest_avg_stat_when_there_are_numerous_generations(self):
        pokedex = {
            1: {"Count": 5, "Total Stats": 1000, "Avg Stat": 200}, 
            2: {"Count": 2, "Total Stats": 500, "Avg Stat": 250},
            3: {"Count": 1, "Total Stats": 100, "Avg Stat": 100}
            }
        expected = 2

        actual = find_generation_with_highest_avg_total_stat(pokedex)[0]

        self.assertEqual(expected, actual)

    def test_return_generation_with_highest_avg_stat_when_given_full_pokedex(self):
        pokedex = create_pokedex()
        pokedex_by_generation = create_pokedex_by_generation(pokedex)
        expected = 1

        actual = find_generation_with_highest_avg_total_stat(pokedex_by_generation)[0]

        self.assertEqual(expected, actual)


    # From this point we're  testing the difference (find_generation_with_highest_avg_total_stat(pokedex_by_generation)[1])
    def test_return_none_if_there_is_only_1_generation_present(self):
        pokedex = {
            1: {"Count": 5, "Total Stats": 1000, "Avg Stat": 200}, 
            }
        expected = None
        
        actual = find_generation_with_highest_avg_total_stat(pokedex)[1]

        self.assertEqual(expected, actual)               


    def test_return_difference_if_there_are_2_generations(self):
        pokedex = {
            1: {"Count": 5, "Total Stats": 1000, "Avg Stat": 200}, 
            2: {"Count": 2, "Total Stats": 500, "Avg Stat": 250}
            }

        expected = 50
        actual = find_generation_with_highest_avg_total_stat(pokedex)[1]

        self.assertEqual(expected, actual)


    def test_return_difference_if_there_are_multiple_generations(self):
        pokedex = {
            1: {"Count": 5, "Total Stats": 1000, "Avg Stat": 200}, 
            2: {"Count": 2, "Total Stats": 500, "Avg Stat": 250}, 
            3: {"Count": 1, "Total Stats": 100, "Avg Stat": 100}
            }

        expected = 50
        actual = find_generation_with_highest_avg_total_stat(pokedex)[1]

        self.assertEqual(expected, actual)        


# ---------------------------------------------------------------------------------------------------------

# Q12: Rounded to the nearest integer, 
# how much higher is the average sum of all six stats among Mega Pokemon than their non-Mega versions? 
# Note that Mega Pokemon share the same Number (the first column) as their non-Mega versions, which will allow you to find all Pokemon that have a Mega version.

def create_pokedex_by_ID(pokedex):
    pokedex_by_ID = {}
    for pokemon_char in pokedex:
        name = pokemon_char.name
        number = pokemon_char.number
        legendary = pokemon_char.legendary

        if legendary == "TRUE":
            continue
        else: 
            pokedex_by_ID.setdefault(number, [])
            pokedex_by_ID[number].append(name)

    return pokedex_by_ID

pokedex_by_ID = create_pokedex_by_ID(pokedex)


def create_mega_vs_non_mega_pokedex(pokedex, pokedex_by_ID):
    mega_vs_non_mega_pokedex = {
        "Mega Pokemon": {"Count": 0, "Total Stats": 0, "Avg Stats": 0},
        "Non Mega Pokemon": {"Count": 0, "Total Stats": 0, "Avg Stats": 0}
    }

    normal_pokemon = []
    for names in pokedex_by_ID.values():
        # print(pokemon_ID, names, len(names))
        if len(names) <= 1 :
            continue 
        normal_pokemon.append(names[0])
    
    for pokemon_char in pokedex:
        name = pokemon_char.name
        mega = pokemon_char.mega
        legendary = pokemon_char.legendary
        total_stat = pokemon_char.get_total_stats()

        if legendary == "TRUE":
            continue

        elif mega == "TRUE":
            mega_vs_non_mega_pokedex["Mega Pokemon"]["Count"] += 1
            mega_vs_non_mega_pokedex["Mega Pokemon"]["Total Stats"] += total_stat
        
        elif name in normal_pokemon:
            mega_vs_non_mega_pokedex["Non Mega Pokemon"]["Count"] += 1
            mega_vs_non_mega_pokedex["Non Mega Pokemon"]["Total Stats"] += total_stat

    mega_stats = mega_vs_non_mega_pokedex["Mega Pokemon"]["Total Stats"]
    mega_count = mega_vs_non_mega_pokedex["Mega Pokemon"]["Count"]

    non_mega_stats = mega_vs_non_mega_pokedex["Non Mega Pokemon"]["Total Stats"] 
    non_mega_count = mega_vs_non_mega_pokedex["Non Mega Pokemon"]["Count"]

    if mega_count == 0 or mega_stats == 0:
        return None
    elif non_mega_count == 0 or non_mega_stats == 0:
        return None
    mega_vs_non_mega_pokedex["Mega Pokemon"]["Avg Stats"] = mega_stats / mega_count
    mega_vs_non_mega_pokedex["Non Mega Pokemon"]["Avg Stats"] = non_mega_stats / non_mega_count

    return mega_vs_non_mega_pokedex


mega_vs_non_mega_pokedex = create_mega_vs_non_mega_pokedex(pokedex, pokedex_by_ID)
print(mega_vs_non_mega_pokedex)
print()



def calculate_difference_between_mega_and_non_mega_avg_stats(mega_vs_non_mega_pokedex):
    if mega_vs_non_mega_pokedex == None or len(mega_vs_non_mega_pokedex) == 0:
        return None

    for mega_status in mega_vs_non_mega_pokedex.keys():
        print(mega_status)

    mega_avg_stat = mega_vs_non_mega_pokedex["Mega Pokemon"]["Avg Stats"]
    non_mega_avg_stat = mega_vs_non_mega_pokedex["Non Mega Pokemon"]["Avg Stats"]
    difference = round(abs(mega_avg_stat - non_mega_avg_stat))

    return difference

difference_between_mega_and_non_mega_avg_stats = calculate_difference_between_mega_and_non_mega_avg_stats(mega_vs_non_mega_pokedex)
print(difference_between_mega_and_non_mega_avg_stats)


class TestCompareMegaPokemonToNonPokemonCounterparts(unittest.TestCase):
    print("------------------------------------------------------------------------")
    def test_return_none_if_there_are_no_mega_pokemon(self):
        pokedex = {
            Pokemon(5,"Charmeleon","Fire","",58,64,58,80,65,80,1,"FALSE","FALSE"),
        }
        pokedex_by_ID = {
            5: ["Charmeleon"]
        }
        expected = None 

        actual = create_mega_vs_non_mega_pokedex(pokedex, pokedex_by_ID)

        self.assertEqual(expected, actual)


    def test_return_none_if_there_are_non_mega_pokemon(self):
        pokedex = {
            Pokemon(6,"Mega Charizard X","Fire","Dragon",78,130,111,130,85,100,1,"FALSE","TRUE"),
        }
        pokedex_by_ID = {
            6: ["Mega Charizard X"]
        }
        expected = None 

        actual = create_mega_vs_non_mega_pokedex(pokedex, pokedex_by_ID)

        self.assertEqual(expected, actual)


    def test_return_none_if_mega_vs_non_mega_pokedex_is_empty(self):
        pokedex = {}
        expected = None
        
        actual = calculate_difference_between_mega_and_non_mega_avg_stats(pokedex)

        self.assertEqual(expected, actual)


    def test_return_0_if_both_mega_and_non_mega_have_the_same_avg_stats(self):
        pokedex = {
            'Mega Pokemon': {'Count': 1, 'Total Stats': 500, "Avg Stats": 500}, 
            'Non Mega Pokemon': {'Count': 1, 'Total Stats': 500, "Avg Stats": 500}
            }
        expected = 0

        actual = calculate_difference_between_mega_and_non_mega_avg_stats(pokedex)

        self.assertEqual(expected, actual)


    def test_return_difference_between_mega_and_non_mega_avg_stats(self):
        pokedex = {
            'Mega Pokemon': {'Count': 3, 'Total Stats': 1500, "Avg Stats": 500}, 
            'Non Mega Pokemon': {'Count': 4, 'Total Stats': 1000, "Avg Stats": 250}}
        expected = 250

        actual = calculate_difference_between_mega_and_non_mega_avg_stats(pokedex)

        self.assertEqual(expected, actual)       


    def test_return_difference_between_mega_and_non_mega_avg_stats_with_sample_data(self):
        print("------------------------------------------------------------------------")
        pokedex = create_pokedex()
        pokedex_by_ID = create_pokedex_by_ID(pokedex)
        print(pokedex_by_ID)
        mega_vs_non_mega_pokedex = create_mega_vs_non_mega_pokedex(pokedex, pokedex_by_ID)
        print()
        print(mega_vs_non_mega_pokedex)
        expected = 107

        actual = calculate_difference_between_mega_and_non_mega_avg_stats(mega_vs_non_mega_pokedex)

        self.assertEqual(expected, actual)   




if __name__ == "__main__":
    unittest.main()