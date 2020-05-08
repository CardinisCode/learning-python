#In ping-pong (table tennis), the first person to score 21
#points wins. However, they must win by 2. So, if the score
#is 21-20, they keep playing until someone is ahead by 2
#points.
#
#Write a function called check_pingpong_winner. This
#function will take as input a 2-tuple of two integers: the
#first integer is Player 1's score, and the second integer
#is Player 2's score. check_pingpong_winner should return a
#string:
#
# - If Player 1 has won, return "Player 1 wins!"
# - If Player 2 has won, return "Player 2 wins!"
# - If neither player has won, return "Keep playing!"
#
#For example:
# check_pingpong_winner((19, 13)) -> "Keep playing!"
# check_pingpong_winner((21, 13)) -> "Player 1 wins!"
# check_pingpong_winner((19, 21)) -> "Player 2 wins!"
# check_pingpong_winner((21, 20)) -> "Keep playing!"
# check_pingpong_winner((25, 25)) -> "Keep playing!"
# check_pingpong_winner((25, 27)) -> "Player 2 wins!"
#
#Remember, the function should RETURN these strings, not
#print them.

import unittest

#Write your function here!
def check_pingpong_winner(score_board):
    player_1_score = score_board[0]
    player_2_score = score_board[1]
    difference = abs(player_1_score - player_2_score)

    if difference < 2: 
        return "Keep playing!"

    elif player_1_score > player_2_score and player_1_score >= 21:
        return "Player 1 wins!"

    elif player_2_score > player_1_score and player_2_score >= 21:
        return "Player 2 wins!"

    return "Keep playing!"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same output as the examples above.




class TestThePingPong_Scoreboard(unittest.TestCase):

    def test_difference_less_than_2(self): 
        expected = "Keep playing!"
        actual = check_pingpong_winner((21, 20))
        self.assertEqual(expected, actual)


    def test_player_1_reaches_21_first(self):
        expected = "Player 1 wins!"
        actual = check_pingpong_winner((21, 19))
        self.assertEqual(expected, actual)


    def test_player_2_reaches_21_first(self):
        expected = "Player 2 wins!"
        actual = check_pingpong_winner((19, 21))
        self.assertEqual(expected, actual)    



print(check_pingpong_winner((19, 13)))
print(check_pingpong_winner((21, 13)))
print(check_pingpong_winner((19, 21)))
print(check_pingpong_winner((21, 20)))
print(check_pingpong_winner((25, 25)))
print(check_pingpong_winner((25, 27)))



if __name__ == "__main__":
    unittest.main()