#MARTA Breeze Card Taps
#In this problem, we're giving you a file containing some real data from
#the Marta (Atlanta's subway system) database. Each line of the file is
#a record of a single ride at a specific Marta station. Riders enter and
#exit the subway system by tapping a Breeze Card against a gate at a
#specific station.
#
#You can see a preview of what the file will look like in
#marta_sample.csv in the dropdown in the top left. Note, however, that
#the real dataset is massive: over 200,000 individual rides are recorded.
#So, you're going to be dealing with some pretty big data!

#Note: NB: expect 200'000 lines of code (real file)
#
#Each line of the file contains six items, separated by commas:
#
# - the transit day, in MM/DD/YYYY format.
# - the transit time, in HH:MM:SS format.
# - the device ID, an identifer of the gate at which the rider entered.
# - the station ID, a numeric identifier the station.
# - the use type, whether the rider was entering, exiting, etc.
# - a serial number, the unique identifier of the rider's Breeze Card.
#
#Your goal is to use this file to answer three questions:
#
# - What is the average number of Breeze Card taps per station?
# - What is the station ID of the station whose traffic is the closest
#   to that average?
# - What station has the least overall amount of traffic?
#
#Note that you will answer these questions in the fill-in-the-blank
#problems below, _not_ in this coding exercise. So, you don't have to
#programmatically find the station ID closest to the average: you could
#just print all the stations and their averages, then visually check
#which is closest to the average.
#
#To get you started, we've gone ahead and opened the file:



#You may add whatever code you want from here on to answer those three
#questions.
#
#HINT: although there are six items on each line of the file, you only
#need one of them: station ID. If you use split(",") to split up each
#line, station ID will be at index 3 on the list.
#
#HINT 2: You'll probably want to use a dictionary, with station IDs as
#the keys and 

def packingStationNamesIntoDict(filename):
    stationNamesFile = open(filename, "r")
    fileContents = stationNamesFile.readlines()
    stationNamesFile.close()

    dict_of_stations = {}

    for line in fileContents: 
        if "\n" in line: 
            line = line.strip("\n")
        currentLine = line.split("\t")
        stationNumber = currentLine[0]
        stationName = currentLine[1]

        dict_of_stations[stationNumber] = stationName
        
    return dict_of_stations

print(packingStationNamesIntoDict("stations.txt"))
print()

def six_important_details_in_one_dict(filename):
    marta_file = open(filename, 'r')
    fileContents = marta_file.readlines()
    marta_file.close() 

    transitTimeList = []
    deviceIDList = []
    stationIDList = []
    useTypeList = []
    serialNumberList = []

    for line in fileContents:
        if "\n" in line: 
            line = line.strip("\n")
        current_line = line.split(",")

        transitTimeList.append(current_line[1])
         
        deviceIDList.append(current_line[2])
        stationIDList.append(current_line[3])
        useTypeList.append(current_line[4])
        serialNumberList.append(current_line[5])

        dict_of_details = {
            "transitTime":transitTimeList, 
            "deviceID":deviceIDList,
            "stationID":stationIDList,
            "useType":useTypeList,
            "serialNumber":serialNumberList
            }
    return dict_of_details
#print(six_important_details_in_one_dict("marta_sample.txt"))
print("We're now currently working on avg_breezeCardTaps")
def avg_breezeCardTaps(aDict): 
    cardTapsDictionary = {}
    
    #1st I want to find the total no. of taps per station:
    if "stationID" in aDict:
        list_of_stationIDs = aDict["stationID"]

    for stationID in list_of_stationIDs: 
        number_of_taps_per_station = list_of_stationIDs.count(stationID)
        cardTapsDictionary[stationID] = number_of_taps_per_station
    print("Our currentTapsDictionary currently looks like:", cardTapsDictionary)

    number_of_stations = len(cardTapsDictionary)
    print("There are", number_of_stations, "stations.")
        
    total_number_of_taps = 0
    for (stationID, number_of_taps) in cardTapsDictionary.items():
        total_number_of_taps += number_of_taps
    print("There have been", total_number_of_taps, "overall!")

    average_taps_per_station = total_number_of_taps / number_of_stations

    return average_taps_per_station
    
    

print(avg_breezeCardTaps(six_important_details_in_one_dict("marta_sample.txt")))








