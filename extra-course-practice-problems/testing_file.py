from datetime import datetime
class Meeting:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

print()
#Write your function here!
def check_availability(calendar, proposed_meeting):
    for meeting in calendar:
        start_time = meeting.start_time
        end_time = meeting.end_time
        
        if proposed_meeting >= start_time and proposed_meeting < end_time:
            print("Proposed meeting:", proposed_meeting)
            print("scheduled meeting: starts at", start_time, "and ends at", end_time)
            print("The proposed meeting both starts after the scheduled meeting AND ends before the scheduled meeting ends")
            return False
            
    return True


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
meetings = [Meeting(datetime(2018, 8, 1, 9, 0, 0), datetime(2018, 8, 1, 11, 0, 0)),
            Meeting(datetime(2018, 8, 1, 15, 0, 0), datetime(2018, 8, 1, 16, 0, 0)),
            Meeting(datetime(2018, 8, 2, 9, 0, 0), datetime(2018, 8, 2, 10, 0, 0))]
print(check_availability(meetings, datetime(2018, 8, 1, 12, 0, 0)))
print(check_availability(meetings, datetime(2018, 8, 1, 10, 0, 0)))
