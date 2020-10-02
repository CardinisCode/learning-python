from sys import argv, exit
import csv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

dna_database_csv = argv[1]
dna_sequence_txt = argv[2]


def main(dna_database_csv, dna_sequence_txt):
    dna_database_file = csv.DictReader(open(dna_database_csv))  # Returns a list of dictionary
    dna_sequence_file = open(dna_sequence_txt, "r")
    sequence_file_contents = dna_sequence_file.readline()

    sequence_list = []
    for char in sequence_file_contents:
        sequence_list.append(char)

    str_count = {
        "AGATC": 0,
        "TTTTTTCT": 0,
        "AATG": 0,
        "TCTAG": 0,
        "GATA": 0,
        "TATC": 0,
        "GAAA": 0,
        "TCTG": 0
    }

    # Every potential dna sequence to be found in the file/s:
    search_sequences = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]

    # For every sequence in our list of possible sequences
    for current_sequence in search_sequences:
        # Search the open txt file and count the number of consecutive occurences of the current sequence
        count = search_sequences_file_contents(sequence_list, current_sequence)
        # Update the str_count dict to reflect this count for this current sequence
        str_count[current_sequence] = count

    for row in dna_database_file:   # Each line is a dictionary
        for sequence in row.keys():  # Now to search through each dictionary
            match = False
            # To ensure the 'name' field does'nt get picked up in the comparisons to follow:
            if sequence in str_count.keys():
                # If there's a match between the current values in the Dictionary and the Sequence:
                if int(row[sequence]) == str_count[sequence]:
                    match = True
                # However if there's no match, we want to move onto the next sequence and 'match' reverts to False
                else:
                    match = False
                    break
        # If every sequence for this individual matches the STR counts in the current txt file:
        if match:
            # We can print the individual's name, close the files and exit.
            print(row["name"])
            dna_sequence_file.close()
            exit(0)

    print("No match.")
    dna_sequence_file.close()
    exit(0)


def search_sequences_file_contents(sequence, search_string):
    longest_sequence_count = 0
    index = 0
    count = 0
    len_search_string = len(search_string)

    while(index < len(sequence) - len_search_string + 1):
        current = "".join(sequence[index: index + len_search_string])

        if current == search_string:
            count += 1
            index += len_search_string

        else:
            index += 1
            if count > longest_sequence_count:
                longest_sequence_count = count
            count = 0

    return longest_sequence_count


main(dna_database_csv, dna_sequence_txt)