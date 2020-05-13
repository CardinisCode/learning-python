import unittest
#In volleyball, the first team to score 25 points wins.
#However, they must win by 2. So, if the score is 25-24,
#they keep playing until someone is ahead by 2 points.
#
#Write a function called check_volleyball_winner. This
#function will take as input a 2-tuple of two integers: the
#first integer is Team 1's score, and the second integer
#is Team 2's score. check_volleyball_winner should return a
#string:
#
# - If Team 1 has won, return "Team 1 wins!"
# - If Team 2 has won, return "Team 2 wins!"
# - If neither player has won, return "Keep playing!"
#
#For example:
# check_volleyball_winner((23, 17)) -> "Keep playing!"
# check_volleyball_winner((25, 17)) -> "Team 1 wins!"
# check_volleyball_winner((23, 25)) -> "Team 2 wins!"
# check_volleyball_winner((25, 24)) -> "Keep playing!"
# check_volleyball_winner((29, 29)) -> "Keep playing!"
# check_volleyball_winner((29, 30)) -> "Keep playing!"
# check_volleyball_winner((29, 31)) -> "Team 2 wins!"
#
#Remember, the function should RETURN these strings, not
#print them.


#Write your function here!
def check_volleyball_winner(scoreboard):
    player_1, player_2 = scoreboard
    difference = abs(player_1 - player_2)

    if player_1 < 25 and player_2 < 25:
        return "Keep playing!"

    elif player_1 == player_2: 
        return "Keep playing!"

    elif player_1 > player_2 and difference >= 2:
        return "Team 1 wins!"

    elif player_2 > player_1 and difference >= 2:
        return "Team 2 wins!"

    return "Keep playing!"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same output as the examples above.
print(check_volleyball_winner((23, 17)))
print(check_volleyball_winner((25, 17)))
print(check_volleyball_winner((23, 25)))
print(check_volleyball_winner((25, 24)))
print(check_volleyball_winner((29, 29)))
print(check_volleyball_winner((29, 30)))
print(check_volleyball_winner((29, 31)))




class TestCheckVolleyballWinner(unittest.TestCase):


    def test_keep_playing(self):
        print("----------------------------------------")
        expected = "Keep playing!"
        actual = check_volleyball_winner((29, 29))

        self.assertEqual(expected, actual)


    def test_player_1_wins_but_has_less_than_25_points(self):
        print("----------------------------------------")
        expected = "Keep playing!"
        actual = check_volleyball_winner((23, 17))

        self.assertEqual(expected, actual)

    def test_player_2_wins_but_has_less_than_25_points(self):
        print("----------------------------------------")
        expected = "Keep playing!"
        actual = check_volleyball_winner((17, 23))

        self.assertEqual(expected, actual)


    def test_player_1_wins_but_difference_is_less_than_2(self):
        print("----------------------------------------")
        expected = "Keep playing!"
        actual = check_volleyball_winner((25, 24))

        self.assertEqual(expected, actual) 


    def test_player_2_wins_but_difference_is_less_than_2(self):
        print("----------------------------------------")
        expected = "Keep playing!"
        actual = check_volleyball_winner((24, 25))

        self.assertEqual(expected, actual) 



if __name__ == "__main__":
    unittest.main()