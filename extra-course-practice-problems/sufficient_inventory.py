#Imagine you're writing a program to check whether sufficient
#inventory exists to fill an incoming order at a store. Your
#current inventory comes in the form of a list of instances of
#an InventoryItem class.
#
#You don't have access to the code for the InventoryItem class.
#However, you know that it has at least two attributes:
#name (a string) and quantity (an integer). The name is the
#product's name, and the quantity is the current number of that
#item that are in stock.
#
#Write a function called sufficient_inventory.
#sufficient_inventory should take three parameters: a list of
#instances of InventoryItem representing the current inventory,
#an item name (a string), and a desired quantity (an integer).
#
#The function should return True if two conditions are met:
#
# (a) There exists an instance of InventoryItem in the list
#     whose name matches the the item name parameter.
# (b) The quantity associated with that instance is larger than
#     the desired quantity.
#
#For example, imagine we called:
#
# sufficient_inventory(my_items, "hat", 3)
#
#This would return True if one of the elements in my_items had
#a name attribute "hat" and a quantity attribute greater than
#or equal to 3. It would return False if either no item in
#my_items had the name "hat", or item with the name "hat"
#has a quantity less than 3.
#
#You may assume that each item name will appear only once in
#the list of InventoryItems, and that quantity will always be
#an integer greater than or equal to 0.
import unittest

#Write your function here!
def sufficient_inventory(current_inventory, item_name, desired_quantity):
    sufficient_stock = False
    for item in current_inventory:
        if item.name == item_name and item.quantity >= desired_quantity:
            sufficient_stock = True

    return sufficient_stock


#If you would like, you may implement the InventoryItem class as
#described and use it to test your code. This is not necessary
#to complete the problem, but it may help you debug. If you
#create a InventoryItem class, all you need is a constructor that
#assigns values to two attributes: self.name and self.quantity.

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    
class TestInventoryItem(unittest.TestCase):
    current_inventory = [InventoryItem("Shoe", 7), InventoryItem("Hat", 3), InventoryItem("Socks", 1)]

    def test_item_not_in_stock(self):
        expected = False
        actual = sufficient_inventory(self.current_inventory, "Underwear", 1)

        self.assertEqual(expected, actual)

    def test_item_found_insufficient_stock(self):
        expected = False
        actual = sufficient_inventory(self.current_inventory, "Socks", 2)

        self.assertEqual(expected, actual)

    
    def test_item_found_with_sufficient_quantity(self):
        expected = True
        actual = sufficient_inventory(self.current_inventory, "Hat", 2)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

    
