# Final Problem #2 - out of a set of 10. 

#A common meme on social media is the name generator. These
#are usually images where they map letters, months, days,
#etc. to parts of fictional names, and then based on your
#own name, birthday, etc., you determine your own.
#
#For example, here's one such image for "What's your
#superhero name?": https://i.imgur.com/TogK8id.png
#
#Write a function called generate_name. generate_name should
#have two parameters, both strings. The first string will
#represent a filename from which to read name parts. The
#second string will represent an individual person's name,
#which will always be a first and last name separate by a
#space.
#
#The file with always contain 52 lines. The first 26 lines
#are the words that map to the letters A through Z in order
#for the person's first name, and the last 26 lines are the
#words that map to the letters A through Z in order for the
#person's last name.
#
#Your function should return the person's name according to
#the names in the file.
#
#For example, take a look at the names in heronames.txt
#(look in the drop-down in the top left). If we were to call
#generate_name("heronames.txt", "Addison Zook"), then the
#function would return "Captain Hawk": Line 1 would map to
#"A", which is the first letter of Addison's first name, and
#line 52 would map to "Z", which is the first letter of
#Addison's last name. The contents of those lines are
#"Captain" and "Hawk", so the function returns "Captain Hawk".
#
#You should assume the contents of the file will change when
#the autograder runs your code. You should NOT assume
#that every name will appear only once. You may assume that
#both the first and last name will always be capitalized.
#
#HINT: Use chr() to convert an integer to a character.
#chr(65) returns "A", chr(90) returns "Z".


#Add your code here!
def generate_name(filename, fullname):
    superhero_file = open(filename, "r")
    superhero_names = []
    for line in superhero_file:
        superhero_names.append(line)
    superhero_file.close()

    list_of_letters = []
    for i in range(65, 91):
        list_of_letters.append(chr(i))

    middle_index = len(superhero_names) // 2
    first_names = superhero_names[:middle_index]
    last_names = superhero_names[middle_index:]

    superhero_first_names = {}
    superhero_last_names = {}

    for i in range(len(first_names)):
        name = first_names[i].rstrip()
        superhero_first_names[list_of_letters[i]] = name

    for i in range(len(last_names)):
        name = last_names[i].rstrip()
        superhero_last_names[list_of_letters[i]] = name

    first_name, last_name = fullname.split(" ")
    first_name_initial = first_name[0]
    last_name_initial = last_name[0]
    superhero_full_name = ""

    superhero_full_name += superhero_first_names[first_name_initial] + " "
    superhero_full_name += superhero_last_names[last_name_initial]

    return superhero_full_name

# Note to self:
# I created my for loops to run from the top left of the tuple 
# down to the bottom right, as I am working with pre-collected data
# However if i was to create the actual game, including the player moves
# I would actually run this loop in reverse
# From the bottom up to the top row - to fit in with the how the game works

# Peter actually created this game using classes and unittests. 



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Captain Hawk, Doctor Yellow Jacket, and Moon Moon,
#each on their own line.
print(generate_name("heronames.txt", "Addison Zook"))
print(generate_name("heronames.txt", "Uma Irwin"))
print(generate_name("heronames.txt", "David Joyner"))
print(generate_name("heronames.txt", "Andrea Folgado"))
print(generate_name("heronames.txt", "Peter VanOnselen"))

number_of_lines = 85-46
print("Solved in", number_of_lines, "number of lines.")



