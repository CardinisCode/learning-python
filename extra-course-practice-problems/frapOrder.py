#Create a class called FrapOrder. FrapOrder should
#have two attributes (instance variables): size and
#extra_shots. Make sure the variable names match those
#words. size will be a character, either "S", "M", or "L".
#extra_shots will be an integer.
#
#FrapOrder should have a constructor with two required
#parameters, one for each of those attributes (size and
#extra_shots, in that order).
#
#FrapOrder should also have a method called get_total.
#get_total should calculate the total cost of the order.
#If size is "S", the base cost is 2.50. If the size is "M",
#the base cost is 3.50. If the size is "L", the base cost is
#4.50. Then, each extra shot costs $0.35.
#
#For example, if size is "M" and extra_shots is 2, then
#get_total would return 4.2: 3.50 + 0.70 = 4.20 (and Python
#drops trailing 0s).
#
#total should NOT be an attribute of the class; instead,
#total should be calculated and returned live when the method
#get_total is called.
#
#The get_total method should have NO parameters besides self.
#Instead, it should calculate the total based on the current
#values for the size and extra_shots attributes.
import unittest

#Write your class here!
class FrapOrder:
    def __init__(self, size, extra_shots):
        self.size = size
        self.extra_shots = extra_shots

    def get_total(self):
        base_price = 0
        if self.size == "S":
            base_price += 2.50
        elif self.size == "M":
            base_price += 3.50
        elif self.size == "L":
            base_price += 4.50

        if self.extra_shots >= 1:
            base_price += (self.extra_shots * 0.35)

        return base_price 


#The code below will test your function. If it works, it
#should print "M" (without the quotes), 2, and 4.2 in that
#order.
# test_order = FrapOrder("M", 2)
# print(test_order.size)
# print(test_order.extra_shots)
# print(test_order.get_total())


class TestFrapOrder(unittest.TestCase):
    def test_Small_order(self):
        test_order = FrapOrder("S", 1)
        expected = 2.85
        actual = test_order.get_total()

        self.assertEqual(expected, actual)


    def test_Med_order(self):
        test_order = FrapOrder("M", 2) 
        expected = 4.2
        actual = test_order.get_total()

        self.assertEqual(expected, actual)

    
    def test_Large_order(self):
        test_order = FrapOrder("L", 3) 
        expected = 5.55
        actual = actual = test_order.get_total()

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()