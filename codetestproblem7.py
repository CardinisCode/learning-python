#APA citation style cites author names like this:
#
#  Last, F., Joyner, D., & Burdell, G.
#
#Note the following:
#
# - Each individual name is listed as the last name, then a
#   comma, then the first initial, then a period.
# - The names are separated by commas, including the last
#   two.
# - There is also an ampersand and additional space before
#   the final name.
# - There is no space or comma following the last period.
#
#Write a function called names_to_apa. names_to_apa should
#take as input one string, and return a reformatted string
#according to the style given above. You can assume that
#the input string will be of the following format:
#
#  First Last, David Joyner, and George Burdell
#
#You may assume the following:
#
# - There will be at least three names, with "and" before
#   the last name.
# - Each name will have exactly two words.
# - There will be commas between each pair of names.
# - The word 'and' will precede the last name.
# - The names will only be letters (no punctuation, special
#   characters, etc.), and first and last name will both be
#   capitalized.


#Write your function below!
def names_to_apa(string_of_names): 
    reformatted_string = ""
    split_string = string_of_names.split(",")
    split_string_length = len(split_string)

    reformatted_string = ""
    for i in range(0, split_string_length):
        last_section = split_string_length -1
        if i == last_section: 
            and_char = split_string[i].split()[0]
            first_name = split_string[i].split()[1]
            surname = split_string[i].split()[2]
            and_char = and_char.replace("and", "&")
            first_name = first_name[0] + "."
            split_string[i] = and_char + " " + surname + ", " + first_name
            reformatted_string += split_string[i]

        else: 
            first_name = split_string[i].split()[0]
            surname = split_string[i].split()[1]
            first_name = first_name[0] + "."
            split_string[i] = surname + ", " + first_name
            print("Section:", i, ":", split_string[i])
            reformatted_string += split_string[i] +  ", " 

    return reformatted_string


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Dell, I., Vanzant, L., Cooley, J., Hamilton, M., & Minsky, M."
print(names_to_apa("Irmgard Dell, Leandro Vanzant, James Cooley, Margaret Hamilton, and Marvin Minsky"))



