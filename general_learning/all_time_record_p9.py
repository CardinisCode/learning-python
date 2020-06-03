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


def create_dictionary_of_victory_points_per_opposition():
    record_board = store_the_file_contents()
    victory_points_per_opposition = {}

    for match in record_board:
        opponent = match.opposition_team
        points_for = match.points_for
        
        if not opponent in victory_points_per_opposition.keys():
            victory_points_per_opposition[opponent] = {
                "Total Points GT Won": 0
            }
        victory_points_per_opposition[opponent]["Total Points GT Won"] += points_for

    return victory_points_per_opposition


# Q9: Against what team has Georgia Tech scored the most points?
def find_team_GT_has_scored_the_most_points_against():
    total_points_per_opposition = create_dictionary_of_victory_points_per_opposition()

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


class TestAllTimeRecord(unittest.TestCase):
    def test_team_GT_has_score_the_most_points_against(self):
        expected = "Duke"
        actual = find_team_GT_has_scored_the_most_points_against()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()