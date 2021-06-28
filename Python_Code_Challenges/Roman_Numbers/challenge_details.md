Challenge: Roman Numbers (Hackajob)

Given a natural number n, translate and return it into a roman numeral string, knowing that:

M=1000; D=500; C=100; L=50; X=10; IX=9; 

VIII=8; VII=7; VI=6; V=5; IV=4; III=3; II=2; I=1; 
Numbers are formed by combining symbols and adding the values, so II is two (two ones) and XIII is thirteen (a ten and three ones). Because each numeral has a fixed value rather than representing multiples of ten, one hundred and so on, according to position, there is no need for "place keeping" zeros, as in numbers like 207 or 1066; those numbers are written as CCVII (two hundreds, a five and two ones) and MLXVI (a thousand, a fifty, a ten, a five and a one).

Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases, to avoid four characters being repeated in succession (such as IIII or XXXX), subtractive notation is used as in this table

Number: 4 9 40 90 400 900

Notation: IV IX XL XC CD CM

For example, MCMIV is one thousand nine hundred and four, 1904 (M is a thousand, CM is nine hundred and IV is four).

INPUT

int n
OUTPUT

string nRomanAlphabet
EXAMPLE 1

Input: 1954
Output: MCMLIV
EXAMPLE 2

Input: 1990
Output: MCMXC
EXAMPLE 3

Input: 2014
Output: MMXIV
CONSTRAINTS

1 <= n <= 10000