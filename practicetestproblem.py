def add_a_capitol(a_dict, a_state, a_city):
    a_dict[a_state] = a_city

my_capitols = {"Georgia": "Atlanta", "Idaho": "Boise", "Maine": "Augusta"}
my_capitols = add_a_capitol(my_capitols, "Texas", "Austin")

print(my_capitols)

#Q: What would this return?
#A: Returns None