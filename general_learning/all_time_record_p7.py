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


# Q7: What is Georgia Tech's all-time record in the month of October? 
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


class TestAllTimeRecord(unittest.TestCase):
    def test_GTs_all_time_record_in_October(self):
        print("---------------------------------------")
        expected = "3-2-0"
        actual = calculate_GTs_alltime_record_in_specific_month("10")
        self.assertEqual(expected, actual)

    def test_GTs_all_time_record_in_November(self):
        print("---------------------------------------")
        expected = "3-1-0"
        actual = calculate_GTs_alltime_record_in_specific_month("11")
        self.assertEqual(expected, actual)
    


if __name__ == "__main__":
    unittest.main()

