# In this problem, we'll do something similar to the previous one: 
# we'll give you a sandbox with access to a dataset to explore, and ask you to answer some questions about it. 
# The points on this page all come from the problems below, not the coding window.

# In these problems, we'll be using a database of names from the United States Social Security Administration. 
# It lists the frequency with which each name has been given to girls and boys in the 2010s. 
# Our version only lists names used at least 25 times for at least one gender so far this decade.

#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:

names_file = open('../resource/lib/public/babynames.csv', 'r')

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

first value = name
second value = the number of times the name was given in the 2010s
(so far)
third value = whether that count corresponds to girls or boys 