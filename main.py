# Import libraries
import sys
from parser import *

MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
DAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY]

def get_available_rooms(day, time):
    if day not in DAYS:
        return "Error: invalid day: %s" % day
    if validate_time(time) == False:
        return "Error: invalid time: %s" % time

    data = parse()
    rooms = getRoomList()

    available_rooms = []


    query_time = get_query_time(time)

    for room in rooms:
        if data[day][room][query_time] == True:
            available_rooms.append(room)

    return available_rooms


def validate_time(time):
    time_data = get_time_data(time)
    hour = time_data[0]
    minute = time_data[1]

    if 0 < hour and hour < 24 and 0 < minute and minute < 60:
        return True
    else:
        return False

def get_time_data(time):
    time_parts = time.split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])

    return [hour, minute]

def round_down_to_half_hour(hour, minute):
    if 0 < minute and minute < 30:
        minute = 0
    else:
        minute = 30

    return [hour, minute]


def get_query_time(time):
    time_data = get_time_data(time)
    query_data = round_down_to_half_hour(time_data[0], time_data[1])

    query_hour = query_data[0]
    query_minute = query_data[1]

    if query_hour == 0:
        query_hour = "00"
    elif query_hour < 10:
        query_hour = "0%d" % query_hour

    if query_minute == 0:
        query_minute = "00"
    elif query_minute < 10:
        query_minute = "0%d" % query_minute

    # both query_hour and query_minute should be strings now

    return "%s:%s" % (query_hour, query_minute)



# our main function
if __name__=="__main__":
    # parse our arguments

    if len(sys.argv) < 3:
        print "Error: No of arguments supplied", len(sys.argv) - 1
        print "Expected: day, time"
    else:
        day = sys.argv[1]
        time = sys.argv[2]

        rooms_available = get_available_rooms(day, time)

        print "Rooms Available:"
        for room in rooms_available:
            print "\t%s" % room
        if len(rooms_available) == 0:
            print "None"
    # all done
