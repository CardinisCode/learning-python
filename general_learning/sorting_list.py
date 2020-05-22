random_integers = [6, 3, 0, 1, 10, 4]
random_mixed_strings = ["a", "t", "h", "5", "T", ":", ",", "e"]
random_words = ["happy", "cat", "purrs", "delightfully", "by", "my", "side"]

print("Lets print the these lists in ascending/alphabetical order")
random_integers.sort()
print("random_integers:", random_integers)
random_mixed_strings.sort()
print("random_mixed_strings:", random_mixed_strings)
random_words.sort()
print("random_words:", random_words)

# Note to self: 
# Sorting a list of random characters will sort them according to their ascii value 

print()
print("Now lets sort in reverse")
random_integers.sort(reverse=True)
print("random_integers in reverse:", random_integers)
random_mixed_strings.sort(reverse=True)
print("random_mixed_strings in reverse:", random_mixed_strings)
random_words.sort(reverse=True)
print("random_words in reverse:", random_words)

# Note to self: 
# sort is a method with 2 keyword parameters: key=None and reverse=True
# when we use sort(), we're saying we'll use the default values for these parameters. 
# So they're optional - we can change them or just leave the argument () empty

# reverse=True -> means that it will sort in reverse order 





