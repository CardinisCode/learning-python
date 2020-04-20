#Q12: Q12: Among teams that Georgia Tech has played at least 5 times, 
# against which team does Georgia Tech have the highest average score differential 
# (points for minus points against, divided by number of games)?

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
            'Total Points for': 0,
            'Total Points against': 0,
            'Differential':0,
            }

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])

        georgia_tournament_played[opponent]['Total Points for'] += points_for
        georgia_tournament_played[opponent]['Total Points against'] += points_against

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

#which team does Georgia Tech have the highest average score differential
def team_with_the_highest_average_score_differential(georgia_score_table):
    #highest average score differential = (points for minus points against, divided by number of games)
    highest_average_differential = 0
    team_with_highest_avg_differential = ""
    for opponent in georgia_score_table.keys():
        total_points_for_GT = georgia_score_table[opponent]['Total Points for']
        total_points_against_GT = georgia_score_table[opponent]['Total Points against']
        current_differential = total_points_for_GT - total_points_against_GT
        number_of_games = georgia_score_table[opponent]['Games Played']
        average_score_differential = current_differential / number_of_games
        if number_of_games >= 4 and average_score_differential > highest_average_differential:
            highest_average_differential = average_score_differential
            team_with_highest_avg_differential = opponent

        
    return (team_with_highest_avg_differential, highest_average_differential)

def all_time_record(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    georgia_score_table = import_file_contents_into_dictionary(file_contents)
    # season_points = calculate_which_team_Georgia_tech_has_scored_the_most_points_against(georgia_score_table)
    #highest_differential = calculate_the_highest_differential_amongst_opponents(georgia_score_table)
    highest_differential_team = team_with_the_highest_average_score_differential(georgia_score_table)

    return highest_differential_team

print(all_time_record("firstfiftylines.csv"))