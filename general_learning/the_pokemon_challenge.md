For our last data analysis-inspired problem, let's go back to one of my favorite examples: Pokemon. Pokemon is a popular video game franchise by Nintendo which features over 800 monsters, called Pokemon, each with unique names, types, and statistics.

The dataset you'll have for this problem contains every Pokemon through Generation 7, including their alternate forms. You don't need to understand Pokemon to solve this problem, though: games are just good candidates for this kind of analysis because they often have well-formed, complete datasets.

To solve these problems, you just need to know a couple things. First, each row of the dataset corresponds to a Pokemon. Each row has 13 columns, in this order:

- Number: The numbered ID of the Pokemon, an integer
- Name: The name of the Pokemon, a string
- Type1: The Pokemon's primary type, a string
- Type2: The Pokemon's secondary type, a string (this may be blank; you may assume Type1 and Type2 will never be the same)
- HP: The Pokemon's HP statistic, an integer in the range 1 to 255
- Attack: The Pokemon's Attack statistic, an integer in the range 1 to 255
- Defense: The Pokemon's Defense statistic, an integer in the range 1 to 255
- SpecialAtk: The Pokemon's Special Attack statistic, an integer in the range 1 to 255
- SpecialDef: The Pokemon's Special Defense statistic, an integer in the range 1 to 255
- Speed: The Pokemon's Speed statistic, an integer in the range 1 to 255
- Generation: What generation the Pokemon debuted in, an integer in the range 1 to 7
- Legendary: Whether the Pokemon is considered "legendary" or not, either TRUE or FALSE (for you hardcore fans, we've grouped Legendary and Mythical Pokemon together for simplicity)
- Mega: Whether the Pokemon is "Mega" or not, either TRUE or FALSE

Use this information to answer the questions below. Note that although you can do this problem without objects, it will probably be much easier if you initially create a Pokemon object with the 13 attributes above, add a method for calculating a total power based on the sum of those six stats (HP, Attack, Defense, SpecialAtk, SpecialDef, and Speed), read the file into a list of instances of that object, and then do your reasoning based on that list.

#Q1: How many Pokemon have only one type? In other words, for how many Pokemon is Type2 blank?
#Q2: What is the most common type? Include both Type1 and Type2 in your count.
#Q3: What Pokemon has the highest HP statistic?
#Q4: Excluding Pokemon that are either Mega or Legendary, what Pokemon has the highest Defense statistic?
#Q5: Among Legendary Pokemon, what is the most common type? Include both Type1 and Type2 in your count.
#Q6: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.

#Q7: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), what is the strongest non-Legendary, non-Mega Pokemon? If there is a tie, list any of the tying Pokemon.

#Q8: What type has the highest average Speed statistic? Include both Type1 and Type2 in your calculation.

#Q9: Rounded to the nearest integer, what is that highest average Speed statistic? Include both Type1 and Type2 in your calculation

# Q10: Among all 7 Pokemon generations, which generation had the highest average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

# Q11: Rounded to the nearest integer, how much higher was that statistic than the next-closest generation's average sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed)?

# Q12: Rounded to the nearest integer, how much higher is the average sum of all six stats among Mega Pokemon than their non-Mega versions? Note that Mega Pokemon share the same Number (the first column) as their non-Mega versions, which will allow you to find all Pokemon that have a Mega version.


My findings and things I learnt personally: 
 - 1)  I do not have to edit the sample csv file to test for scenarios which aren't true to the data in its current form. 
    So if a question asks me a question regarding the legendary pokemon but there aren't any legendary pokemon in the sample csv, 
    then I can simply introduce 1/more sample legendary pokemon in the test scenario - which allows me to actually test my code against various scenarios without having to change the sample csv itself. 

Eg: In terms of the sum of all six stats (HP, Attack, Defense, Special Attack, Special Defense, and Speed), 
    what is the weakest Legendary Pokemon? If there is a tie, list any of the tying Pokemon.

In my sample code there is only 1 legendary pokemon but I need a few different legendary pokemon. 
So I can write my test like this: 

    def test_return_pokemon_with_weakest_stat_when_there_are_2_legendary_pokemon(self):
        pokedex = [
            Pokemon(1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,1,"TRUE","FALSE"),
            Pokemon(144,"Articuno","Ice","",90,85,100,95,125,85,1,"TRUE","FALSE")
            ]
        expected = "Bulbasaur"
        actual = find_weakest_legendary_pokemon(pokedex)

        self.assertEqual(expected, actual) 

Here I have brought in a "fake" legendary pokemon as it allows me to test my function against a data set with more than 1 legendary pokemon.  
So I can introduce "fake" (but likely) data into my tests if I am working with a sample subset of a file, as long as the fake data resembles data I'll likely find in the full version of the file. This allows me to full against all possible outcomes whilst still working with a small sample of the data. 

2) I can create a test class for each individual question

3) To avoid duplication, I can create an overall test class which can cover a question on the data subset itself.
Like to make sure the file / list (that runs through out the entire program) isnt empty.

