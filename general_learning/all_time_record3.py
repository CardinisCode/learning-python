# Lets now answer this question: 
# How many points has Georgia Tech scored all-time against Auburn?

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
    for i in range(1, len(file_contents)):
        line = file_contents[i].rstrip()
        date, opposing_team, location, points_for, points_against = line.split(",")

        current_match = Match(opposing_team, date, location, points_for, points_against)
        record_board.append(current_match)

    return record_board

def calculate_all_time_points_GT_scored_against_opponent(opponent):
    all_time_points = 0

    record_board = store_the_file_contents()
    for match in record_board:
        opposing_team = match.opposition_team
        points_for = match.points_for

        if opposing_team == opponent:
            all_time_points += points_for

    return all_time_points

print(calculate_all_time_points_GT_scored_against_opponent("Auburn"))

