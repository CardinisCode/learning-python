# Lets answer Q2: Who was the first team Georgia Tech ever played against?
# we need the earliest data recorded in this file. 

#Firstly we need to extract the file contents. So I shall create a function 
# which opens the file once and returns these contents for easy access. 
def extract_file_contents(filename): 
    imported_file = open(filename, "r")
    file_contents = imported_file.readlines()
    imported_file.close()
    return file_contents


# current_filename = "season2016.csv"

# Now to store this data in such a way that it can be easily accessed not only to answer this question
# but for the 11 questions that follow. 
from datetime import datetime

def store_the_file_contents(Match):
    record_board = {}
    file_contents = extract_file_contents("season2016.csv")
    for i in range(1, len(file_contents)):
        line = file_contents[i].rstrip()
        # split_line = line.split(",")
        date, opposing_team, location, points_for, points_against = line.split(",")
        print("line contents:", date, opposing_team, location, points_for, points_against)
        print()
        if not opposing_team in record_board.keys():
            record_board[opposing_team] = []
        current_match = Match(date, location, points_for, points_against)
        record_board[opposing_team].append(current_match)

    return record_board



print(store_the_file_contents(Match))


class Match:
    def __init__(self, date, location, points_for, points_against):
        self.date = date
        self.location = location
        self.points_for = points_for
        self.points_against = points_against

