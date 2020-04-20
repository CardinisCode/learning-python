#Q10: How many teams has played Georgia Tech and never scored a point?

def import_file_contents_into_dictionary(filename):
    record_file = open(filename, "r")
    # record_file = open('../resource/lib/public/georgia_tech_football.csv', 'r')
    file_contents =record_file.readlines()
    record_file.close()

    running_total = 0

    for index in range(1, len(file_contents)):
        line_as_list = file_contents[index].split(",")
        # opponent = line_as_list[1]
        points_against = int(line_as_list[4])

        if points_against == 0:
            running_total += 1

    return running_total

print(import_file_contents_into_dictionary("season2016.csv"))
# '../resource/lib/public/georgia_tech_football.csv'

#My answer for Q10:
# - For season2016.csv: 2
# - For their file:     226