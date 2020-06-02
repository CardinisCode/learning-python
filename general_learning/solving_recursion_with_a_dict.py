# Looking through my study notes, I noticed they mentioned it was possible
# to solve fibonacci using a dictionary where 
#   - each key =  the index / location in the fibonacci sequence
#   - & the value = the value found at this location in the sequence

# so I was curious to see how I would 
# go about solving it. 
# This is my take on it: 

# Note with the default Fibonacci sequence, the first 2 numbers are pre-set 
# with the value: 1

def solving_fibonacci_1(n):
    fibonacci_seq = {
    0: 1, 
    1: 1, 
    }

    for i in range(0, n + 1):
        if not i in fibonacci_seq:
            fibonacci_seq[i] = fibonacci_seq[i -1] + fibonacci_seq[i -2]

    return fibonacci_seq[n]


print(solving_fibonacci_1(5))
print(solving_fibonacci_1(10))
print(solving_fibonacci_1(15))

def solving_fibonacci_2(n):
    fibonacci_seq = {
    0: 1, 
    1: 1, 
    }

    for i in range(0, n + 1):
        if n in fibonacci_seq: 
            return fibonacci_seq[n]

        if not i in fibonacci_seq:
            fibonacci_seq[i] = fibonacci_seq[i -1] + fibonacci_seq[i -2]

    return fibonacci_seq[n]

print()
print(solving_fibonacci_1(5))
print(solving_fibonacci_1(10))
print(solving_fibonacci_1(15))

# 