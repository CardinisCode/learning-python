#Recall in 5.2.4 Worked Example 1, we gave you the code for
#merge_sort. You may copy that code into this problem and
#modify it. Change it such that instead of sorting from
#lowest to highest, it sorts from highest to lowest.
#
#Name your function sort_with_merge(). For example, if you call
#merge_sort([5, 3, 1, 2, 4]), you would get [5, 4, 3, 2, 1].
#
#Do not use Python's sort or reverse methods to complete
#this.


#Write your code below!
def sort_with_merge(to_sort_list):
    if len(to_sort_list) <= 1:
        return to_sort_list
    else: 
        midpoint = len(to_sort_list) // 2
        #print("Our current mid point is:", midpoint)
        left = sort_with_merge(to_sort_list[:midpoint])
        #print("our items to the left:", left)
        right = sort_with_merge(to_sort_list[midpoint:])
        #print("Our items to the right", right)

        sorted_list = []
        while len(left) and len(right) >0:
            if left[0] > right[0]:
                #print("left:", left[0], "and right:", right[0] )
                sorted_list.append(left[0])
                del left[0]
            else:
                sorted_list.append(right[0])
                del right[0]
        sorted_list.extend(left)
        sorted_list.extend(right)

    return sorted_list

#My notes: 
# I made a few tweaks to their original code, including 
# changing the variable names (relevant to the situation)
# and changed '<' to '>' 
# So where usually left[0] would be smaller than right[0], 
# This situation asks us to sort from the highest down to the lowest
# So now we're asking if left[0] is higher than right[0]. 
# Hence: 
# if left[0] > right[0]:

# If yes, left[0] is added to the new list sorted_list, 
# before being removed from the current list 'left'.
# If not, then right[0] is added to  sorted_list, 
# before being deleted from 'right'. 

# We delete the higher number (from the perspective left/right list) 
# so that our comparison if statement (Line 27) 
# is always dealing with the first number in each list.
# Once we find that the first number is the highest no. in the comparison,
# we delete it so we can move onto the next number in the list. 



#The code below will test your function. If it works, this
print(sort_with_merge([1, 3, -1, -3, -5, 5]))
#will print [5, 3, 1, -1, -3, -5].


# 5.2.4 Worked Example 1:
# def mergesort(lst):
    # if len(lst) <= 1:
        # return lst
    
    # else:
        # midpoint = len(lst) // 2
        # left = mergesort(lst[:midpoint])
        # right = mergesort(lst[midpoint:])

        # newlist = []
        # while len(left) and len(right) > 0:
            # if left[0] < right[0]:
                # newlist.append(left[0])
                # del left[0]

            # else:
                # newlist.append(right[0])
                # del right[0]

        # newlist.extend(left)
        # newlist.extend(right)

        # return newlist


