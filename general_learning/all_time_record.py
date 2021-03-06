
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
from datetime import datetime

def extract_file_contents(filename): 
    imported_file = open(filename, "r")
    file_contents = imported_file.readlines()
    imported_file.close()
    return file_contents


class Match:
    def __init__(self, opposition, date, location, points_for, points_against):
        self.opposition_team = opposition
        self.date = date
        self.location = location
        self.points_for = int(points_for)
        self.points_against = int(points_against)

    def __str__(self):
        return "%s: %s, %s, %s,%s" % (opposition_team, self.date, self.location, self.points_for, self.points_against)
    
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


def create_dictionary_of_points_for_and_against_per_opposition():
    record_board = store_the_file_contents()
    points_per_opposition = {}

    for match in record_board:
        opponent = match.opposition_team
        points_for = match.points_for
        points_against = match.points_against
        
        if not opponent in points_per_opposition.keys():
            points_per_opposition[opponent] = {
                "Total Points GT Won": 0,
                "Total Points GT Lost": 0,
                "Number of Games Played": 0
            }
        points_per_opposition[opponent]["Total Points GT Won"] += points_for
        points_per_opposition[opponent]["Total Points GT Lost"] += points_against
        points_per_opposition[opponent]["Number of Games Played"] += 1

    return points_per_opposition


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
def calculating_GTs_all_time_record_in_home_games():
    record_board = store_the_file_contents()

    wins_for_GT = 0
    losses_for_GT = 0
    ties_for_GT = 0

    for match in record_board:
        location = match.location
        points_for = match.points_for
        points_against = match.points_against

        if location == "Home":
            if points_for > points_against:
                wins_for_GT += 1
            elif points_against > points_for:
                losses_for_GT += 1
            else:
                ties_for_GT += 1

    record = str(wins_for_GT) + "-" + str(losses_for_GT) + "-" + str(ties_for_GT)
    return record


# Q6: What was Georgia Tech's record in all games played in the 2009 calendar year? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
def calculate_GTs_record_of_all_games_played_in_specific_year(match_year):
    record_board = store_the_file_contents()

    wins_for_GT = 0
    losses_for_GT = 0
    ties_for_GT = 0

    for match in record_board:
        date = match.get_date(match.date)
        year = date.year
        points_for = match.points_for
        points_against = match.points_against

        if year == int(match_year):
            if points_for > points_against:
                wins_for_GT += 1
            elif points_against > points_for:
                losses_for_GT += 1
            else:
                ties_for_GT += 1

    record = str(wins_for_GT) + "-" + str(losses_for_GT) + "-" + str(ties_for_GT)
    return record


#Q7: What is Georgia Tech's all-time record in the month of October? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
def calculate_GTs_alltime_record_in_specific_month(match_month):
    record_board = store_the_file_contents()

    wins_for_GT = 0
    losses_for_GT = 0
    ties_for_GT = 0

    for match in record_board:
        date = match.get_date(match.date)
        month = date.month
        points_for = match.points_for
        points_against = match.points_against

        if month == int(match_month):
            if points_for > points_against:
                wins_for_GT += 1
            elif points_against > points_for:
                losses_for_GT += 1
            else:
                ties_for_GT += 1

    record = str(wins_for_GT) + "-" + str(losses_for_GT) + "-" + str(ties_for_GT)
    return record


# Q8: Georgia Tech played in the SEC from 1933 to 1963. What was its record during this time? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
def calculate_GTs_all_time_record_between_two_dates(start_date, end_date):
    record_board = store_the_file_contents()

    wins_for_GT = 0
    losses_for_GT = 0
    ties_for_GT = 0

    for match in record_board:
        date = match.get_date(match.date)
        year = date.year
        points_for = match.points_for
        points_against = match.points_against

        if year >= int(start_date) and year <= int(end_date):
            if points_for > points_against:
                wins_for_GT += 1
            elif points_against > points_for:
                losses_for_GT += 1
            else:
                ties_for_GT += 1

    record = str(wins_for_GT) + "-" + str(losses_for_GT) + "-" + str(ties_for_GT)
    return record


# Q9: Against what team has Georgia Tech scored the most points?
def find_team_GT_has_scored_the_most_points_against():
    total_points_per_opposition = create_dictionary_of_points_for_and_against_per_opposition()

    highest_points_for_GT = None
    team_in_question = None

    for team in total_points_per_opposition.keys():
        points_for = total_points_per_opposition[team]["Total Points GT Won"]

        if highest_points_for_GT == None or points_for > highest_points_for_GT:
            highest_points_for_GT = points_for
            team_in_question = team

    return team_in_question


# Q10: What is one of the two teams that Georgia Tech has played, and yet has never scored any points against? 
# Name either team.
def find_team_GT_played_but_never_scored_any_points_against():
    total_points_per_opposition = create_dictionary_of_points_for_and_against_per_opposition()
    teams_with_no_points_against_them = []

    for opponent in total_points_per_opposition:
        points_for = total_points_per_opposition[opponent]["Total Points GT Won"]

        if points_for == 0:
            teams_with_no_points_against_them.append(opponent)

    return teams_with_no_points_against_them[0]


# Q11: How many teams has played Georgia Tech and never scored a point?
def find_number_teams_to_play_GT_but_never_score_a_point():
    total_points_per_opposition = create_dictionary_of_points_for_and_against_per_opposition()
    number_of_teams = 0

    for opponent in total_points_per_opposition.keys():
        points_against = total_points_per_opposition[opponent]["Total Points GT Lost"]

        if points_against == 0:
            number_of_teams += 1

    return number_of_teams


# Q12: Against what team does Georgia Tech have the highest scoring differential (points for minus points against) all-time?
def find_team_GT_has_the_highest_scoring_differential_against():
    total_points_per_opposition = create_dictionary_of_points_for_and_against_per_opposition()

    highest_differential = None
    team_with_highest_differential = None

    for opponent in total_points_per_opposition.keys():
        points_for = total_points_per_opposition[opponent]["Total Points GT Won"]
        points_against = total_points_per_opposition[opponent]["Total Points GT Lost"]
        differential = abs(points_for - points_against)

        if differential < 0: 
            continue
        else:
            if highest_differential == None or differential > highest_differential:
                highest_differential = differential
                team_with_highest_differential = opponent

    return team_with_highest_differential

# Q13: Among teams that Georgia Tech has played at least 5 times, 
# against which team does Georgia Tech have the highest average score differential 
# (points for minus points against, divided by number of games)?

def find_team_GT_has_highest_avg_differential_against():
    scoring_per_opposition = create_dictionary_of_points_for_and_against_per_opposition()

    highest_avg_differential = None
    opponent_with_highest_avg_differential = None

    for opponent in scoring_per_opposition.keys():
        games_played = scoring_per_opposition[opponent]["Number of Games Played"]
        points_for = scoring_per_opposition[opponent]["Total Points GT Won"]
        points_against = scoring_per_opposition[opponent]["Total Points GT Lost"]
        differential = abs(points_for - points_against)
        avg_differential = differential / games_played

        if games_played >= 1 and (highest_avg_differential == None or avg_differential > highest_avg_differential):
            highest_avg_differential = avg_differential
            opponent_with_highest_avg_differential = opponent

        # Since the data extract season2016 never shows more than 1 match p/team, 
        # I've written my code for to make sure that every opponent included has played against GT at least once. 
        # In the code I submitted against their (full) dataset I adjusted my if statement accordingly:
        #    if games_played >= 5 and (highest_avg_differential == None or avg_differential > highest_avg_differential):
        # This did produce the expected outcome from their dataset: Furman

    return opponent_with_highest_avg_differential


class TestAllTimeRecord(unittest.TestCase):

    # Correct outcome for #1 (Clemson) against their data-set is: 51-28-2
    def test_all_time_record_GT_lose_to_clemson(self):
        print("---------------------------------------")
        expected = "0-1-0"
        actual = all_time_record("Clemson")
        self.assertEqual(expected, actual)

    # Correct outcome for #1 (Duke) against their data-set is: 51-33-1
    def test_all_time_record_GT_win_to_Duke(self):
        expected = "1-0-0"
        actual = all_time_record("Duke")
        self.assertEqual(expected, actual)


    def test_all_time_record_GT_tie_with_Pensalvania(self):
        expected = "0-0-1"
        actual = all_time_record("Pensalvania")
        self.assertEqual(expected, actual)

    
        # Correct outcome for #2 against their data-set is: Auburn
    def find_earliest_team_GT_ever_played_against(self):
        print("---------------------------------------")
        expected = "Jersey"
        actual = find_earliest_date()
        self.assertEqual(expected, actual)

    # Correct outcome for #3 against their data-set is:
    def test_calculate_all_time_points_GT_scored_against_opponent(self):
        expected = 18
        actual = calculate_all_time_points_GT_scored_against_opponent("Auburn")
        self.assertEqual(expected, actual)

    # Correct outcome for #4 against their data-set is: 1143
    def test_points_clemson_scores_all_time_against_GT(self):
        expected = 26
        actual = calculate_all_time_points_opponent_scored_against_GT("Clemson")
        self.assertEqual(expected, actual)


    def test_points_Auburn_scores_all_time_against_GT(self):
        expected = 13
        actual = calculate_all_time_points_opponent_scored_against_GT("Auburn")
        self.assertEqual(expected, actual)


     # Correct outcome for #5 against their data-set is: 513-226-27
    def test_GTs_all_time_record_in_home_games(self):
        expected = "6-2-1"
        actual = calculating_GTs_all_time_record_in_home_games()
        self.assertEqual(expected, actual)
       

    # Correct outcome for #6 against their data-set is: 11-3-0
    def test_GTs_record_all_games_played_in_year_2016(self):
        expected = "9-4-1"
        actual = calculate_GTs_record_of_all_games_played_in_specific_year("2016")
        self.assertEqual(expected, actual)


    def test_GTs_record_all_games_played_in_year_2015(self):
        expected = "1-0-0"
        actual = calculate_GTs_record_of_all_games_played_in_specific_year("2015")
        self.assertEqual(expected, actual)


    # Correct outcome for #7 against their data-set is: 302-177-10
    def test_GTs_all_time_record_in_October(self):
        expected = "3-3-0"
        actual = calculate_GTs_alltime_record_in_specific_month("10")
        self.assertEqual(expected, actual)


    def test_GTs_all_time_record_in_November(self):
        expected = "3-1-0"
        actual = calculate_GTs_alltime_record_in_specific_month("11")
        self.assertEqual(expected, actual)


    # Correct outcome for #8 against their data-set is: 206-110-12
    def test_GTs_all_time_record_between_2015_and_2016(self):
        expected = "10-4-1"
        actual = calculate_GTs_all_time_record_between_two_dates("2015", "2016")
        self.assertEqual(expected, actual)


    # Correct outcome for #9 against their data-set is: Duke
    def test_team_GT_has_score_the_most_points_against(self):
        expected = "Duke"
        actual = find_team_GT_has_scored_the_most_points_against()
        self.assertEqual(expected, actual)


    # Correct outcome for #10 against their data-set is: 'Carnegie Tech' OR 'St. Albans'
    def test_team_GT_played_but_never_scored_any_points_against(self):
        expected = "Luisiana"
        actual = find_team_GT_played_but_never_scored_any_points_against()
        self.assertEqual(expected, actual)

    # Correct outcome for #11 against their data-set is: 11
    def test_find_number_teams_to_play_GT_but_never_score_a_point(self):
        expected = 2
        actual = find_number_teams_to_play_GT_but_never_score_a_point()
        self.assertEqual(expected, actual)

    # Correct outcome for #12 against their data-set is: Tulane
    def test_find_team_GT_has_the_highest_scoring_differential_against(self):
        expected = "Vanderbilt"
        actual = find_team_GT_has_the_highest_scoring_differential_against()
        self.assertEqual(expected, actual)

    # Correct outcome for #13 against their data-set is: Furman
    def test_find_team_GT_has_highest_avg_differential_against(self):
        expected = "Vanderbilt"
        actual = find_team_GT_has_highest_avg_differential_against()
        self.assertEqual(expected, actual)

    

if __name__== "__main__":
    unittest.main()


