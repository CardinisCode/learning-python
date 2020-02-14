import unittest

#Write a function called st_dev. st_dev should have one
#parameter, a filename. The file will contain one integer on
#each line. The function should return the population standard
#deviation of those numbers.
#
#The formula for population standard deviation can be found here:
#edge.edx.org/asset-v1:GTx+gt-mooc-staging1+2018_T1+type@asset+block@stdev.PNG
#
#The formula is a bit complex, though, and since this is a
#CS class and not a math class, here are the steps you would
#take to calculate it manually:
#
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.
#
#You may assume for this problem that the file will contain
#only integers -- you don't need to worry about invalid
#files or lines. The easiest way to take the square root is
#to raise it to the 0.5 power (e.g. 2 ** 0.5 will give the
#square root of 2).
#
#HINT: You might find this easier if you load all of the
#numbers into a list before trying to calculate the average.
#Either way, you're going to need to loop over the numbers
#at least twice: once to calculate the mean, once to
#calculate the sum of the differences.

def find_mean(number_list):
    total = 0.0
    for number in number_list:
        total += number
    return total / len(number_list)

def calc_difference_squared(mean, data_point):
    difference = abs(mean - data_point)
    return difference ** 2

def calc_standard_deviation(number_list):
    mean = find_mean(number_list)

    running_sum_of_differences = 0.0
    for number in number_list:
        running_sum_of_differences += calc_difference_squared(mean, number)
    
    return (running_sum_of_differences / len(number_list)) ** 0.5


class TestStDev(unittest.TestCase):
    def test_should_find_the_mean_of_the_list(self):
        number_list = [23, 58, 21, 15, 38, 86, 18, 74, 98, 28, 21, 58]

        self.assertEquals(find_mean(number_list), 44.833333333333336)

    def test_should_find_the_diff_between_mean_and_square_the_result(self):
        mean = 3
        data_point = 1

        self.assertEquals(calc_difference_squared(mean, data_point), 4)

    def test_should_return_the_standard_deviation_given_a_number_list(self):
        number_list = [23, 58, 21, 15, 38, 86, 18, 74, 98, 28, 21, 58]

        self.assertEqual(calc_standard_deviation(number_list), 27.796382658340438)


if __name__ == '__main__':
    unittest.main()
