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
    pseudo_fibonacci = []
    fibonacci_length = len(fibonacci_list)
    print("The current list length has", fibonacci_length, "numbers")

    for i in fibonacci_list:
        pseudo_fibonacci.append(i)

    first_number = fibonacci_list[fibonacci_length -2]
    second_number =fibonacci_list[fibonacci_length -1] 
    print("My first number:", first_number, "and my second number:", second_number)
    
    for i in range(0, n):
        next_number = first_number + second_number
        pseudo_fibonacci.append(next_number)
        first_number = second_number
        second_number = next_number
    
    p_fibonacci_length = len(pseudo_fibonacci)
    print("There are", p_fibonacci_length, "numbers in this list")

    return pseudo_fibonacci

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#If your function works correctly, this will originally
#print:
a_list = [8, 10]
print(next_fib(a_list, 4))







