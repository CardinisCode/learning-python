
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
import unittest

def extract_file_contents(filename): 
    imported_file = open(filename, "r")
    file_contents = imported_file.readlines()
    imported_file.close()
    return file_contents


from datetime import datetime

class Match:
    def __init__(self, opposition, date, location, points_for, points_against):
        self.opposition_team = opposition
        self.date = date
        self.location = location
        self.points_for = int(points_for)
        self.points_against = int(points_against)

    def __str__(self):
        return "%s: %s, %s,%s" % (self.date, self.location, self.points_for, self.points_against)
    
    def get_date(self, date_string):
        year, month, day = date_string.split("-")
        self.date = datetime(int(year), int(month), int(day))
        return self.date


def store_the_file_contents():
    record_board = []
    file_contents = extract_file_contents("season2016.csv")
    # input_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')

    for i in range(1, len(file_contents)):
        line = file_contents[i].rstrip()
        date, opposing_team, location, points_for, points_against = line.split(",")

        current_match = Match(opposing_team, date, location, points_for, points_against)
        record_board.append(current_match)

    return record_board

# Solving Task 1: the initial question "What is GT's all-time score against opponent X?"

def all_time_record(opposing_team):
    record_board = store_the_file_contents()

    wins_for_GT = 0
    losses_for_GT = 0
    ties_for_GT = 0

    for match in record_board:
        team = match.opposition_team
        points_for = match.points_for
        points_against = match.points_against

        if team == opposing_team:
            if points_for > points_against:
                wins_for_GT += 1
            elif points_for < points_against:
                losses_for_GT += 1
            else:
                ties_for_GT += 1  

    record = str(wins_for_GT) + "-" + str(losses_for_GT) + "-" + str(ties_for_GT)

    return record


# Lets answer Q2: Who was the first team Georgia Tech ever played against?

def find_earliest_date():
    earliest_date = None
    team_on_earliest_date = None 

    record_board = store_the_file_contents()
    for match in record_board:
        opposing_team = match.opposition_team
        date = match.get_date(match.date)

        if earliest_date == None or date < earliest_date: 
            earliest_date = date
            team_on_earliest_date = opposing_team
        else:
            continue

    return team_on_earliest_date


# Q3: How many points has Georgia Tech scored all-time against Auburn?

def calculate_all_time_points_GT_scored_against_opponent(opponent):
    all_time_points = 0

    record_board = store_the_file_contents()
    for match in record_board:
        opposing_team = match.opposition_team
        points_for = match.points_for

        if opposing_team == opponent:
            all_time_points += points_for

    return all_time_points


# Q4: How many points has Auburn scored all-time against Georgia Tech?
def calculate_all_time_points_opponent_scored_against_GT(opponent):
    all_time_points = 0

    record_board = store_the_file_contents()
    for match in record_board:
        opposing_team = match.opposition_team
        points_against = match.points_against

        if opposing_team == opponent:
            all_time_points += points_against

    return all_time_points

# Q5: What is Georgia Tech's all-time record in home games? 
#   Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.



class TestAllTimeRecord(unittest.TestCase):
    def test_all_time_record_GT_lose_to_clemson(self):
        print("---------------------------------------")
        expected = "0-1-0"
        actual = all_time_record("Clemson")
        self.assertEqual(expected, actual)

    def test_all_time_record_GT_win_to_Duke(self):
        print("---------------------------------------")
        expected = "1-0-0"
        actual = all_time_record("Duke")
        self.assertEqual(expected, actual)


    def test_all_time_record_GT_tie_with_Pensalvania(self):
        print("---------------------------------------")
        expected = "0-0-1"
        actual = all_time_record("Pensalvania")
        self.assertEqual(expected, actual)


    def test_points_clemson_scores_all_time_against_GT(self):
        expected = 26
        actual = calculate_all_time_points_opponent_scored_against_GT("Clemson")
        self.assertEqual(expected, actual)


    def test_points_clemson_scores_all_time_against_GT(self):
        expected = 13
        actual = calculate_all_time_points_opponent_scored_against_GT("Auburn")
        self.assertEqual(expected, actual)


if __name__== "__main__":
    unittest.main()


