You are receiving an int n and an array of integers m as parameters. You need to calculate the sum of the int received as first parameter in the function and all integers from the array that are exactly divisible with 2.

The array received can have minimum 0 and maximum 1000 elements. If the constrain is not satisfied return only the int received as parameter.

You can change the programming language you want to use from the top right corner of the IDE.
We'd recommend you use the IDE on hackajob as this will allow the hiring managers to review your complete solution once you submit it. However, if you'd prefer, you can complete the challenge in your own IDE and copy the solution into the IDE on hackajob. If you do this, please make sure that the main class and method are in the same structure.
Use the Run function to check if your code is passing the example test cases.
INPUT

int n
[]int m
OUTPUT

int total
EXAMPLE 1

Input: 1, [1,2,3,4]
Output: 7
^ the output is 7 because 1 (the first parameter of function) + 2 (is divisible by 2) + 4 (is divisible by 2) = 7
EXAMPLE 2

Input: 2, [1,3]
Output: 2
^ the output is 2 because 2 (the first parameter of function) is the only integer added to the final result, 1 is not divisible by 2 and 3 is not divisible by 2
CONSTRAINTS

m can have between 0 and 1000 elements