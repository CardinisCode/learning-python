import unittest
from datetime import datetime



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


class TestAllTimeRecord(unittest.TestCase):
    def test_points_clemson_scores_all_time_against_GT(self):
        expected = 26
        actual = calculate_all_time_points_opponent_scored_against_GT("Clemson")
        self.assertEqual(expected, actual)




if __name__ == "__main__":
    unittest.main()