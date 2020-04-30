For our last data analysis-inspired problem, let's go back to one of my favorite examples: Pokemon. Pokemon is a popular video game franchise by Nintendo which features over 800 monsters, called Pokemon, each with unique names, types, and statistics.

The dataset you'll have for this problem contains every Pokemon through Generation 7, including their alternate forms. You don't need to understand Pokemon to solve this problem, though: games are just good candidates for this kind of analysis because they often have well-formed, complete datasets.

To solve these problems, you just need to know a couple things: 
-   First, each row of the dataset corresponds to a Pokemon. 
    -   Each row has 13 columns, in this order:

Number: The numbered ID of the Pokemon, an integer
Name: The name of the Pokemon, a string
Type1: The Pokemon's primary type, a string
Type2: The Pokemon's secondary type, a string (this may be blank; you may assume Type1 and Type2 will never be the same)
HP: The Pokemon's HP statistic, an integer in the range 1 to 255
Attack: The Pokemon's Attack statistic, an integer in the range 1 to 255
Defense: The Pokemon's Defense statistic, an integer in the range 1 to 255
SpecialAtk: The Pokemon's Special Attack statistic, an integer in the range 1 to 255
SpecialDef: The Pokemon's Special Defense statistic, an integer in the range 1 to 255
Speed: The Pokemon's Speed statistic, an integer in the range 1 to 255
Generation: What generation the Pokemon debuted in, an integer in the range 1 to 7
Legendary: Whether the Pokemon is considered "legendary" or not, either TRUE or FALSE (for you hardcore fans, we've grouped Legendary and Mythical Pokemon together for simplicity)
Mega: Whether the Pokemon is "Mega" or not, either TRUE or FALSE

Use this information to answer the questions below. Note that although you can do this problem without objects, it will probably be much easier if you initially:
-    create a Pokemon object with the 13 attributes above, 
-   add a method for calculating a total power based on the sum of those six stats (HP, Attack, Defense, SpecialAtk, SpecialDef, and Speed), 
-   read the file into a list of instances of that object, 
-   and then do your reasoning based on that list.



Q1: How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
A1: Using sample subset: 10
A1: Using their file: 420

Q2: What is the most common type? Include both Type1 and Type2 in your count.
A1: Using sample subset: Poison
A1: Using their file: Water


Q3: What Pokemon has the highest HP statistic?
A3: Using sample subset: Mega Pidgeot
A3: Using their file: Blissey


Q4: Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?
A4: Using sample subset: Blastoise
A4: Using their file: Shuckle


Q5: Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.
A5: Using sample subset: Bug
A5: Using their file: Psychic


Q6: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.
A6: Using sample subset: Legendary Caterpie
A6: Using their file: Cosmog


Q7: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the strongest non-Legendary, non-Mega Pokemon? If there is a tie, list any of the tying Pokemon.
A7: Using sample subset: Charizard
A7: Using their file: Slaking


Q8: What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.
A8: Using sample subset: Dragon
A8: Using their file: Flying


Q9: Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation.
A9: Using sample subset: 100
A9: Using their file: 85


Q10: Among all 7 Pokemon generations, which generation had the highest average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?
A10: Using sample subset: 4
A10: Using their file: 7


Q11: Rounded to the nearest integer, how much higher was that statistic than the next-closest generation's average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?
A11: Using sample subset: 197
A11: Using their file: 2



Q12: Rounded to the nearest integer, how much higher is the average sum of all six stats among Mega Pokemon than their non-Mega versions? Note that Mega Pokemon share the same Number (the first column) as their non-Mega versions, which will allow you to find all Pokemon that have a Mega version.
A12: Using sample subset: 107
A12: Using their file: 100