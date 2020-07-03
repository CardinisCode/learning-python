#Imagine you're writing a program to check registration status
#at a conference. The list of registrants comes in the form of
#a list of instances of the Registrant class.
#
#You don't have access to the code for the Registrant class.
#However, you know that it has at least two attributes:
#name (a string) and authorized (a boolean).
#
#Write a function called is_authorized. is_authorized should
#take two parameters: a list of instances of Registrant
#representing the registered individuals, and a name as a
#string.
#
#The function should return True if _any_ instance in the list
#has the same name and an authorized status of True. It should
#return False if either (a) no instance in the list of
#registrants has the same name, or (b) the instance with the
#same name has an authorized status of False.
#
#You should not assume that the list of registrants is sorted
#in any way.
#
#Hint: Beware of registrants who appear in the list twice with
#different values for authorized. If _any_ instance has a
#the value True for authorized, the function should return True.
import unittest

#Write your function here!

# My 2nd pass at this challenge: 
# I am really happy I managed to bring this from 20 lines of code down to 5 lines! 
def is_authorized(registration, current_name):
    for individual in registration:
        if individual.name == current_name and individual.authorized == True:
            return True 
    return False 


# My first pass  at this challenge: 
# def check_guest_is_registered(registered_guests, current_guest):
#     guest_is_registered = False
#     authorized = False

#     for guest in registered_guests:
#         guest_name = guest.name
#         if guest_name == current_guest:
#             guest_is_registered = True
#             authorized = guest.authorized
        
#     return (guest_is_registered, authorized)


# def is_authorized(registered_guests, current_guest):
#     guest_is_registered, guest_is_authorized = check_guest_is_registered(
#         registered_guests, current_guest)

#     if guest_is_registered and guest_is_authorized:
#         return True

#     return False


#If you would like, you may implement the Registrant class as
#described and use it to test your code. This is not necessary
#to complete the problem, but it may help you debug. If you
#create a Registrant class, all you need is a constructor that
#assigns values to two attributes: self.name and self.authorized.

class Registrant:
    def __init__(self, name, authorized):
        self.name = name
        self.authorized = authorized


registered_guests = [
    Registrant("Harry Williams", True), 
    Registrant("Mary Oliver", False), 
    Registrant("Martha Jones", False),
    Registrant("Harry Potter", True)
]

check_current_guest_is_welcome = is_authorized(registered_guests, "Martha Jones")
print(check_current_guest_is_welcome)

class TestRegistrant(unittest.TestCase):
    guests_registered = [Registrant("Harry Williams", True), Registrant("Mary Oliver", False), Registrant("Harry Potter", True)]

    def test_guest_not_registered(self):
        print("----------------------------------------------------")
        expected = False
        actual = is_authorized(self.guests_registered, "John Smith")

        self.assertEqual(expected, actual)


    def test_guest_registered_not_authorized(self):
        print("----------------------------------------------------")
        expected = False
        actual = is_authorized(self.guests_registered, "Mary Oliver")

        self.assertEqual(expected, actual)


    def test_guest_registered_and_authorized(self):
        print("----------------------------------------------------")
        expected = True
        actual = is_authorized(self.guests_registered, "Harry Williams")

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()