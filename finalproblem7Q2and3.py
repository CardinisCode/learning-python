#the next 2 questions I'll answer at the same time:
# Q2: How many points has Georgia Tech scored all-time against Auburn?
# Q3: How many points has Auburn scored all-time against Georgia Tech?
# My Code to answer the question:

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


def all_time_record(opponent, filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    georgia_score_table = import_file_contents_into_dictionary(file_contents)

    # I used this to pull the total stats for each team, which allowed me to 
    # know what my expected stats would be using my copy of season2016.
    # # print(georgia_score_table)
    points_won_against_opponent = georgia_score_table["Auburn"]['Total Points Won by GT']
    points_won_by_opponent_against_GT = georgia_score_table["Auburn"]['Total Points Lost by GT']
    print("Auburn")
    print("GT has", points_won_against_opponent, "points against Auburn")
    print("Auburn has", points_won_by_opponent_against_GT, "points against GT")
    return (opponent, points_won_against_opponent, points_won_by_opponent_against_GT)

#With the shortened file:
print(all_time_record("Auburn", "season2016.csv"))
#With their file (only accessible in their sandbox):
#print(all_time_record("Auburn", '../resource/lib/public/georgia_tech_football.csv'))
#My answers using their file:
# A2: 950
# A3: 880
