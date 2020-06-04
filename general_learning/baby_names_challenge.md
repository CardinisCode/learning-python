In these problems, we'll be using a database of names from the United States Social Security Administration. It lists the frequency with which each name has been given to girls and boys in the 2010s. Our version only lists names used at least 25 times for at least one gender so far this decade.

#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

#names_file = open('../resource/lib/public/babynames.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.

Q1: How many total names are listed in the database?
Q2: How many total births are covered by the names in the database?
Q3: How many different boys' names are there that begin with the letter Z? (Count the names, not the people.)
Q4: What is the most common girl's name that begins with the letter Q?
Q5: How many total babies were given names that both start and end with vowels (A, E, I, O, or U)?
Q6: What letter is the least common first letter of a baby's name (in terms of number of babies with names starting with that letter, not number of names)?
Q7: How many babies were born with names starting with that least-common letter?
Q8: What letter is the most common first letter of a baby's name (in terms of number of babies with names starting with that letter, not number of names)?
Q9: How many babies were born with names starting with that most-common letter?
Q10: By default, the Social Security Administration's data separates out names by gender. For example, Jamie is listed separately for girls and for boys. If you were to remove this separation, what would be the most common name in the 2010s regardless of gender?
Q11: How many people would have that name?
Q12: What name that is used for both genders has the smallest difference in which gender holds the name most frequently? In case of a tie, enter any one of the correct answers.