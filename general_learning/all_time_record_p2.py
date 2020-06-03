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

class Match:
    def __init__(self, opposition, date, location, points_for, points_against):
        self.opposition_team = opposition
        self.date = date
        self.location = location
        self.points_for = points_for
        self.points_against = points_against

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


def find_earliest_date():
    earliest_date = None
    team_on_earliest_date = None 

    record_board = store_the_file_contents()
    for match in record_board:
        opposing_team = match.opposition_team
        date = match.get_date(match.date)
        print(date, type(date))

        if earliest_date == None or date < earliest_date: 
            earliest_date = date
            team_on_earliest_date = opposing_team
        else:
            continue

    return team_on_earliest_date

print(store_the_file_contents())
print()
print(find_earliest_date())
print()

# t = store_the_file_contents()
# print(t["Virginia"][0].get_date())
# print(t["Virginia"][0])

# happy = Match("2016-11-19", "Home", "16", "20")
# print(happy)
# print(str(happy))
# print(happy.__str__())




