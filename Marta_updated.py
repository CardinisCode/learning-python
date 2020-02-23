import unittest

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

def load_stations(filename):
    station_file = open(filename, "r")
    file_contents = station_file.readlines()
    station_file.close()

    stations_dictionary = {} 

    for line in file_contents:
        split_line = line.split("\t")
        station_number = split_line[0]
        station_name = split_line[1].strip()
        stations_dictionary[station_number] = station_name

    return stations_dictionary


def load_marta_file(filename):
    marta_file = open(filename, "r")
    file_contents = marta_file.readlines()
    marta_file.close()

    rides_per_station = {}
    for line in file_contents:
        split_line = line.split(",")
        station_ID = split_line[3]
        individual_ride = {
            "day": split_line[0],
            "time": split_line[1],
            "device_id": split_line[2],
            "station_id": station_ID,
            "use_type": split_line[4],
            "serial_number": split_line[5].strip()
        }
        if not station_ID in rides_per_station:
            rides_per_station[station_ID] = []
        rides_per_station[station_ID].append(individual_ride)

    return rides_per_station


def average_taps_per_stations(rides_per_station):
    total_taps = 0.0
    number_of_stations = len(rides_per_station)
    
    for rides in rides_per_station.values():
        total_taps += len(rides)

    return total_taps / number_of_stations


def station_with_least_traffic(rides_per_station):
    station_with_least_traffic = ""
    minimal_number_of_trips = None

    for station, rides in rides_per_station.items():
        number_of_trips = len(rides)

        if minimal_number_of_trips == None: 
            minimal_number_of_trips = number_of_trips
            station_with_least_traffic = station

        if number_of_trips < minimal_number_of_trips: 
            minimal_number_of_trips = number_of_trips
            station_with_least_traffic = station

    return station_with_least_traffic


def get_total_trips_per_station(rides_per_station): 
    trips_per_station = []
    for station, rides in rides_per_station.items():
        trips_per_station.append({
            "station": station, 
            "trips": len(rides)
        })

    return trips_per_station


def find_closest_to_average(average_taps, rides_per_station):
    closest_to_average = []
    difference = None
    for station, rides in rides_per_station.items():
        current = abs(len(rides) - average_taps)
        if difference == None: 
            closest_to_average.append(station)
            difference = current
        elif difference == current: 
            closest_to_average.append(station)
        elif difference > current: 
            closest_to_average = [station]
            difference = current
    
    return closest_to_average


def output_data():
    filename = ''
    rides_per_station = load_marta_file(filename)
    average_taps = average_taps_per_stations(rides_per_station)
    print("Average taps:", average_taps)
    print("Least Traffic:", station_with_least_traffic(rides_per_station))
    print("Closest to Average:", find_closest_to_average(average_taps, rides_per_station))

#Answers submitted: 
#Q1: What is the average number of Breeze Card taps per station? (Only consider stations with at least one tap.)
#My Answer: 5847.973684210527

#Q2: Which station has traffic closest to the average? (Enter the numeric station ID)
#My answer: 24

#Q3: Which station has the least traffic? (Enter the numeric station ID)
#My answer: 23

#All 3 answers were correct (As per their grading)

# Code written by Andi, Tests written by Peter
class TestMarta(unittest.TestCase):
    def test_should_return_closest_to_average(self):
        rides_per_station = load_marta_file('marta_sample.txt')
        average_taps = average_taps_per_stations(rides_per_station)

        actual = find_closest_to_average(average_taps, rides_per_station)

        self.assertEqual(["30", "31"], actual)

    # - What is the station ID of the station whose traffic is the closest
    #   to that average?
    def test_should_return_all_stations_and_total_trips(self):
        rides_per_station = load_marta_file('marta_sample.txt')
        output = [
            { "station": "30", "trips": 6 },
            { "station": "31", "trips": 4 }
        ]

        actual = get_total_trips_per_station(rides_per_station)

        self.assertEqual(output, actual)

    # - What station has the least overall amount of traffic?
    def test_should_return_station_with_least_traffic(self):
        rides_per_station = load_marta_file('marta_sample.txt')

        actual = station_with_least_traffic(rides_per_station)

        self.assertEqual("31", actual)

    def test_should_return_ave_taps_of_5_for_file(self):
        rides_per_station = load_marta_file('marta_sample.txt')

        actual = average_taps_per_stations(rides_per_station)

        self.assertEqual(5.0, actual)

    def test_should_load_stations(self):
        expected_stations = {
            '00': 'MARTA Training',
            '01': 'CTS Test Lab 1',
            '02': 'Test Bus Facility',
            '03': 'HPEM Lab'
        }

        result = load_stations('station_small.txt')

        self.assertEqual(expected_stations, result)

    def test_should_load_marta_file_correctly(self):
        # - the transit day, in MM/DD/YYYY format.
        # - the transit time, in HH:MM:SS format.
        # - the device ID, an identifer of the gate at which the rider entered.
        # - the station ID, a numeric identifier the station.
        # - the use type, whether the rider was entering, exiting, etc.
        # - a serial number, the unique identifier of the rider's Breeze Card.

        def create_entry(day, time, device_id, station_id, use_type, serial_number):
            return {
                "day": day,
                "time": time,
                "device_id": device_id,
                "station_id": station_id,
                "use_type": use_type,
                "serial_number": serial_number
            }
        
        expected_marta = {
            '30': [
                create_entry('01/18/2016', '12:01:08', 'RVG10405', '30', '9', '3E8CADDB574A4E4A'),
                create_entry('01/18/2016', '08:01:06', 'RVG10402', '30', '9', '3E8CADDF4A674E4A'),
                create_entry('01/18/2016', '16:01:03', 'RVG10402', '30', '9', '3E8CADF935024E4A')
            ]
        }

        actual = load_marta_file('small_marta.csv')

        self.assertEqual(expected_marta, actual)
        

if __name__ == '__main__':
    unittest.main()
