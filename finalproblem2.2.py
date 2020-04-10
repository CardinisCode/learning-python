# Same problem as Final Problem 2, but to make things interesting we have
# to plan for a full name that includes more than 1 surname. 


#Add your code here!
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
    first_names_list = superhero_names[:middle_index]
    last_names_list = superhero_names[middle_index:]

    #Now to create 2 dictionaries to store our superhero names
    superhero_first_names = {}
    superhero_last_names = {}

    #So we can add these names into our dictionaries as the values
    # and the keys are the letters from our capital letters list:
    for i in range(len(first_names_list)):
        name = first_names_list[i].rstrip()
        superhero_first_names[list_of_letters[i]] = name

    for i in range(len(last_names_list)):
        name = last_names_list[i].rstrip()
        superhero_last_names[list_of_letters[i]] = name

#   Now to manipulate the fullname string:
    superhero_full_name = ""
    names = fullname.split(" ")
    first_name = names[0]
    first_name_initial = first_name[0]

    for letter, superhero_name in superhero_first_names.items():
        if letter == first_name_initial:
            superhero_full_name += superhero_name + " "

    last_names = names[1:]

    for last_name in last_names:
        last_name_initial = last_name[0]
        for letter, superhero_name in superhero_last_names.items():
            if letter == last_name_initial:
                superhero_full_name += superhero_name + " "

    return superhero_full_name.rstrip()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Captain Hawk, Doctor Yellow Jacket, and Moon Moon,
#each on their own line.
print(generate_name("heronames.txt", "Addison Zook"))
# Outputs: Captain Hawk
print(generate_name("heronames.txt", "Uma Irwin"))
# Outputs: Doctor Yellow Jacket
print(generate_name("heronames.txt", "David Joyner"))
# Outputs: Moon Moon
print(generate_name("heronames.txt", "Andrea Cardini Folgado"))
# Outputs: Captain Hulk Warriors
print(generate_name("heronames.txt", "Peter Daniel Van Onselen"))
# Outputs: Power Centurion Skull Doom
print(generate_name("heronames.txt", "Janine Van Der Merwe"))
# Outputs: Golden Skull Centurion Machine

number_of_lines = 57-6
print("Solved in", number_of_lines, "number of lines.")



