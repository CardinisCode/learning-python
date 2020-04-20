#Q6: What is Georgia Tech's all-time record in the month of October? 
# Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.

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
            'Points Won in October': 0,
            'Points Lost in October': 0,
            'Points Tied in October': 0,
            }

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        date = line_as_list[0]
        # print("Current date:", date)
        month = date[5:7]
        print("Current month:", month)
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])

        if points_for > points_against:
            georgia_tournament_played[opponent]['Games Won'] += 1
            georgia_tournament_played[opponent]['Total Points Won by GT'] += points_for
            if month == "10":
                georgia_tournament_played[opponent]['Points Won in October'] += points_for
        elif points_against == points_for:
            georgia_tournament_played[opponent]['Games Tied'] += 1
            if month == "10":
                georgia_tournament_played[opponent]['Points Tied in October'] += points_for
        else:
            georgia_tournament_played[opponent]['Games Lost'] += 1
            georgia_tournament_played[opponent]['Total Points Lost by GT'] += points_against
            if month == "10":
                georgia_tournament_played[opponent]['Points Lost in October'] += points_against
        if 'Games Played' in georgia_tournament_played[opponent].keys():
            georgia_tournament_played[opponent]['Games Played'] += 1
    
    return georgia_tournament_played

def calculate_all_time_scores_for_georgia_tech_at_home(georgia_score_table):
    total_games_won = 0
    total_games_lost = 0
    total_games_tied = 0
    for opponent in georgia_score_table.keys():
        total_games_won += georgia_score_table[opponent]['Points Won in October']
        total_games_lost += georgia_score_table[opponent]['Points Lost in October']
        total_games_tied += georgia_score_table[opponent]['Points Tied in October']

    return str(total_games_won) + "-" + str(total_games_lost) + "-" + str(total_games_tied)


def all_time_record(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    georgia_score_table = import_file_contents_into_dictionary(file_contents)
    season_points = calculate_all_time_scores_for_georgia_tech_at_home(georgia_score_table)

    return season_points

print(all_time_record("season2016.csv"))

#My answer for Q6:
# - For season2016.csv: 73-72-0
# - For their file:     8746-4348-67

