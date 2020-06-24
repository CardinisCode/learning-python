#Write a function called rabbit_hole. rabbit_hole should have
#two parameters: a dictionary and a string. The string may be
#a key to the dictionary. The value associated with that key,
#in turn, may be another key to the dictionary.
#
#Keep looking up the keys until you reach a key that has no
#associated value. Then, return that key.
#
#For example, imagine if you had the following dictionary.
#This one is sorted to make this example easier to follow:
#
# d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
#      "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
#      "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
#      "rat": "ram", "ram": "rat"}
#
#If we called rabbit_hole(d, "bat"), then our code should...
#
# - Look up "bat", and find "pig"
# - Look up "pig", and find "cat"
# - Look up "cat", and find "dog"
# - Look up "dog", and find "ant"
# - Look up "ant", and find no associated value, and so it would
#   return "ant".
#
#Other possible results are:
#
# rabbit_hole(d, "bat") -> "fly"
# rabbit_hole(d, "ewe") -> "hen"
# rabbit_hole(d, "jay") -> "doe"
# rabbit_hole(d, "yak") -> "yak"
#
#Notice that if the initial string passed in is not a key in
#the dictionary, that string should be returned as the result as
#well.
#
#Note, however, that it is possible to get into a loop. In the
#dictionary above, rabbit_hole(d, "rat") would infinitely go
#around between "rat" and "ram". You should prevent this: if a
#key is ever accessed more than once (meaning a loop has been
#reached), return the boolean False.
#
#Hint: If you try to access a value from a dictionary that does
#not exist, a KeyError will be raised.


import unittest
#Write your function here!
# With my 2nd pass at this challenge, I came to the same solution with slightly different naming of the variables. 
# I did however solve this a lot quicker than I did the first time :D 

def rabbit_hole(animal_dict, animal):
    try:
        current_animal = animal_dict[animal]
        return rabbit_hole(animal_dict, current_animal)

    except RecursionError:
        return False 
    
    except KeyError:
        return animal


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ant, hen, doe, yak, False, each on their own line.
d = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

print(rabbit_hole(d, "bat"))
print(rabbit_hole(d, "ewe"))
print(rabbit_hole(d, "jay"))
print(rabbit_hole(d, "yak"))
print(rabbit_hole(d, "rat"))


class TestRabbitHole(unittest.TestCase):
    dictionary = {"bat": "pig", "pig": "cat", "cat": "dog", "dog": "ant",
     "cow": "bee", "bee": "elk", "elk": "fly", "ewe": "cod",
     "cod": "hen", "hog": "fox", "fox": "jay", "jay": "doe",
     "rat": "ram", "ram": "rat"}

    def test_key_not_present_in_dictionary(self):
        print("-----------------------------")
        expected = "yak"
        actual = rabbit_hole(self.dictionary, "yak")
        
        self.assertEqual(expected, actual)

    def test_key_bat_returns_ant(self):
        expected = "ant"
        actual = rabbit_hole(self.dictionary, "bat")
        
        self.assertEqual(expected, actual)

    



if __name__ == "__main__":
    unittest.main()