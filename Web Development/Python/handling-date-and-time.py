# in this lesson, I am going to be working with python datetime module for handling and working with date and time in python
# python datetime module provides an efficient way of handling and manipulating time and dates 
# also, this module allows for the handling and manipulation of python timezone and creating of future time and dates 

import pytz
import datetime

# first, getting the current full date and time
print("Current date and time is: ", datetime.datetime.now())

# from a single datetime object, many data and time related objects can be extracted
print()
date_and_time = datetime.datetime.now()
print("current Year is {} and the current month is {}".format(date_and_time.year, date_and_time.strftime("%B")))

# the date and time can also be formatted nicely such that date and time information can be properly printed in human readable formats

print("\n{}".format(date_and_time.strftime("Event happened on %d{0} of %B, %Y at %I:%M %p")))

# datetime strings can also be parsed and then converted to datetime or date object
incidence_date = "2025 10 21"
incidence_date = datetime.date.strptime(incidence_date, "%Y %m %d")
print(incidence_date)

# and now it is easy to work with the date object
print(f"\nthe month name for {str(incidence_date)} is {incidence_date.strftime("%B")} and the day is ", incidence_date.strftime("%A"))  #  getting the full month name of the date

# creating datetime objects for future is possible
tomorrow = datetime.timedelta(days=1) + datetime.datetime.now()

# also making computation between dates and time objects is possible
print("the date and time for tommorow is {}".format(tomorrow))

# now it is possible to get the full name of the day
print("\n tomorrow is {0} and by this time tomorrow in sha Allah the time will be {1}".format(tomorrow.strftime("%A"), tomorrow.strftime("%I:%M %p")))

print()
# working with timezones can be very difficult especially if we are building an application that is used by many users in different locations
# in this case, the ability to easily convert between various time is crucial and important
# let's say a user in Lagos shedules an event with another user in Tokyo in Japan, there should be a way to present time to both user
# so that they both get the same accurate time of the meeting

lagos_user_time = datetime.datetime.now() + datetime.timedelta(hours=2)
print("Lagos User Time:", lagos_user_time)

# and this user has a meeting with someone  in Tokyo
# first the lagos timezone needs to be converted to utc first
lagos_time_utc = lagos_user_time.astimezone(pytz.utc)
print("Lagost Time to UTC:", lagos_time_utc)

# and now we can now convert the date and time to tokyo date and time
tokyo_user_utc = pytz.timezone('Asia/Tokyo')
tokyo_user_time = lagos_time_utc.astimezone(tokyo_user_utc)
print("Tokyo User Time is:", tokyo_user_time)
print('\nLagos Time [{}] -> Tokyo User Time [{}]'.format(lagos_user_time.strftime("%I:%M %p"), tokyo_user_time.strftime('%I:%M %p')))


print("\n{0:=^100}\n".format('[INTERNATIONAL FLIGHT TIME DISPLAY]'))
# this is a mimick of an airport board that shows the departure and the arrival time of passengers 
# the airport is located in London in UK and it carries passengers that are travelling to, Tokyo, America, and China and it departs by 10:30 Am
# Here is a board that shows the departure time and also the arrival time for each passenger on-board, given that each passenger will use the same time of arrival and no stop-over


flight_duration_time = datetime.timedelta(hours=11, minutes=30)
flight_departure_location = 'Europe/London'
europe_tz = pytz.timezone(flight_departure_location)
flight_departure_time = europe_tz.localize(datetime.datetime(2025, 3, 29, 0, 30))
destination_list = {
    'China':"Asia/Shanghai", 'Tokyo':'Asia/Tokyo', 'America':'America/Los_Angeles'
}

total_flight_duration = (flight_departure_time).astimezone(pytz.utc) + flight_duration_time


print("{0:^105}\n".format('[Amot Flight Information Display System]'))
print("{0:^25} {1:^25} {2:^25} {3:^25}".format('Departing from', "Going to", 'Departure Time', "Arrival Time",))
print("{0:-<25} {0:-<25} {0:-<25} {0:-<25}".format(""))
for location in destination_list:
    location_tz = pytz.timezone(destination_list[location])
    arrival_time = total_flight_duration.astimezone(location_tz)
    print("{0:^25} {1:^25} {2:^25} {3:^25}".format(
        flight_departure_location.replace('/', " "), location, flight_departure_time.strftime("%Y %B %d %I:%M %p"), arrival_time.strftime("%Y %B %d %I:%M %p")))

