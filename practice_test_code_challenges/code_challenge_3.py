#Imagine you're writing a program to check if a person is
#available at a certain time.
#
#To do this, you want to write a function called
#check_availability. check_availability will have two
#parameters: a list of instances of the Meeting class, and
#proposed_time, a particular date and time.
#
#check_availability should return True (meaning the person
#is available) if there are no instances of Meeting that
#conflict with the proposed_time. In other words, it should
#return False if proposed_time is between the start_time and
#end_time for any meeting in the list of meetings.
#
#The Meeting class is defined below. It has two attributes:
#start_time and end_time. start_time is an instance of the
#datetime class showing when the meeting starts, and
#end_time is an instance of the datetime class indicating
#when the meeting ends.
#
#Hint: Instances of the datetime have at least six
#attributes: year, month, day, hour, minute, and second.
#
#Hint 2: Comparison operators work with instances of the
#datetime class. time_1 < time_2 will be True if time_1 is
#earlier than time_2, and False otherwise.
#
#You should not assume that the list is sorted.

#Here is our definition of the Meeting class:
from datetime import datetime
import unittest

class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
    
    # My partner created this method to help me convert their test data into the (correct) datetime format:
    @staticmethod
    def from_string(start, end):
        #2018-08-07 11:30:00
        def get_date_time(time_string):
            date, time = time_string.split(" ")
            year, month, day = date.split("-")
            hour, minute, second = time.split(":")
            return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

        return Meeting(get_date_time(start), get_date_time(end))


#Write your function here!
def check_availability(scheduled_meetings, potential_meeting):
    print("The potential meeting is at:", potential_meeting)
    potential_date_time = datetime(
        int(potential_meeting.year),
        int(potential_meeting.month),
        int(potential_meeting.day),
        int(potential_meeting.hour),
        int(potential_meeting.minute),
        int(potential_meeting.second)
    )
        
    for meeting in scheduled_meetings:
        start_date_time = datetime(
            int(meeting.start_time.year),
            int(meeting.start_time.month),
            int(meeting.start_time.day),
            int(meeting.start_time.hour),
            int(meeting.start_time.minute),
            int(meeting.start_time.second)
        )
        end_date_time = datetime(
            int(meeting.end_time.year),
            int(meeting.end_time.month),
            int(meeting.end_time.day),
            int(meeting.end_time.hour),
            int(meeting.end_time.minute),
            int(meeting.end_time.second)
        )

        if potential_date_time >= start_date_time and potential_date_time < end_date_time:
            return False
        
    return True







#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
# meetings = [Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
#             Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
#             Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
# print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
# print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))

meetings = [
    Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 10, 30, 0)), 
    Meeting(datetime(2018, 8, 6, 13, 30, 0), datetime(2018, 8, 6, 14, 45, 0)), 
    Meeting(datetime(2018, 8, 3, 12, 15, 0), datetime(2018, 8, 3, 14, 15, 0)), 
    Meeting(datetime(2018, 8, 1, 16, 15, 0), datetime(2018, 8, 1, 19, 0, 0)), 
    Meeting(datetime(2018, 8, 4, 15, 15, 0), datetime(2018, 8, 4, 17, 30, 0)), 
    Meeting(datetime(2018, 8, 7, 12, 30, 0), datetime(2018, 8, 7, 14, 0, 0)), 
    Meeting(datetime(2018, 8, 3, 12, 45, 0), datetime(2018, 8, 3, 14, 30, 0)), 
    Meeting(datetime(2018, 8, 1, 15, 30, 0), datetime(2018, 8, 1, 18, 30, 0))
    ]
#proposed_meeting = 2018-08-07 13:45:00

print(check_availability(meetings, datetime(2018, 8, 7, 13, 45, 0)))
# We expect check_availability to return the bool False





class TestCheckAvailability(unittest.TestCase):
    meetings = [
    Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 10, 30, 0)), 
    Meeting(datetime(2018, 8, 6, 13, 30, 0), datetime(2018, 8, 6, 14, 45, 0)), 
    Meeting(datetime(2018, 8, 3, 12, 15, 0), datetime(2018, 8, 3, 14, 15, 0)), 
    Meeting(datetime(2018, 8, 1, 16, 15, 0), datetime(2018, 8, 1, 19, 0, 0)), 
    Meeting(datetime(2018, 8, 4, 15, 15, 0), datetime(2018, 8, 4, 17, 30, 0)), 
    Meeting(datetime(2018, 8, 7, 12, 30, 0), datetime(2018, 8, 7, 14, 0, 0)), 
    Meeting(datetime(2018, 8, 3, 12, 45, 0), datetime(2018, 8, 3, 14, 30, 0)), 
    Meeting(datetime(2018, 8, 1, 15, 30, 0), datetime(2018, 8, 1, 18, 30, 0))
    ]

    # meetings = [
    #     Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
    #     Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
    #     Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]

    def test_not_available(self):
        print("---------------------")
        expected = False
        actual = check_availability(self.meetings, datetime(2018, 8, 7, 13, 45, 0))

        self.assertEqual(expected, actual)

    def test_available_for_meeting(self):
        print("---------------------")
        expected = True
        actual = check_availability(self.meetings, datetime(2018, 8, 1, 12, 0, 0))

        self.assertEqual(expected, actual)

    def test_failing_1(self):
        print("---------------------")
        meetings = [
            Meeting(datetime(2018, 8, 6, 11, 45, 0), datetime(2018, 8, 6, 13, 15, 0)), 
            Meeting(datetime(2018, 8, 5, 11, 15, 0), datetime(2018, 8, 5, 12, 45, 0)), 
            Meeting(datetime(2018, 8, 7, 12, 0, 0), datetime(2018, 8, 7, 14, 45, 0))
            ]
        expected = True
        actual = check_availability(meetings, datetime(2018, 8, 6, 11, 15, 0))

        self.assertEqual(expected, actual)


    def test_failing_2(self):
        print("---------------------")
        meetings = [
            Meeting.from_string("2018-08-07 10:15:00", "2018-08-07 11:30:00"), 
            Meeting.from_string("2018-08-06 16:45:00", "2018-08-06 19:45:00"), 
            Meeting.from_string("2018-08-06 10:30:00", "2018-08-06 12:00:00"), 
            Meeting.from_string("2018-08-04 13:30:00", "2018-08-04 15:00:00"), 
            Meeting.from_string("2018-08-03 13:30:00", "2018-08-03 15:00:00"), 
            Meeting.from_string("2018-08-01 11:15:00", "2018-08-01 12:15:00"), 
            Meeting.from_string("2018-08-01 16:45:00", "2018-08-01 18:45:00"), 
            Meeting.from_string("2018-08-06 14:15:00", "2018-08-06 16:30:00")
            ]
        expected = True
        actual = check_availability(meetings, datetime(2018, 8, 7, 11, 30, 0))
        # 2018-08-07 11:30:00

        self.assertEqual(expected, actual)
    




if __name__ == "__main__":
    unittest.main()