# Q4: What is Georgia Tech's all-time record in home games? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.
# My code:
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
        home_or_away = line_as_list[2]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])
        # print("Points for:", points_for, "and points against:", points_against)

        if points_for > points_against:
            georgia_tournament_played[opponent]['Games Won'] += 1
            georgia_tournament_played[opponent]['Total Points Won by GT'] += points_for
            if home_or_away == "Home":
                print("Points for GT at home:", points_for)
                georgia_tournament_played[opponent]['Home Points Won'] += points_for
        elif points_against == points_for:
            georgia_tournament_played[opponent]['Games Tied'] += 1
            if home_or_away == "Home":
                georgia_tournament_played[opponent]['Home Points Tied'] += points_for
        else:
            georgia_tournament_played[opponent]['Games Lost'] += 1
            georgia_tournament_played[opponent]['Total Points Lost by GT'] += points_against
            if home_or_away == "Home":
                georgia_tournament_played[opponent]['Home Points Lost'] += points_against
        if 'Games Played' in georgia_tournament_played[opponent].keys():
            georgia_tournament_played[opponent]['Games Played'] += 1
    
    return georgia_tournament_played

def calculate_all_time_scores_for_georgia_tech_at_home(georgia_score_table):
    total_games_won = 0
    total_games_lost = 0
    total_games_tied = 0
    for opponent in georgia_score_table.keys():
        total_games_won += georgia_score_table[opponent]['Home Points Won']
        total_games_lost += georgia_score_table[opponent]['Home Points Lost']
        total_games_tied += georgia_score_table[opponent]['Home Points Tied']

    return str(total_games_won) + "-" + str(total_games_lost) + "-" + str(total_games_tied)


def all_time_record(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    georgia_score_table = import_file_contents_into_dictionary(file_contents)
    season_points = calculate_all_time_scores_for_georgia_tech_at_home(georgia_score_table)

    # I used this to pull the total stats for each team, which allowed me to 
    # know what my expected stats would be using my copy of season2016.
    # # print(georgia_score_table)
    return season_points

print(all_time_record("season2016.csv"))
#A4: 15328-5318-217
