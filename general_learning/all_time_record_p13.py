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
    def test_find_team_GT_has_highest_avg_differential_against(self):
        expected = "Vanderbilt"
        actual = find_team_GT_has_highest_avg_differential_against()
        self.assertEqual(expected, actual)

if __name__== "__main__":
    unittest.main()