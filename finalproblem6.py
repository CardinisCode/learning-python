#Let's try out a sort of data analysis-style problem. In
#this problem, you're going to have access to a data set
#covering Georgia Tech's all-time football history. The data
#will be a CSV file, meaning that each line will be a comma-
#separated list of values. Each line will describe one game.
#The columns, from left-to-right, are:
#
# - Date: the date of the game, in Year-Month-Day format.
# - Opponent: the name of the opposing team
# - Location: Home, Away, or Neutral
# - Points For: Points scored by Georgia Tech
# - Points Against: Points scored by the opponent
#
#If Points For is greater than Points Against, then Georgia
#Tech won the game. If Points For is less than Points Against,
#then Georgia Tech lost the game. If the two are equal, then
#the game was a tie.
#
#You can see a subsection of this dataset in season2016.csv
#in the top left, but the actual dataset you'll be accessing
#here will have 1237 games.
#
#Write a function called all_time_record. all_time_record
#should take as input a string representing an opposing team
#name. It should return a string representing the all-time
#record between Georgia Tech and that opponent, in the form
#Wins-Losses-Ties. For example, Georgia Tech has beaten
#Clemson 51 times, lost 28 times, and tied 2 times. So,
#all_time_record("Clemson") would return the string "51-28-2".
#
#We have gone ahead and started the function and opened the
#file for you. The first line of the file are headers:
#Date,Opponent,Location,Points For,Points Against. After that,
#every line is a game.
import unittest

def import_file_contents_into_dictionary(file_contents):
    georgia_tournament_played = {}

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        if not opponent in georgia_tournament_played.keys():
            georgia_tournament_played[opponent] = {
            'Games Played': 0,
            'Games Won': 0, 
            'Games Lost': 0,
            'Games Tied': 0,
            }

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])
        # print("Points for:", points_for, "and points against:", points_against)

        if points_for > points_against:
            georgia_tournament_played[opponent]['Games Won'] += 1
        elif points_against == points_for:
            georgia_tournament_played[opponent]['Games Tied'] += 1
        else:
            georgia_tournament_played[opponent]['Games Lost'] += 1
        if 'Games Played' in georgia_tournament_played[opponent].keys():
            georgia_tournament_played[opponent]['Games Played'] += 1
    
    return georgia_tournament_played


def all_time_record(opponent):
    record_file = open("season2016.csv", "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    georgia_score_table = import_file_contents_into_dictionary(file_contents)

    # I used this to pull the total stats for each team, which allowed me to 
    # know what my expected stats would be using my copy of season2016.
    # # print(georgia_score_table)
    # print("North Carolina")
    # print("Games played:", georgia_score_table["North Carolina"]["Games Played"])
    # print("Games Won:", georgia_score_table["North Carolina"]["Games Won"])
    # print("Games Lost", georgia_score_table["North Carolina"]["Games Lost"])
    # print("Games Tied", georgia_score_table["North Carolina"]["Games Tied"])

    georgia_record = ""

    for opponents in georgia_score_table.keys():
        if opponent == opponents:
            georgia_record += str(georgia_score_table[opponent]['Games Won']) + "-"
            georgia_record += str(georgia_score_table[opponent]['Games Lost']) + "-"
            georgia_record += str(georgia_score_table[opponent]['Games Tied'])
            return georgia_record

    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
 # (Note this would be the expected stats for these teams using their file
 # Which can only be run inside their test environment - 
 # This doesn't help me until I submit my code inside their environment.)

#print: 51-28-2, 51-33-1, and 29-21-3, each on a separate
#line.

class AllTimeRecord(unittest.TestCase):
    def test_georgia_tech_plays_clemson(self):
        actual = all_time_record("Clemson")
        self.assertEqual("31-41-5", actual) 

    def georgia_tech_plays_duke(self):
        actual = all_time_record("Duke")
        self.assertEqual("8-12-3", actual) 

    def georgia_tech_plays_north_carolina(self):
        actual = all_time_record("North Carolina")
        self.assertEqual("5-7-3", actual)

    def test_georgia_tech_plays_kentucky(self):
        print("georgia_tech_plays_kentucky")
        actual = all_time_record("Kentucky")
        self.assertEqual("3-1-1", actual) 

    def test_georgia_tech_plays_mercer(self):
        print("georgia_tech_plays_mercer")
        actual = all_time_record("Mercer")
        self.assertEqual("2-2-1", actual) 

    def test_georgia_tech_plays_georgia(self):
        print("Geogia Tech play Georgia")
        actual = all_time_record("Georgia") 
        self.assertEqual("45-2-3",actual)

print("Clemson:", all_time_record("Clemson"))
print("Duke:", all_time_record("Duke"))
print("North Carolina:", all_time_record("North Carolina"))
# print(all_time_record("Kentucky"))
# print(all_time_record("Mercer"))
# print("Georgia:", all_time_record("Georgia"))

if __name__ == "__main__":
    unittest.main()

# To get their data, i submitted my code with an imbedded request to print the dictionary
# So it pulled all the data from their file and imported it all into a dictionary. 
# It looks like this:
# {'Georgia': {'Games Played': 107, 'Games Won': 44, 'Games Lost': 63, 'Games Tied': 0},
#  'Duke': {'Games Played': 85, 'Games Won': 42, 'Games Lost': 43, 'Games Tied': 0}, 
#  'Virginia Tech': {'Games Played': 15, 'Games Won': 8, 'Games Lost': 7, 'Games Tied': 0}, 
#  'Virginia': {'Games Played': 40, 'Games Won': 18, 'Games Lost': 22, 'Games Tied': 0}, 
#  'Clemson': {'Games Played': 81, 'Games Won': 39, 'Games Lost': 42, 'Games Tied': 0}, 
#  'Wake Forest': {'Games Played': 31, 'Games Won': 19, 'Games Lost': 12, 'Games Tied': 0}, 
#  'Miami-FL': {'Games Played': 23, 'Games Won': 13, 'Games Lost': 10, 'Games Tied': 0}, 
#  'North Carolina': {'Games Played': 53, 'Games Won': 25, 'Games Lost': 28, 'Games Tied': 0}, 
#  'Pittsburgh': {'Games Played': 12, 'Games Won': 7, 'Games Lost': 5, 'Games Tied': 0}, 
#  'Jacksonville State': {'Games Played': 3, 'Games Won': 3, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Tennessee': {'Games Played': 44, 'Games Won': 23, 'Games Lost': 21, 'Games Tied': 0}, 
#  'Kentucky': {'Games Played': 20, 'Games Won': 12, 'Games Lost': 8, 'Games Tied': 0}, 
#  'Georgia Southern': {'Games Played': 2, 'Games Won': 2, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Vanderbilt': {'Games Played': 37, 'Games Won': 21, 'Games Lost': 16, 'Games Tied': 0}, 
#  'Mercer': {'Games Played': 12, 'Games Won': 10, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Boston College': {'Games Played': 9, 'Games Won': 7, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Florida State': {'Games Played': 27, 'Games Won': 10, 'Games Lost': 17, 'Games Tied': 0}, 
#  'Notre Dame': {'Games Played': 35, 'Games Won': 15, 'Games Lost': 20, 'Games Tied': 0}, 
#  'Tulane': {'Games Played': 50, 'Games Won': 29, 'Games Lost': 21, 'Games Tied': 0}, 
#  'Alcorn State': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Mississippi State': {'Games Played': 5, 'Games Won': 4, 'Games Lost': 1, 'Games Tied': 0}, 
#  'North Carolina State': {'Games Played': 29, 'Games Won': 20, 'Games Lost': 9, 'Games Tied': 0}, 
#  'Wofford': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Mississippi': {'Games Played': 4, 'Games Won': 0, 'Games Lost': 4, 'Games Tied': 0}, 
#  'Alabama A&M': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Syracuse': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Brigham Young': {'Games Played': 4, 'Games Won': 1, 'Games Lost': 3, 'Games Tied': 0}, 
#  'Elon': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Southern California': {'Games Played': 4, 'Games Won': 1, 'Games Lost': 3, 'Games Tied': 0}, 
#  'Maryland': {'Games Played': 21, 'Games Won': 15, 'Games Lost': 6, 'Games Tied': 0}, 
#  'Middle Tennessee State': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Presbyterian': {'Games Played': 4, 'Games Won': 4, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Utah': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Kansas': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Western Carolina': {'Games Played': 5, 'Games Won': 4, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Air Force': {'Games Played': 4, 'Games Won': 4, 'Games Lost': 0, 'Games Tied': 0}, 
#  'South Carolina State': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Iowa': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Louisiana State': {'Games Played': 19, 'Games Won': 6, 'Games Lost': 13, 'Games Tied': 0}, 
#  'Gardner-Webb': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Fresno State': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Army': {'Games Played': 4, 'Games Won': 2, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Samford': {'Games Played': 8, 'Games Won': 6, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Troy': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'West Virginia': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Connecticut': {'Games Played': 3, 'Games Won': 3, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Auburn': {'Games Played': 86, 'Games Won': 37, 'Games Lost': 49, 'Games Tied': 0}, 
#  'Tulsa': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Stanford': {'Games Played': 2, 'Games Won': 2, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Navy': {'Games Played': 25, 'Games Won': 16, 'Games Lost': 9, 'Games Tied': 0}, 
#  'Citadel': {'Games Played': 10, 'Games Won': 7, 'Games Lost': 3, 'Games Tied': 0}, 
#  'Central Florida': {'Games Played': 3, 'Games Won': 3, 'Games Lost': 0, 'Games Tied': 0}, 
#  'New Mexico State': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Arizona': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Furman': {'Games Played': 12, 'Games Won': 7, 'Games Lost': 5, 'Games Tied': 0}, 
#  'Baylor': {'Games Played': 4, 'Games Won': 3, 'Games Lost': 1, 'Games Tied': 0}, 
#  'South Carolina': {'Games Played': 20, 'Games Won': 9, 'Games Lost': 11, 'Games Tied': 0}, 
#  'Penn State': {'Games Played': 7, 'Games Won': 3, 'Games Lost': 4, 'Games Tied': 0}, 
#  'Tennessee-Chattanooga': {'Games Played': 8, 'Games Won': 6, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Nebraska': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Virginia Military Institute': {'Games Played': 15, 'Games Won': 7, 'Games Lost': 8, 'Games Tied': 0}, 
#  'Indiana State': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Michigan State': {'Games Played': 3, 'Games Won': 3, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Alabama': {'Games Played': 52, 'Games Won': 24, 'Games Lost': 28, 'Games Tied': 0}, 
#  'Memphis': {'Games Played': 3, 'Games Won': 1, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Florida': {'Games Played': 39, 'Games Won': 18, 'Games Lost': 21, 'Games Tied': 0}, 
#  'William & Mary': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Purdue': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'California': {'Games Played': 7, 'Games Won': 4, 'Games Lost': 3, 'Games Tied': 0}, 
#  'Iowa State': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Rice': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Texas Tech': {'Games Played': 2, 'Games Won': 1, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Southern Methodist': {'Games Played': 11, 'Games Won': 4, 'Games Lost': 7, 'Games Tied': 0}, 
#  'Texas Christian': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Texas A&M': {'Games Played': 2, 'Games Won': 1, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Missouri': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Arkansas': {'Games Played': 2, 'Games Won': 1, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Davidson': {'Games Played': 13, 'Games Won': 10, 'Games Lost': 3, 'Games Tied': 0}, 
#  'Washington & Lee': {'Games Played': 6, 'Games Won': 3, 'Games Lost': 3, 'Games Tied': 0}, 
#  "St. Mary's": {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Georgia Pre-Flight': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Fort Benning': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Texas': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Sewanee': {'Games Played': 11, 'Games Won': 5, 'Games Lost': 6, 'Games Tied': 0}, 
#  'Michigan': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Pennsylvania': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Carnegie Tech': {'Games Played': 2, 'Games Won': 0, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Oglethorpe': {'Games Played': 9, 'Games Won': 4, 'Games Lost': 5, 'Games Tied': 0}, 
#  'Georgetown': {'Games Played': 5, 'Games Won': 2, 'Games Lost': 3, 'Games Tied': 0}, 
#  'Rutgers': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Centre': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Camp Logan': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Camp Gordon': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  '11th Cavalry': {'Games Played': 3, 'Games Won': 1, 'Games Lost': 2, 'Games Tied': 0}, 
#  'Carlisle': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Cumberland': {'Games Played': 3, 'Games Won': 3, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Transylvania': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Camp McPherson': {'Games Played': 2, 'Games Won': 1, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Gordon': {'Games Played': 4, 'Games Won': 3, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Mooney': {'Games Played': 3, 'Games Won': 2, 'Games Lost': 1, 'Games Tied': 0}, 
#  'North Georgia': {'Games Played': 3, 'Games Won': 3, 'Games Lost': 0, 'Games Tied': 0}, 
#  'Maryville': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}, 
#  'Tennessee Medical': {'Games Played': 1, 'Games Won': 1, 'Games Lost': 0, 'Games Tied': 0}, 
# 'St. Albans': {'Games Played': 1, 'Games Won': 0, 'Games Lost': 1, 'Games Tied': 0}}
