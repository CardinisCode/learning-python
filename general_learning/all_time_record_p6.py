# Q6: What was Georgia Tech's record in all games played in the 2009 calendar year? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.

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



class TestAllTimeRecord(unittest.TestCase):
    def test_GTs_record_all_games_played_in_year_2016(self):
        expected = "9-4-1"
        actual = calculate_GTs_record_of_all_games_played_in_specific_year("2016")
        self.assertEqual(expected, actual)

    def test_GTs_record_all_games_played_in_year_2015(self):
        expected = "1-0-0"
        actual = calculate_GTs_record_of_all_games_played_in_specific_year("2015")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()