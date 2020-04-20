#Q8: Against what team has Georgia Tech scored the most points?

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
            }

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])

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

def calculate_which_team_Georgia_tech_has_scored_the_most_points_against(georgia_score_table):
    highest_score = 0
    opponent_with_most_losses = ""
    for opponent in georgia_score_table.keys():
        victory_points = georgia_score_table[opponent]['Total Points Won by GT']
        if victory_points > highest_score:
            highest_score = victory_points
            opponent_with_most_losses = opponent
    
    return (opponent_with_most_losses, highest_score)

def all_time_record(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    georgia_score_table = import_file_contents_into_dictionary(file_contents)
    season_points = calculate_which_team_Georgia_tech_has_scored_the_most_points_against(georgia_score_table)

    return season_points

print(all_time_record("season2016.csv"))

#My answer for Q5:
# - For season2016.csv: 'Mercer'
# - For their file:     'Duke'