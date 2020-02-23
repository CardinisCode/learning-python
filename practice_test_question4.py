file_to_open = "test_data.csv"

def lets_write_to_file(filename): 
    openFile = open(filename)
    
    count = 0
    sum = 0

    for num in openFile:
        sum += num
        count += 1
    print(sum/count)

    openFile.close()
    



print(lets_write_to_file(file_to_open))