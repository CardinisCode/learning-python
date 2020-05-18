#The game Uno is a card game where each player's goal is
#to get rid of all their cards. A round ends when one player
#has gotten rid of all their cards. They then receive a
#number of points based on the cards left in their opponents'
#hands. The first player to reach 500 points across multiple
#rounds wins the game.
#
#Write a function called check_uno_winner. This function will
#take as input a tuple with at least 2 integers, but up to 8.
#Each integer will represent one player's score.
#
#If any player has more than 500 points, check_uno_winner
#should return the string, "Player X wins!", where X refers
#to the position of the player in the list who has more than
#500 points. Because Uno is played in the real world, the
#first player in the list should be referred to as Player 1,
#the second player as Player 2, and so on.
#
#If no player has more than 500 points, check_uno_winner
#should return the string, "Keep playing!"
#
#For example:
# check_uno_winner((0, 0)) -> "Keep playing!"
# check_uno_winner((505, 250)) -> "Player 1 wins!"
# check_uno_winner((250, 505)) -> "Player 2 wins!"
# check_uno_winner((25, 101, 362, 415)) -> "Keep playing!"
# check_uno_winner((25, 101, 426, 515)) -> "Player 4 wins!"
#
#Remember, the function should RETURN these strings, not
#print them. You may assume that only one player will have
#a score above 500.

import unittest
#Write your function here!
def check_uno_winner(scoreboard):
    end_message = "Keep playing!"
    highest_score = None

    for index in range(0, len(scoreboard)):
        score = scoreboard[index]
        if score >= 500:
            if highest_score == None or highest_score > score:
                highest_score = score
                end_message = "Player " + str(index +1) + " wins!"

    return end_message





#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same output as the examples above.
print(check_uno_winner((0, 0)))



class TestUnoWinner(unittest.TestCase):
    def test_no_winner(self): 
        expected = "Keep playing!"
        actual = check_uno_winner((0, 0))

        self.assertEqual(expected, actual)


    def test_player_1_wins_with_2_players(self):
        expected = "Player 1 wins!"
        actual = check_uno_winner((505, 250))

        self.assertEqual(expected, actual)

    
    def test_player_2_wins_with_2_players(self):
        expected = "Player 2 wins!"
        actual = check_uno_winner((250, 505))

        self.assertEqual(expected, actual)    


    def test_player_no_winner_with_4_players(self):
        expected = "Keep playing!"
        actual = check_uno_winner((25, 101, 362, 415))

        self.assertEqual(expected, actual)   

    def test_player_4_wins_with_4_players(self):
        expected = "Player 4 wins!"
        actual = check_uno_winner((25, 101, 426, 515))

        self.assertEqual(expected, actual) 


if __name__ == "__main__":
    unittest.main()