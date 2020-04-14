#Earlier in the course, you implemented a function that could
#find if someone had won a particular game of either tic-tac-
#toe or mancala based on a 2D list or tuple representing the
#current game board.
#
#In this problem, you'll do the same thing, but for the game
#Connect 4. Write a function called check_winner which takes
#as input a 2D list. It should return "X" if there are four
#adjacent "X" values anywhere in the list (row, column,
#diagonal); "O" if there are four adjacent "O" values
#anywhere in the list; and None if there are neither.
#
#Here are the ways Connect-4 is different from tic-tac-toe:
#
# - Connect-4 is played with 6 rows and 7 columns, not 3
#   rows and 3 columns.
# - You must have 4 in a row (or column or diagonal) to win
#   instead of 3.
# - You may only place pieces in the bottom-most empty
#   space in a column (e.g. you "drop" the pieces in the
#   column and they fall to the first empty spot). Note,
#   though, that this shouldn't affect your reasoning.
#
#To keep things simple, we'll still use "X" and "O" to
#represent the players, and None to represent empty spots.
#You may assume there will be only one winner per board,
#no characters besides "X", "O", and None, and you don't
#have to worry about whether the board is actually a
#valid game of Connect 4.
#
#Hints:
# - Don't forget both kinds of diagonals, top-left to
#   bottom-right and bottom-left to top-right.
# - This board is too large to check every possible place
#   for a winner: there are 69 places a player could win.
# - Remember, if you put a negative index in a list,
#   Python "wraps around" and checks the last value. You
#   may have to control for this.

import unittest
#Write your function here!
def check_winner(game_moves):

    for row in range(0, len(game_moves)):
        # print(game_moves[row])
        for column in range(0, len(game_moves[row])):
            print("Current slot:", game_moves[row][column])

            if game_moves[row][column] == None:
                print("Its a None, just ignore")
                continue

            elif column <= 3 and row <= 2:
                if game_moves[row][column] == game_moves[row][column + 1] == game_moves[row][column +2] == game_moves[row][column +3]:
                    print("Horizontal comparison")
                    return game_moves[row][column]

                elif game_moves[row][column] == game_moves[row+1][column] == game_moves[row +2][column] == game_moves[row + 3][column]:
                    print("Vertical comparison")
                    return game_moves[row][column]

                elif game_moves[row][column] == game_moves[row+1][column+1] == game_moves[row +2][column+2] == game_moves[row + 3][column +3]:
                    print("Diagonal comparison from top left to bottom right")
                    return game_moves[row][column]

            elif column >= 4 and row <= 2:
                print("Row is:", row, "and the column is", column)
                if game_moves[row][column] == game_moves[row +1][column -1] == game_moves[row +2][column -2] == game_moves[row +3][column -3]:
                    print("Diagonal comparison from top right to bottom left")
                    return game_moves[row][column]

                





#The code below tests your function on three Connect-4
#boards. Remember, the line breaks are not needed to create
#a 2D tuple; they're used here just for readability.





nowins =(("X" , "X" , None, None, None, None, None),
         ("O" , "O" , None, None, None, None, None),
         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
         ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
         ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))




print()     


# print(check_winner(xwins))
# if check_winner(xwinsdiagonal) == "X":
#     print("Correct outcome for xwins, congrats!")
# else: 
#     print("We're expecting X but you produced", check_winner(xwinsdiagonal))
# print()
# print(check_winner(owins))
# if check_winner(owins) == "O":
#     print("Correct outcome for Owins, congrats!")
# else:
#     print("We're expecting O but you produced", check_winner(owins))
# print()
# # print(check_winner(nowins))
# if check_winner(nowins) == None:
#     print("Correct outcome for Nowins, congrats!")
# else:
#     print("We're expecting None but you produced", check_winner(nowins))
# print()
# # print(check_winner(XwinsVertical))
# if check_winner(XwinsVertical) == "X": 
#     print("Correct outcome for xwinsVertical, congrats!")
# else:
#     print("We're expecting O but you produced", check_winner(XwinsVertical))
# print()
# if check_winner(owinsdiagonal) == "O":
#     print("Correct outcome for Owins, congrats!")
# else:
#     print("We're expecting O but you produced", check_winner(owinsdiagonal))


class TestConnect4(unittest.TestCase):
    def test_O_wins_horizontal(self):
        owins = ((None, None, None, None, None, None, None),
            (None, None, None, None, None, None, None),
            ("O" , "O" , "O" , "O" , None, None, None),
            ("O" , "X" , "X" , "X" , None, None, None),
            ("X" , "X" , "X" , "O" , "X" , None, None),
            ("X" , "O" , "O" , "X" , "O" , None, None))

        self.assertEqual("O", check_winner(owins))

    def test_O_wins_horizontal_at_the_end(self):
        owins = ((None, None, None, None, None, None, None),
            (None, None, None, None, None, None, None),
            (None, None, None, "O" , "O" , "O" , "O" ),
            ("O" , "X" , "X" , "X" , None, None, None),
            ("X" , "X" , "X" , "O" , "X" , None, None),
            ("X" , "O" , "O" , "X" , "O" , None, None))

        self.assertEqual("O", check_winner(owins))

    def test_X_wins_horizontal(self):
        xwins = ((None, None, None, None, None, None, None),
            (None, None, None, None, None, None, None),
            ("X" , "X" , "X" , "X" , None, None, None),
            ("X" , "O" , "O" , "O" , None, None, None),
            ("O" , "O" , "O" , "X" , "O" , None, None),
            ("O" , "X" , "X" , "O" , "X" , None, None))

        self.assertEqual("X", check_winner(xwins))

    def test_x_wins_horizontal_right(self):
        game_board = (
            ('X', 'X', None, None, None, None, None), 
            ('O', 'O', None, None, None, None, None), 
            ('O', 'X', 'O', 'O', None, 'O', 'O'), 
            ('O', 'X', 'X', 'X', 'X', 'X', 'X'), 
            ('X', 'X', 'X', 'O', 'X', 'X', 'O'), 
            ('X', 'O', 'O', 'X', 'O', 'X', 'O'))
    
        self.assertEqual("X", check_winner(game_board))

    def test_X_wins_diagonal(self):
        xwinsdiagonal = ((None, None, None, None, None, None, None),
            (None, None, None, None, None, None, None),
            (None, None, None, None, "X" , None, None),
            (None, None, None, "X" , "O" , "O", None),
            (None, "O" , "X" , "X" , "O" , "X", None),
            ("O" , "X" , "O" , "O" , "O" , "X" , "X"))

        self.assertEqual("X", check_winner(xwinsdiagonal))

    def test_O_diagonal(self):
        owinsdiagonal = ((None, "O", None, None, None, None, None), 
            (None, None, "O", None, "X", "X", None), 
            ("O", "X", None, "O", "X", None, "X"), 
            ("X", "O", None, None, "O", "X", None), 
            (None, None, None, "X" , "O" , "O", None), 
            ("O" , "X" , "O" , "O" , "O" , "X" , "X"))

        self.assertEqual("O", check_winner(owinsdiagonal))

    def test_X_wins_vertical(self):
        XwinsVertical =(
            ("O" , "X" , None, None, None, None, None),
            ("O" , "O" , None, None, None, None, None),
            ("X" , "X" , "O" , "O" , None, "O" , "O" ),
            ("X" , "X" , "X" , "X" , None, "X" , "X" ),
            ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
            ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))
        
        self.assertEqual("X", check_winner(XwinsVertical))

    def test_O_vertical(self):
        OwinsVertical =(
            ("X" , "O" , None, None, None, None, None),
            ("X" , "X" , None, None, None, None, None),
            ("O" , "O" , "X" , "X" , None, "X" , "X" ),
            ("O" , "O" , "O" , "O" , None, "O" , "O" ),
            ("O" , "O" , "O" , "X" , "O" , "O" , "X" ),
            ("O" , "X" , "X" , "O" , "X" , "O" , "X" ))
        
        self.assertEqual("O", check_winner(OwinsVertical))

    def test_for_no_wins(self):
        nowins =(
            ("X" , "X" , None, None, None, None, None),
            ("O" , "O" , None, None, None, None, None),
            ("O" , "X" , "O" , "O" , None, "O" , "O" ),
            ("O" , "X" , "X" , "X" , None, "X" , "X" ),
            ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
            ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))

        self.assertEqual(None,check_winner(nowins))

if __name__ == "__main__":
    unittest.main()