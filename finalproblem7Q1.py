#Last problem, you wrote a function that generated the all-
#time win-loss-tie record for Georgia Tech against any other
#team.
#
#That dataset had a lot of other information in it. Let's
#use it to answer some more questions. As a reminder, the
#data will be a CSV file, meaning that each line will be a
#comma-separated list of values. Each line will describe one
#game.
#
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent

#This line will open the file:
# record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.
#Q1:Who was the first team Georgia Tech ever played against?
#My code to answer the Q:
def import_file_contents_into_dictionary(filename):
    record_file = open(filename,"r")
    file_contents =record_file.readlines()
    record_file.close()

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        if index == 1:
            return opponent

print(import_file_contents_into_dictionary("season2016.csv"))
# print(import_file_contents_into_dictionary('../resource/lib/public/georgia_tech_football.csv'))
# The answer (using their file): Georgia
# 
# 
# 


