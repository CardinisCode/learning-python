#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. 
When decrypting the message, 
#it's relatively easy to tell from context 
#whether a letter is
#meant to be an i or a j.
#
#To encrypt a message:

#-    1 ) first remove all non-letters

#-    2 ) convert the entire message to the same case.

#-    3 ) we break the message into pairs. 
# EG: imagine we wanted to encrypt the message 
# "PS. Hello, worlds". 
# First: we could convert it to PSHELLOWORLDS
# then: break it into letter pairs: 
# PS HE LL OW OR LD S. 
# 
#- If there is an odd number of characters: 
#-    we add X to the end.
#
#-    4 ) for each pair of letters: 
#-          we locate both letters in the cipher square. 
#
#There are four possible orientations for the pair of letters: 
#-      the "rectangle" case: they could be in different rows and column
#-      the "row" case: they could be in the same row but different                 columns   
#-      the "column" case: they could be in the same column but different           rows
#-      the "same" case: they could be the same letter.
        -   For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal.
#
# Looking at the message PS HE LL OW OR LD SX:
# 
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#What we do for each of the other three cases is different:
#
    For the Rectangle case:
        we replace each letter with the letter in the same row, but the other letter's column. 

#   Eg 1: we would replace HE with GR:
#       G is in the same row as H but the same column as E,
#   &   R is in the same row as E but the same column as H. 

#   Eg2: CS would become KL: 
#       K is in C's row but S's column, 
#   &   L is in C's column but S's row.
# - 

    For the Row case, 
        we pick the letter to the right of each letter, wrapping around the end of the row if we need to. 
#       PS becomes QL: 
#           Q is to the right of P
#       &   L is to the right of S if we wrap around the end of the
#           row.

    For the Column case, 
        we pick the letter below each letter, wrapping around if necessary. 
        LD becomes TY:
#       T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#

When decrypting: 
it would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.

#Decrypting a message is essentially the same process (as encrypting): 
    You would use the exact same cipher and process 

Except: 
#for the Row and Column cases: 
    you would shift left and up
    (instead of right and down)
#
#Write two methods: encrypt and decrypt. 

-   encrypt should:
        take as input a string 
    &   return an encrypted version of it (according to the rules above)
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - 
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
#   Add an X to the end if the length if odd.
# - Encrypt it.
#
-   decrypt should:
        take as input a string and
    &   return the unencrypted version, just undoing the last step. 
    
    You don't need to worry about:
    -   Js and Is, 
    -   duplicate letters 
    OR  odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"
#
#HINT: You might find it easier if you implement some
#helper functions, like a find_letter function that
#returns the row and column of a letter in the cipher.
#
#HINT 2: Once you've written encrypt, decrypt should
#be trivial: try to think of how you can modify encrypt
#to serve as decrypt.
#
#To make this easier, we've gone ahead and created the
#cipher as a 2D tuple for you:
CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))



#Add your code here!



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: QLGRQTVZIBTYQZ, then PSHELXOWORLDSX
print(encrypt("PS. Hello, world"))
print(decrypt("QLGRQTVZIBTYQZ"))
