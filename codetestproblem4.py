#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!
def find_median(filename):
    number_file = open(filename, "r")
    file_contents = number_file.readlines()
    number_file.close()

    numbers_list = []
    for line in file_contents: 
        if "\n" in line: 
            line = line.strip("\n")
        number = int(line)
        numbers_list.append(number)
    numbers_list.sort()
    print("My list after sorting:", numbers_list)

    number_of_values = len(numbers_list)
    print("There are", number_of_values, "numbers in this file")

    half_way_value = 0.0
    if number_of_values % 2 == 0:
        half_way_point = round(number_of_values / 2) -1
        left = numbers_list[half_way_point]
        right = numbers_list[half_way_point + 1]
        print("Half way value #1", left)
        print("Half way value #2:", right)
        two_middle_values = left + right
        half_way_value = two_middle_values / 2
    else: 
        half_way_point = int(number_of_values / 2)
        print("Odd Half way point:", half_way_point)
        half_way_value = numbers_list[half_way_point]
    return half_way_value

#I'll keep the print statements in, as they were used to debug my code. 

#Areas of improvement: 
#1: Use variables more! 
#    - ie, when doing a calculation, put the value of that calcualtion 
#      into a variable. This prevents duplication and makes things easier
#      to debug

#2: I initally used round() on line 52 - but this rounds up to the next decimal
#   - Where int(value) will return just the integer part of the float.
#     eg: given 5.4, it will return 5, dropping everything after the "."
#     indirectly rounding down

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16
print(find_median("FindMedianInput.txt"))



