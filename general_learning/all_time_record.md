#Let's try out a sort of data analysis-style problem. 
# 
# Re the file (to be imported) - a data set
# covering Georgia Tech's all-time football history:

#   It will be a CSV file: 
#       each line will be a comma-separated list of values

#   You can see a subsection of this dataset in season2016.csv
#   in the top left, but the actual dataset you'll be accessing
#   here will have 1237 games.

#  The first line of the file are headers:
#       Date,Opponent,Location,Points For,Points Against. 
#   After that, every line is a game.
# 

#. Each line (from line 2) will describe one game.
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
# Scoring: 
#If Points For is greater than Points Against, 
#   then Georgia Tech won the game. 
# If Points For is less than Points Against,
#   then Georgia Tech lost the game. 
# If the two are equal, 
# then the game was a tie.
#

# Task 1: 
#   Write a function called all_time_record. 
#       - all_time_record should take as input: a string representing an opposing team name. 
#       - It should return: a string representing the all-time record between Georgia Tech and that opponent, 
#         in the form Wins-Losses-Ties. 
#           EG: Georgia Tech has beaten Clemson 51 times, lost 28 times, and tied 2 times. 
#           So:  all_time_record("Clemson") would return the string "51-28-2".
#

# This dataset had a lot of other information in it. Let's
# use it to answer some more questions.

# I will document the code I use to answer each question as it will show how I changed/adjusted the code accordingly to answer the question. 
# On task 1, I didn't use any dictionary/lists/classes to store the info. 
# Yet when I saw how many questions that followed and the info I needed to extract to answer the questions, I knew I had to decide how I wanted to store the data for easier extraction - not just for the current question, but for all the questions overall. 
# After all the size of the program should reflect what's needed from the data itself - a big program just for the sake of it is a waste of resources.  

# Q2: Who was the first team Georgia Tech ever played against?
# Q3: How many points has Georgia Tech scored all-time against Auburn?
# Q4: How many points has Auburn scored all-time against Georgia Tech?
# Q5: What is Georgia Tech's all-time record in home games? 
#   Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
# Q6: What was Georgia Tech's record in all games played in the 2009 calendar year? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
# Q7: What is Georgia Tech's all-time record in the month of October? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
# Q8: Georgia Tech played in the SEC from 1933 to 1963. What was its record during this time? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
# Q9: Against what team has Georgia Tech scored the most points?
# Q10: What is one of the two teams that Georgia Tech has played, and yet has never scored any points against? 
# Name either team.
# Q11: How many teams has played Georgia Tech and never scored a point?
# Q12: Against what team does Georgia Tech have the highest scoring differential (points for minus points against) all-time?
# Q13: Among teams that Georgia Tech has played at least 5 times, 
# against which team does Georgia Tech have the highest average score differential (points for minus points against, divided by number of games)?




    
