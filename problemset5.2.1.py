#We've started a recursive function below called
#measure_string that should take in one string parameter,
#myStr, and returns its length. However, you may not use
#Python's built-in len function.
#
#Finish our code. We are missing the base case and the
#recursive call.
#
#HINT: Often when we have recursion involving strings, we
#want to break down the string to be in its simplest form.
#Think about how you could splice a string little by little.
#Then think about what your base case might be - what is
#the most basic, minimal string you can have in python?
#
#Hint 2: How can you establish the base case has been
#reached without the len() function?

#You may not use the built-in 'len()' function.

#def measure_string(myStr):
    #if #Complete this line!
    	#return #Complete this line!
    #else:
        #return #Compulete this line!
    
    
#The line below will test your function. As written, this
#should print 13. You may modify this to test your code.

def measure_string(myStr):
    print("Just as a test, our string is:", len(myStr), "Characters long.")
    if myStr == "":
        return 0
        
    else:
        return 1 + measure_string(myStr[:-1])


#To make things easier to read when they print to console:
print()
print("Lets start...")
#To make sure the if statement works as we expect:
print(measure_string(""))
print(measure_string("13 characters too long"))

#My notes to future self:

#For the base case: 
# Think what is the lowest number of characters a string could possibly have? 
# Answer: 0 / An empty string

# For the recursive function: 
# To build a tally without using count(), len() or a for-loop,
# you have to add 1 before the recursive function call, in the tail
# Then, as the value for recursive function call: slice the string by 1
# value (for function call) = string sliced by 1 (its last character)
# So as the tally builds up (+1), the string itself becomes (-1) shorter
# Thus ensuring the recursive loop will end once it has gone through the full length
# Of the string in question (and not looping infinitely...)

