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




import unittest
# import json

def creating_record_history(file_input, opposing_team):
    wins_for_GT = 0
    losses_for_GT = 0
    ties_for_GT = 0

    for i in range(1, len(file_input)):
        line = file_input[i]
        line = line.rstrip()
        line_split = line.split(",")
        team = line_split[1]
        points_for = int(line_split[3])
        points_against = int(line_split[4])

        #current_opponent = Opponents(team, location, points_for, points_against)
        
        if team == opposing_team:
            if points_for > points_against:
                wins_for_GT += 1
            elif points_for < points_against:
                losses_for_GT += 1
            else:
                ties_for_GT += 1  

    record = str(wins_for_GT) + "-" + str(losses_for_GT) + "-" + str(ties_for_GT)

    return record


def all_time_record(opposing_team):
    #input_file = open("season2016.csv", "r")
    input_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents = input_file.readlines()
    input_file.close()

    record_history = creating_record_history(file_contents, opposing_team)

    return record_history


    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
#line.
print("Clemson", all_time_record("Clemson"), "Vs the expected: 51-28-2")
print()
print("Duke", all_time_record("Duke"), "Vs the expected: 51-33-1")
print()
print("North Carolina", all_time_record("North Carolina"), "Vs the expected: 29-21-3")
print()
print("Pensalvania", all_time_record("Pensalvania"))