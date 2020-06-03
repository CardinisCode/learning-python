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
                "Total Points GT Lost": 0
            }
        points_per_opposition[opponent]["Total Points GT Won"] += points_for
        points_per_opposition[opponent]["Total Points GT Lost"] += points_against

    return points_per_opposition


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


class TestAllTimeRecord(unittest.TestCase):
    # Correct outcome for #10 against their data-set is: Carnegie Tech
    def test_team_GT_played_but_never_scored_any_points_against(self):
        expected = "Luisiana"
        actual = find_team_GT_played_but_never_scored_any_points_against()
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()