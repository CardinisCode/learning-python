from sys import argv, exit
import csv

print(len(argv))
if len(argv) != 3: 
    print("Missing a command line argument!")
    exit(1)

dna_database_csv = argv[1]
dna_sequence_txt = argv[2]

def main(dna_database_csv, dna_sequence_txt):
    dna_database_file = csv.DictReader(open(dna_database_csv))  # Returns a list of dictionary

    for row in dna_database_file:   # Each line is a dictionary
        for sequence in row.keys():
            print(sequence)
        # Now I can grab the individual values in the current dictionary
        #print(row["AGATC"])         

    # dna_sequence_file = open(dna_sequence_txt, "r")

    exit(0)


# def 




main(dna_database_csv, dna_sequence_txt)




