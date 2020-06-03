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


# Q11: How many teams has played Georgia Tech and never scored a point?
def find_number_teams_to_play_GT_but_never_score_a_point():
    total_points_per_opposition = create_dictionary_of_points_for_and_against_per_opposition()
    number_of_teams = 0

    for opponent in total_points_per_opposition.keys():
        points_against = total_points_per_opposition[opponent]["Total Points GT Lost"]

        if points_against == 0:
            number_of_teams += 1

    return number_of_teams


class TestAllTimeRecord(unittest.TestCase):
    def test_find_number_teams_to_play_GT_but_never_score_a_point(self):
        expected = 2
        actual = find_number_teams_to_play_GT_but_never_score_a_point()
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()