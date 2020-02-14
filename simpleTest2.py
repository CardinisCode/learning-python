#Just to test things as i work with them 
import random
myString = "Ilike2flossdaily" 
my_new_string = ""
shuffle_my_string = list(myString)
random.shuffle(shuffle_my_string)

for i in shuffle_my_string: 
    my_new_string += ''.join(i)

print(my_new_string)

new_word = "tree" + "Hug"
print(new_word)
new_word = new_word[0].upper() + new_word[1:].lower()
print(new_word)
