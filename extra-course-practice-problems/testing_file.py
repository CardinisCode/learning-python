new_list = [9, 12, 13, 13, 15, 15, 19, 21, 23, 25, 25, 27, 27, 28, 29, 29, 30, 33, 33, 40]

def find_item_using_binary_search(new_list, search_term, checks_done):
    mid_index = len(new_list) // 2
    mid_value = new_list[mid_index]
    print(mid_value, "at index", mid_index)
    checks_done += 1
    print("checks_done so far:", checks_done)


    if mid_value == search_term:
        return mid_index, checks_done

    elif len(new_list) == 1 and not mid_value == search_term:
        return -1

    elif mid_value > search_term:
        list_to_search = new_list[:mid_index]
        return find_item_using_binary_search(list_to_search, search_term, checks_done)
    
    elif mid_value < search_term:
        return find_item_using_binary_search(new_list[mid_index:], search_term, checks_done)


checks_done = 0
print("Checking my list for 33:", find_item_using_binary_search(new_list, 33, checks_done))
print()
print("Checking my list for 100:", find_item_using_binary_search(new_list, 100, checks_done))