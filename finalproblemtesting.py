def generate_name(filename, fullname):
    superhero_file = open(filename, "r")
    superhero_names = []

    #To extract the lines into a list of names
    for line in superhero_file:
        superhero_names.append(line)
    superhero_file.close()

    # Lets create a list with the capital letters from A to Z:
    list_of_letters = []
    for i in range(65, 91):
        list_of_letters.append(chr(i))

    #To split our list of superhero names into 2 smaller lists:
    middle_index = len(superhero_names) // 2
    first_names = superhero_names[:middle_index]
    last_names = superhero_names[middle_index:]

    #Now to create 2 dictionaries to store our superhero names
    superhero_first_names = {}
    superhero_last_names = {}

    #So we can add these names into our dictionaries as the values
    # and the keys are the letters from our capital letters list:
    for i in range(len(first_names)):
        name = first_names[i].rstrip()
        superhero_first_names[list_of_letters[i]] = name

    for i in range(len(last_names)):
        name = last_names[i].rstrip()
        superhero_last_names[list_of_letters[i]] = name

    number_of_names = fullname.count(" ") + 1
    print("We have", number_of_names, "names in our fullname")

    superhero_full_name = ""
    first_name = fullname.split(" ")[0]
    first_name_initial = first_name[0]
    print("Our first name is:", first_name)
    
    if number_of_names == 2:
        last_name = fullname.split(" ")[1]
        last_name.initial = last_name[0]

    elif number_of_names >= 3:
        

    for letter, superhero_name in superhero_first_names.items():
        if letter == first_name_initial:
            superhero_full_name += superhero_name + " "





    return superhero_full_name

print(generate_name("heronames.txt", "Andrea Folgado"))
print(generate_name("heronames.txt", "Peter Van Onselen"))