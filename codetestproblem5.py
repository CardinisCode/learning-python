#Write a function called next_fib. next_fib should take
#have two parameters: a list of integers and a single integer.
#For this description, we'll call the single integer n.
#
#next_fib should modify the list to add the next n pseudo-
#Fibonacci numbers to the end of the sequence. A pseudo-
#Fibonacci number is the sum of the previous two numbers in
#the sequence, but in our case, the previous two numbers may
#not be the original numbers from the Fibonacci sequence.
#
#For example, if the original list given was:
#
# a_list = [5, 5, 10, 15, 25, 40, 65]
#
# Then next_fib(a_list, 3) would return:
#       [5, 5, 10, 15, 25, 40, 65, 105, 170, 275]
#
#All the original numbers in the list are still there, and
#three new ones have been added.
#
#You may assume the list parameter will always have at least
#two numbers.
#
#HINT: Python gets mad if you try to change a list while
#iterating over it with a for-each loop. You'll have to get
#clever with a for or while loop to do this!


#Add your code here!
def next_fib(fibonacci_list, n):
    fibonacci_length = len(fibonacci_list)
    while fibonacci_length <= (fibonacci_length + 3): 
        last_number = fibonacci_list[fibonacci_length -1]
        print(last_number)
        next_fibonacci = last_number + fibonacci_list[fibonacci_length -2]
        fibonacci_list.append(next_fibonacci)
        fibonacci_length += 1
    
    #pseudo_fibonacci = []
    #for i in fibonacci_list:
        #pseudo_fibonacci.append(i)

    #p_fibonacci_length = len(pseudo_fibonacci)
    #print("There are", p_fibonacci_length, "numbers in this list")


    #return pseudo_fibonacci
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#If your function works correctly, this will originally
#print:
#[5, 5, 10, 15, 25, 40, 65, 105, 170, 275] 
a_list = [5, 5, 10, 15, 25, 40, 65]
print(next_fib(a_list, 3))






