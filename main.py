# Import libraries
import sys
# from parser.py import *

MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
DAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY]

# our main function
if __name__=="__main__":
    # parse our arguments

    if len(sys.argv) < 3:
        print "Error: No of arguments supplied", len(sys.argv) - 1
        print "Expected: day, time"
    else:
        day = sys.argv[1]
        time = sys.argv[2]
        data = parse()

        rooms_available = get_available_rooms(day, time, data)

        print rooms_available
    # all done


def get_available_rooms(day, time, data):
    if day not in DAYS:
        return "Error: invalid day: %s" % day
    if validate_time(time) == False:
        return "Error: invalid time: %s" % time




def validate_time(time):
    time_data = time.split(':')
    hour = int(time_data[0])
    minute = int(time_data[1])

    if 0 < hour and hour < 24 and 0 < minute and minute < 60:
        return True
    else:
        return False

