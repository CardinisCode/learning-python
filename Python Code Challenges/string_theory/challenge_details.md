Challenge: String Theory (Hackajob)

For a given sentence p, return the following:

-   how many vowels and consonants p has, we do not count Y and W as vowels
-   p with reversed words order and reversed cases (any upper-case letter will be lower-case and every lower-case letter will be upper-case)
-   every word in p separated by a dash ('-')
-   p with inserted string "pv" before any vowel in the sentence

Take into consideration that p can have any kind of characters.

You have to return a string containing the above queries, separated by double colon ("::")

INPUT
string p

OUTPUT
string combined_queries

This is how combined_queries should look like:

nr_vowels nr_consonants::reversed_p_with_reversed_cases::every-word-in-p::p_wpvith_inspvertpved_strpving_pv
EXAMPLE
Input
"ThIs is p"

Output
2 5::P IS tHiS::ThIs-is-p::ThpvIs pvis p