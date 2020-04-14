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


#Write your function here!
def check_winner(game_moves):
    print()
    print("testing...")
    print()
    # x_moves_in_a_row = 0
    # o_moves_in_a_row = 0
    for row in game_moves:
        for slot in range(0, len(row)-2):
            print(row[slot], slot)
            if slot >= 4:
                continue
            elif row[slot] == "X":
                if row[slot +1] == "X" and row[slot +2] == "X" and row[slot +3] == "X":
                    return "X"
            elif row[slot] == "O":
                if row[slot +1] == "O" and row[slot +2] == "O" and row[slot +3] == "O":
                    return "O"



            # print("Player:", slot, "plays")
            # if slot == "X":
            #     x_moves_in_a_row += 1
            #     o_moves_in_a_row = 0
            #     if x_moves_in_a_row == 4:
            #         return "X"
            # elif slot == "O":
            #     o_moves_in_a_row += 1
            #     x_moves_in_a_row = 0
            #     if o_moves_in_a_row == 4:
            #         return "O"
            # else:
            #     x_moves_in_a_row = 0
            #     o_moves_in_a_row = 0
            #     continue 





#The code below tests your function on three Connect-4
#boards. Remember, the line breaks are not needed to create
#a 2D tuple; they're used here just for readability.
xwins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         (None, None, None, None, "X" , None, None),
         (None, None, None, "X" , "O" , "O", None),
         (None, "O" , "X" , "X" , "O" , "X", None),
         ("O" , "X" , "O" , "O" , "O" , "X" , "X"))
owins = ((None, None, None, None, None, None, None),
         (None, None, None, None, None, None, None),
         ("O" , "O" , "O" , "O" , None, None, None),
         ("O" , "X" , "X" , "X" , None, None, None),
         ("X" , "X" , "X" , "O" , "X" , None, None),
         ("X" , "O" , "O" , "X" , "O" , None, None))
nowins =(("X" , "X" , None, None, None, None, None),
         ("O" , "O" , None, None, None, None, None),
         ("O" , "X" , "O" , "O" , None, "O" , "O" ),
         ("O" , "X" , "X" , "X" , None, "X" , "X" ),
         ("X" , "X" , "X" , "O" , "X" , "X" , "O" ),
         ("X" , "O" , "O" , "X" , "O" , "X" , "O" ))
         
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))


