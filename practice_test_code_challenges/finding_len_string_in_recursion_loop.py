#Challenge: 
    #Finding the length of a string using recursion but without using len()

def measure_string(myStr):
    count = 0
    
    if myStr == myStr[-1]:
        return count + 1

    else:
        return 1 + measure_string(myStr[1:])

print(measure_string("13 characters"))