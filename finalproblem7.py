def import_file_contents_into_dictionary(file_contents):
    georgia_tournament_played = {}
    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        home_or_away = line_as_list[2]
        if not opponent in georgia_tournament_played.keys():
            georgia_tournament_played[opponent] = {
            'Games Played': 0,
            'Games Won': 0, 
            'Games Lost': 0,
            'Games Tied': 0,
            'Total Points Won by GT': 0,
            'Total Points Lost by GT': 0,
            'Total Points Tied by GT':0,
            'Home Games Played': 0,
            'Home Games Won': 0,
            'Home Games Lost': 0,
            'Home Games Tied': 0,
            'Differential':0,
            }

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        opponent = line_as_list[1]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])

        # If GT scored more points in the match against their opponent:
        if points_for > points_against:
            georgia_tournament_played[opponent]['Games Won'] += 1
            if home_or_away == "Home":
                georgia_tournament_played[opponent]['Home Games Played'] += 1
                georgia_tournament_played[opponent]['Home Games Won'] += 1

        # If GT and the opponent scored equal points in the match:
        elif points_against == points_for:
            georgia_tournament_played[opponent]['Games Tied'] += 1
            georgia_tournament_played[opponent]['Total Points Tied by GT'] += points_for
            if home_or_away == "Home":
                georgia_tournament_played[opponent]['Home Games Played'] += 1
                georgia_tournament_played[opponent]['Home Games Tied'] += points_for

        # If the opponent scored more points than GT in the match:
        else:
            georgia_tournament_played[opponent]['Games Lost'] += 1
            if home_or_away == "Home":
                georgia_tournament_played[opponent]['Home Games Played'] += 1
                georgia_tournament_played[opponent]['Home Games Lost'] += 1

        georgia_tournament_played[opponent]['Games Played'] += 1
        georgia_tournament_played[opponent]['Total Points Won by GT'] += points_for
        georgia_tournament_played[opponent]['Total Points Lost by GT'] += points_against

    return georgia_tournament_played

def unpack_file_contents(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    return file_contents

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
    return first_team


def points_scored_all_time_against_auburn(georgia_score_table):

    return georgia_score_table["Auburn"]['Total Points Won by GT']


def overall_points_scored_by_auburn_against_GT(georgia_score_table):
    return georgia_score_table["Auburn"]['Total Points Lost by GT']

def georgia_techs_all_time_record_in_home_games(file_contents):
    total_home_games = 0
    games_won = 0
    games_lost = 0
    games_tied = 0
    for index in range(1, len(file_contents)):
        current_line = file_contents[index].rstrip()
        line_as_list = current_line.split(",")
        home_or_away = line_as_list[2]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])

        if home_or_away == "Home":
            total_home_games += 1
            if points_for > points_against:
                games_won += 1
            elif points_for == points_against:
                games_tied += 1
            else:
                games_lost += 1

    all_time_record_for_home = str(games_won) + "-" + str(games_lost) + "-" + str(games_tied)
    return all_time_record_for_home

def georgia_techs_all_time_record_2009(file_contents):
    total_home_games = 0
    games_won = 0
    games_lost = 0
    games_tied = 0

    for index in range(1, len(file_contents)):
        current_line = file_contents[index].rstrip()
        line_as_list = current_line.split(",")
        date = line_as_list[0]
        year = date[0:4]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])        

        if year == "2009":
            total_home_games += 1
            if points_for > points_against:
                games_won += 1
            elif points_for == points_against:
                games_tied += 1
            else:
                games_lost += 1

    overall_time_record_for_2009 = str(games_won) + "-" + str(games_lost) + "-" + str(games_tied)
    if (games_won + games_lost + games_tied) == total_home_games:
        return overall_time_record_for_2009
    return "Keep trying..."

def georgia_techs_all_time_score_for_games_in_october(file_contents, georgia_score_table):
    total_october_games = 0
    games_won = 0
    games_lost = 0
    games_tied = 0

    for index in range(1, len(file_contents)):
        current_line = file_contents[index].rstrip()
        line_as_list = current_line.split(",")
        date = line_as_list[0]
        month = date[5:7]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])        

        if month == "10":
            total_october_games += 1
            if points_for > points_against:
                games_won += 1
            elif points_for == points_against:
                games_tied += 1
            else: 
                games_lost += 1

    overall_time_record_for_october = str(games_won) + "-" + str(games_lost) + "-" + str(games_tied)
    if (games_won + games_lost + games_tied) == total_october_games:
        return overall_time_record_for_october
    return "Keep trying..."

def georgia_techs_record_from_1933_to_1963(file_contents, georgia_score_table):
    total_games = 0
    games_won = 0
    games_lost = 0
    games_tied = 0

    for index in range(1, len(file_contents)):
        current_line = file_contents[index].rstrip()
        line_as_list = current_line.split(",")
        date = line_as_list[0]
        year = date[0:4]
        points_for = int(line_as_list[3])
        points_against = int(line_as_list[4])        

        if year >= "1933" and year <= "1963":
            total_games += 1
            if points_for > points_against:
                games_won += 1
            elif points_for == points_against:
                games_tied += 1
            else:
                games_lost += 1

    overall_time_record = str(games_won) + "-" + str(games_lost) + "-" + str(games_tied)
    if (games_won + games_lost + games_tied) == total_games:
        return overall_time_record
    return "Keep trying..."

def against_which_team_georgia_tech_scored_the_most_points(georgia_score_table):
    opponent_with_most_losses_against_GT = ""
    highest_points = 0

    for opponent in georgia_score_table.keys():
        points_won_by_GT = georgia_score_table[opponent]['Total Points Won by GT']
        if points_won_by_GT >= highest_points:
            highest_points = points_won_by_GT
            opponent_with_most_losses_against_GT = opponent

    return opponent_with_most_losses_against_GT

def find_teams_georgia_tech_has_never_won_points_against(georgia_score_table):
    for opponent in georgia_score_table.keys():
        points_won_by_GT = georgia_score_table[opponent]['Total Points Won by GT']
        if points_won_by_GT == 0:
            return opponent

def number_of_teams_have_never_scored_a_point_against_GT(georgia_score_table):
    number_of_teams = 0
    for opponent in georgia_score_table.keys():
        points_lost_by_GT = georgia_score_table[opponent]['Total Points Lost by GT']
        if points_lost_by_GT == 0:
            number_of_teams += 1
    return number_of_teams

def find_team_GT_has_the_alltime_highest_scoring_differential_against(georgia_score_table):
    highest_differential = 0
    team_with_highest_differential = ""
    for opponent in georgia_score_table.keys():
        total_points_for_GT = georgia_score_table[opponent]['Total Points Won by GT']
        total_points_against_GT = georgia_score_table[opponent]['Total Points Lost by GT']
        current_differential = total_points_for_GT - total_points_against_GT
        georgia_score_table[opponent]['Differential'] = current_differential
        if current_differential > highest_differential:
            highest_differential = current_differential
            team_with_highest_differential = opponent

    return team_with_highest_differential

def find_team_GT_has_the_highest_avg_score_differential_against(georgia_score_table):
    highest_average_differential = 0
    team_with_highest_avg_differential = ""
    for opponent in georgia_score_table.keys():
        current_differential = georgia_score_table[opponent]['Differential']
        number_of_games = georgia_score_table[opponent]['Games Played']
        average_score_differential = current_differential / number_of_games
        if number_of_games >= 5 and average_score_differential > highest_average_differential:
            highest_average_differential = average_score_differential
            team_with_highest_avg_differential = opponent
    return team_with_highest_avg_differential



file_contents = unpack_file_contents("completefile.csv")
georgia_score_table = import_file_contents_into_dictionary(file_contents)

print()
first_team = first_team_Georgia_played_against(file_contents)
print("Question #1: Who was the first team Georgia Tech ever played against?")
print()
print("Answer #1:", first_team)
print("Expected Answer: Auburn")
expected_answer = "Auburn"
if first_team == expected_answer:
    print("Correct Answer!")

# My Answers for #1: 
# # 1: Georgia - Wrong!
# # 2: 'Auburn' - Correct!

print()
print()
total_points_scored_against_auburn = points_scored_all_time_against_auburn(georgia_score_table)
print("Question #2: How many points has Georgia Tech scored all-time against Auburn?")
print()
print("Answer #2:", total_points_scored_against_auburn)
print("Expected Answer: 1327")

# #My Answers for #2:
# Attempt #1: 950 - Wrong
# Attempt #2: 1327 - Correct!

print()
print()
overall_points_lost_in_games_played_against_auburn = overall_points_scored_by_auburn_against_GT(georgia_score_table)
print("Question #Q3: How many points has Auburn scored all-time against Georgia Tech?")
print("Answer #3:", overall_points_lost_in_games_played_against_auburn)
print("Expected Answer: 1143")

#My Answer for #3: 
# Attempt #1: 880 - Wrong!
# Attempt #2: 1143 - Correct!

print()
total_points_for_georgia_Tech_at_home = georgia_techs_all_time_record_in_home_games(file_contents)
print("Question #4: What is Georgia Tech's all-time record in home games? Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.")
print()
print("Answer #4:", total_points_for_georgia_Tech_at_home)
print("Expected Answer: 513-226-27")

#My attempts for #4:
#1: 15328-5318-217 - Wrong!
#2: 21077-11874-289 - Wrong!
#3: 722-475-289 - Wrong!
#4: 513-226-27 - Correct!

print()
print()
georgia_techs_all_time_scores_for_2009 = georgia_techs_all_time_record_2009(file_contents)
print("Question #5: What was Georgia Tech's record in all games played in the 2009 calendar year? Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.")
print()
print("Answer #5:", georgia_techs_all_time_scores_for_2009)
print("Expected Answer: 11-3-0")

# My attempts for #5:
#1: 418-87-0 - Wrong
#2: 12312-10871-172 - Wrong!
#3: 11-3-0 - Correct!

print()
print()
georgia_techs_all_time_scores_for_october = georgia_techs_all_time_score_for_games_in_october(file_contents, georgia_score_table)
print("Question #6: What is Georgia Tech's all-time record in the month of October? Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.")
print()
print("Answer #6:", georgia_techs_all_time_scores_for_october)
print("Expected Answer: 302-177-10")

# My attempts for #6:
#1: 8746-4348-67 - Wrong!
#2: 411080-323558-4970 - Wrong!
#3: 302-177-10 - Correct!

print()
print()
georgia_techs_all_time_scores_1933_to_1963 = georgia_techs_record_from_1933_to_1963(file_contents, georgia_score_table)
print("Question #7: Georgia Tech played in the SEC from 1933 to 1963. What was its record during this time? Enter your response in the same style as the previous problem's output, Wins-Losses-Ties; for example, 100-50-25.")
print()
print("Answer #7:", georgia_techs_all_time_scores_1933_to_1963)
print("Expected Answer: 206-110-12 ")

#My attempts for #7:
#1: 4886-2008-62 - Wrong!
#2: 280767-240992-3199 - Wrong!
#3: 206-110-12 - Correct!

print()
print()
opponent_georgia_tech_scored_most_points_against = against_which_team_georgia_tech_scored_the_most_points(georgia_score_table)
print("Question #8: Against what team has Georgia Tech scored the most points?")
print()
print("Answer #8:", opponent_georgia_tech_scored_most_points_against)
print("Expected Answer: Duke")

# My attempts for #8:
#1: 'Duke' - Correct!

print()
print()
teams_georgia_tech_have_never_scored_points_against = find_teams_georgia_tech_has_never_won_points_against(georgia_score_table)
print("Question #9: What is one of the two teams that Georgia Tech has played, and yet has never scored any points against? Name either team")
print()
print("Answer #9:", teams_georgia_tech_have_never_scored_points_against)
print("Expected Answer: Carnegie Tech. Note there are more than 1 possible answers")

# My attempts for #9: 
#1: 'Utah' - Wrong!
#2: Carnegie Tech - Correct!

print()
print()
no_of_teams_have_never_scored_a_point_against_GT = number_of_teams_have_never_scored_a_point_against_GT(georgia_score_table)
print("Question #10: How many teams has played Georgia Tech and never scored a point?")
print()
print("Answer #10:", no_of_teams_have_never_scored_a_point_against_GT)
print("Expected Answer: 11")

# My attempts for #10:
#1: 226 - Wrong!
#2: 11 - Correct!

print()
print()
team_GT_has_highest_scoring_differential_against = find_team_GT_has_the_alltime_highest_scoring_differential_against(georgia_score_table)
print("Question #11: Against what team does Georgia Tech have the highest scoring differential (points for minus points against) all-time?")
print()
print("Answer #11:", team_GT_has_highest_scoring_differential_against)
print("Expected Answer: Tulane")

# My attempts for #11: 
#1: 'Tulane' - Correct!

print()
print()
team_GT_has_the_highest_avg_score_differential_against = find_team_GT_has_the_highest_avg_score_differential_against(georgia_score_table)
print("Question #12: Among teams that Georgia Tech has played at least 5 times, against which team does Georgia Tech have the highest average score differential (points for minus points against, divided by number of games)?")
print()
print("Answer #12:", team_GT_has_the_highest_avg_score_differential_against)
print("Expected Answer: Furman")

# My attempts for #12:
#1: 'Furman' - Correct!

print()




