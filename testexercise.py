def tri(n):
    if n == 1:
        return 1
    else:
        return n + tri(n -1)


#print("Option 2:", tri(5))

def tri2(n):
    if n > 1:
        return n + tri(n -1)
    else:
        return 1

#print("Option 4:", tri2(5))

def binary_search(n):
    count = 0
    myList = []
    if n == 1:
        myList.append(n)
        return 1
    elif n > 1: 
        middle = n // 2
        count +=1 
        myList.append(binary_search(middle))
    return (count, myList)

print(binary_search(9976))