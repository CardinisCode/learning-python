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


def create_mega_vs_non_mega_dict(my_pokemon_collection):
    mega_vs_non_mega_dict = {}
    mega_vs_non_mega_dict["Mega"] = {
        "Total Power": 0, 
        "Total Count": 0, 
        "Avg Power": 0.0, 
    }
    mega_vs_non_mega_dict["Non-Mega"] = {
        "Total Power": 0,
        "Total Count": 0,
        "Avg Power": 0.0,
    }
    pokemon_by_ID_dict = {}

    for pokemon in my_pokemon_collection.values():
        pokemon_name = pokemon.name
        pokemon_ID = pokemon.id
        mega = pokemon.mega
        total_power = pokemon.get_total_power()
        #print(pokemon_ID, ":", pokemon_name, mega, total_power)
        #print()
        
        if pokemon.legendary == "TRUE":
            continue
        if not pokemon_ID in pokemon_by_ID_dict.keys():
            pokemon_by_ID_dict[pokemon_ID] = []
        
        pokemon_by_ID_dict[pokemon_ID].append(pokemon_name)
        
    for pokemon_names in pokemon_by_ID_dict.values():
        filter_names = []
        for name in pokemon_names:
            if my_pokemon_collection[name].mega == "TRUE":
                filter_names.append(name)

        #Alternative code for this above for-loop:
        # filter_names = [x for x in pokemon_names if x.startswith("Mega")]

        if len(filter_names) >= 1:
            local_mega = 0
            local_norm = 0
            for name in pokemon_names:
                
                total_power = my_pokemon_collection[name].get_total_power()
                if my_pokemon_collection[name].mega == "TRUE": 
                    local_mega += total_power
                    mega_vs_non_mega_dict["Mega"]["Total Power"] += total_power
                    mega_vs_non_mega_dict["Mega"]["Total Count"] += 1
                else: 
                    local_norm += total_power
                    mega_vs_non_mega_dict["Non-Mega"]["Total Power"] += total_power
                    mega_vs_non_mega_dict["Non-Mega"]["Total Count"] += 1
    
    non_mega_total_power = mega_vs_non_mega_dict["Non-Mega"]["Total Power"]
    non_mega_total_count = mega_vs_non_mega_dict["Non-Mega"]["Total Count"]
    non_mega_average = non_mega_total_power / non_mega_total_count
    mega_vs_non_mega_dict["Non-Mega"]["Avg Power"] = non_mega_average

    mega_total_power = mega_vs_non_mega_dict["Mega"]["Total Power"]
    mega_total_count = mega_vs_non_mega_dict["Mega"]["Total Count"]
    mega_average = mega_total_power / mega_total_count
    mega_vs_non_mega_dict["Mega"]["Avg Power"] = mega_average

    return mega_vs_non_mega_dict


def find_power_difference_mega_vs_non_mega(mega_vs_non_mega_dict):
    non_mega_average = mega_vs_non_mega_dict["Non-Mega"]["Avg Power"]
    mega_average = mega_vs_non_mega_dict["Mega"]["Avg Power"]
    power_difference = int(mega_average - non_mega_average)

    return power_difference


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
mega_vs_non_mega_dict = create_mega_vs_non_mega_dict(my_pokemon_collection)

power_difference_mega_vs_non_mega = find_power_difference_mega_vs_non_mega(mega_vs_non_mega_dict)
print(power_difference_mega_vs_non_mega)