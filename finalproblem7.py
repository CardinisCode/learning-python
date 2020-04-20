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
            'Total Points Won by GT': 0,
            'Total Points Lost by GT': 0,
            'Home Points Won': 0,
            'Home Points Lost': 0,
            'Home Points Tied': 0,
            }

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])
        # print("Points for:", points_for, "and points against:", points_against)

        if points_for > points_against:
            georgia_tournament_played[opponent]['Games Won'] += 1
            georgia_tournament_played[opponent]['Total Points Won by GT'] += points_for
        elif points_against == points_for:
            georgia_tournament_played[opponent]['Games Tied'] += 1
        else:
            georgia_tournament_played[opponent]['Games Lost'] += 1
            georgia_tournament_played[opponent]['Total Points Lost by GT'] += points_against
        if 'Games Played' in georgia_tournament_played[opponent].keys():
            georgia_tournament_played[opponent]['Games Played'] += 1
    
    return georgia_tournament_played

def unpack_file_contents(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()
    return file_contents

#Q1: Who was the first team Georgia Tech ever played against?
def first_team_Georgia_played_against(file_contents):
    first_team = ""
    earliest_date = "0000-00-00"
    
    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        date = line_as_list[0]
        if index == 1:
            earliest_date = date
            first_team = line_as_list[1]

    first_year = earliest_date[0:4]
    first_month = earliest_date[5:7] 
    first_day = earliest_date[5:7]

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        date = line_as_list[0]
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        opponent = line_as_list[1]
        
        if year <= int(first_year) or month <= int(first_month) or day <= int(first_day):
            earliest_date = str(year) + "-" + str(month) + "-" + str(day)
            first_team = opponent
    return (earliest_date, first_team)

#Q2: How many points has Georgia Tech scored all-time against Auburn?
def points_scored_all_time_against_auburn(georgia_score_table):
    return "Calculating..."


file_contents = unpack_file_contents("firstthirtylines.csv")
georgia_score_table = import_file_contents_into_dictionary(file_contents)
first_team = first_team_Georgia_played_against(file_contents)
total_points_scored_against_auburn = points_scored_all_time_against_auburn(georgia_score_table)
print(first_team)


#
