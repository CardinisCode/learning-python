#The game HORSE is a popular basketball shooting game.
#It can be played with any number of players. One-by-one,
#each player takes a shot from anywhere they want. If they
#make the shot, the next person must make the same shot.
#If they do not, they receive a letter: H, then O, then R,
#then S, then E. Once a player receives all 5 letters, they
#are out of the game.
#
#The game continues until all but one player has all five
#letters.
#
#Write a function called check_horse_winner. This function
#will take as input a tuple of at least two, but potentially
#more, strings. 
#
#check_horse_winner should return the following:
#
# - If only one player is left with fewer than 5 letters,
#   return "Player X wins!", where X is the index of the
#   player in the list (which could be 0).
# - If more than one player has fewer than 5 letters,
#   return "Players X, Y: keep playing!", where X, Y, and
#   potentially more numbers are the indices of all players
#   who have not yet been eliminated.
# - If no player has 5 letters, return "Everyone: keep
#   playing!"

import unittest
#Write your function here!
def check_horse_winner(scoreboard):
    players_playing_on = []
    return_string = ""

    for index in range(0, len(scoreboard)):
        current_score = scoreboard[index]
        if len(current_score) != 5:
            players_playing_on.append(index)
    
    if len(players_playing_on) == len(scoreboard): 
        return_string = "Everyone: keep playing!"
    elif len(players_playing_on) == 1:
        return_string = "Player " + str(players_playing_on[0]) + " wins!"
    else:
        return_string = "Players "
        for index in range(0, len(players_playing_on)):
            current_player = players_playing_on[index]
            if index == len(players_playing_on) -1:
                return_string += str(current_player) + ": keep playing!"
            else:
                return_string += str(current_player) + ", "
    return return_string    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Everyone: keep playing!
#Players 1, 2: keep playing!
#Player 2 wins!
print(check_horse_winner(("HOR", "HORS", "H", "HO")))
print(check_horse_winner(("HORSE", "HOR", "HORS", "HORSE")))
print(check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE")))


class TestCheckHorseWinner(unittest.TestCase):
    def test_all_players_continue_playing(self):
        expected = "Everyone: keep playing!"
        actual = check_horse_winner(("HOR", "HORS", "H", "HO"))

        self.assertEqual(expected, actual)

    def test_only_one_player_wins(self):
        expected = "Player 2 wins!"
        actual = check_horse_winner(("HORSE", "HORSE", "HORS", "HORSE"))
        
        self.assertEqual(expected, actual)

    def test_multiple_winners(self):
        expected = "Players 1, 2: keep playing!"
        actual = check_horse_winner(("HORSE", "HOR", "HORS", "HORSE"))

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()