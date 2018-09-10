import csv
import time
from datetime import datetime
from pprint import pprint
## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'
month_filter = ""
day_filter = 0

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    # TODO: handle raw input and complete function
    # handle raw input
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')# ask the user to input the name
        if city.lower() not in ('chicago', 'new york', 'washington'):#check if it is valid input
            print("Wrong input. Please input again.")#if not, ask the user to input again
        else:
            break
    # return the file name
    if city.lower() == 'chicago':
        return chicago
    elif city.lower() == 'new york':
        return new_york_city
    elif city.lower() == 'washington':
        return washington



def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function
    # handle raw input
    while True:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')# ask the user to input filter
        if time_period.lower() not in ('month', 'day', 'none'):#check if it is valid input
            print("Wrong input. Please input again")#if not, ask the user to input again
        else:
            break

    #set global variable for month or day
    global month_filter
    global day_filter

    if time_period.lower() == 'month':
        month_filter = get_month()
    elif time_period.lower() == 'day':
        day_filter = get_day()
    elif time_period.lower() == 'none':
        month_filter = ''
        day_filter = 0

    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''

    # TODO: handle raw input and complete function
    #handle raw input
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')# ask the user to input which month
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):#check if it is a valid input
            print("Wrong input. Please input again.")#if not, ask the user to input again
        else:
            break
    # returns the specified month
    if month.lower() == 'january':
        return month
    elif month.lower() == 'february':
        return month
    elif month.lower() == 'march':
        return month
    elif month.lower() == 'april':
        return month
    elif month.lower() == 'may':
        return month
    elif month.lower() == 'june':
        return month



def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function
    # handle raw input
    while True:
        day = input('\nWhich day? Please type your response as an integer.\n')#ask the user to input which day
        if day.lower() not in ('1', '2', '3', '4', '5', '6', '7'):#check if it is a valid input
            print("Wrong input. Please input again.")#if not, ask the user to input again
        else:
            break

    # returns the day
    if day.lower() == '1':# if the input is 1, return 1
        return int(day)
    elif day.lower() == '2':
        return int(day)
    elif day.lower() == '3':
        return int(day)
    elif day.lower() == '4':
        return int(day)
    elif day.lower() == '5':
        return int(day)
    elif day.lower() == '6':
        return int(day)
    elif day.lower() == '7':
        return int(day)



def keywithmaxval(d):
    # return the key with the max value

    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    month_counts = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0}
    for row in city_file:
        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')# use datetime to parse dates
        month = date.strftime('%B')
        month_counts[month] += 1
    max_key = keywithmaxval(month_counts)# the most popular month

    return (max_key, month_counts[max_key])


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    day_counts = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
    for row in city_file:
        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        if time_period == 'month':
            month = date.strftime('%B').lower()
            if month == month_filter:
                day = date.strftime('%A')
                day_counts[day] += 1
        else:
            day = date.strftime('%A')
            day_counts[day] += 1
    max_key = keywithmaxval(day_counts)# the most popular day
    return (max_key, day_counts[max_key])


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    hour_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
                   16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0}


    for row in city_file:
        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        if time_period == 'month':
            month = date.strftime('%B').lower()
            if month == month_filter:
                hour = date.hour
                hour_counts[hour] += 1
        elif time_period == 'day':
            day = int(date.strftime('%w')) + 1
            if day == day_filter:
                hour = date.hour
                hour_counts[hour] += 1
        else:
            hour = date.hour
            hour_counts[hour] += 1

    max_key = keywithmaxval(hour_counts)# the most popular hour
    return (max_key, hour_counts[max_key])


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    # initialize count variables
    n_trips = 0
    n_trip_totals = 0
    avg_trip = 0

    for row in city_file:
        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        if time_period == 'month':#check if month filter
            month = date.strftime('%B').lower()
            if month == month_filter:
                n_trips += 1
                n_trip_totals += float(row['Trip Duration'])
        elif time_period == 'day':# check if day filter
            day = int(date.strftime('%w')) + 1
            if day == day_filter:
                n_trips += 1
                n_trip_totals += float(row['Trip Duration'])
        else:
            n_trips += 1
            n_trip_totals += float(row['Trip Duration'])


    avg_trip = n_trip_totals / n_trips
    return (n_trip_totals, n_trips, avg_trip)


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    StartDict = {}
    EndDict = {}
    # TODO: complete function
    for row in city_file:
        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        Start = row['Start Station']
        End = row['End Station']
        if time_period == 'month':
            month = date.strftime('%B').lower()
            if month == month_filter:
                if Start in StartDict:
                    StartDict[Start] += 1
                else:
                    StartDict[Start] = 1

                if End in EndDict:
                    EndDict[End] += 1
                else:
                    EndDict[End] = 1
        if time_period == 'day':
            day = int(date.strftime('%w')) + 1
            if day == day_filter:
                if Start in StartDict:
                    StartDict[Start] += 1
                else:
                    StartDict[Start] = 1

                if End in EndDict:
                    EndDict[End] += 1
                else:
                    EndDict[End] = 1
        else:
            if Start in StartDict:
                StartDict[Start] += 1
            else:
                StartDict[Start] = 1

            if End in EndDict:
                EndDict[End] += 1
            else:
                EndDict[End] = 1

    max_key1 = keywithmaxval(StartDict)# the key with maximum value for start station
    max_key2 = keywithmaxval(EndDict)#the key with maximum value for end station

    return (max_key1, StartDict[max_key1], max_key2, EndDict[max_key2])


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    TripDict = {}
    TripKey = ();

    for row in city_file:
        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        Start = row['Start Station']
        End = row['End Station']
        TripKey = (Start, End)
        if time_period == 'month':#check if month filter
            month = date.strftime('%B').lower()
            if month == month_filter:
                if TripKey in TripDict:
                    TripDict[TripKey] += 1
                else:
                    TripDict[TripKey] = 1
        elif time_period == 'day':#check if day filter
            day = int(date.strftime('%w')) + 1
            if day == day_filter:
                if TripKey in TripDict:
                    TripDict[TripKey] += 1
                else:
                    TripDict[TripKey] = 1
        else:
            if TripKey in TripDict:
                TripDict[TripKey] += 1
            else:
                TripDict[TripKey] = 1

    max_key = keywithmaxval(TripDict)# the key with maximum value for trip

    return (max_key, TripDict[max_key])


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function

    user_counts = {'Subscriber': 0, 'Customer': 0,'Dependent': 0, '': 0}


    for row in city_file:

        date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        if time_period == 'month':# check if month filter
            month = date.strftime('%B').lower()
            if month == month_filter:
                user_counts[row['User Type']] += 1
        elif time_period == 'day':#check if day filter
            day = int(date.strftime('%w')) + 1
            if day == day_filter:
                user_counts[row['User Type']] += 1
        else:
            user_counts[row['User Type']] += 1

    return (user_counts['Subscriber'], user_counts['Customer'])


def gender(city, city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function

    gender_counts = {'Male': 0, 'Female': 0, '': 0}
    if city==new_york_city or city==chicago:#check if new york or chicago

        for row in city_file:

            date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
            if time_period == 'month':
                month = date.strftime('%B').lower()
                if month == month_filter:
                    gender_counts[row['Gender']] += 1
            elif time_period == 'day':
                day = int(date.strftime('%w')) + 1
                if day == day_filter:
                    gender_counts[row['Gender']] += 1
            else:
                gender_counts[row['Gender']] += 1
        return (gender_counts['Male'], gender_counts['Female'])
    else: #check if washington, if so, there is no Gender data, so output unknown information
        return 'unknown information'




def birth_years(city, city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest, most recent, and most popular birth years?
    '''
    # TODO: complete function

    BirthDict = {}
    EarliestYear = 8000.0
    MostRecentYear = 0.0
    # TODO: complete function
    if city == new_york_city or city == chicago:#check if new york or chicago

        for row in city_file:
            if row['Birth Year'] != '':
                date = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
                if time_period == 'month':
                    month = date.strftime('%B').lower()
                    if month == month_filter:
                        if row['Birth Year'] in BirthDict:
                            BirthDict[row['Birth Year']] += 1
                        else:
                            BirthDict[row['Birth Year']] = 1
                        if float(row['Birth Year']) > MostRecentYear:
                            MostRecentYear = float(row['Birth Year'])
                        if float(row['Birth Year']) < EarliestYear:
                            EarliestYear = float(row['Birth Year'])
                elif time_period == 'day':
                    day = int(date.strftime('%w')) + 1
                    if day == day_filter:
                        if row['Birth Year'] in BirthDict:
                            BirthDict[row['Birth Year']] += 1
                        else:
                            BirthDict[row['Birth Year']] = 1
                    if float(row['Birth Year']) > MostRecentYear:
                        MostRecentYear = float(row['Birth Year'])
                    if float(row['Birth Year']) < EarliestYear:
                        EarliestYear = float(row['Birth Year'])
                else:
                    if row['Birth Year'] in BirthDict:
                        BirthDict[row['Birth Year']] += 1
                    else:
                        BirthDict[row['Birth Year']] = 1
                    if float(row['Birth Year']) > MostRecentYear:
                        MostRecentYear = float(row['Birth Year'])
                    if float(row['Birth Year']) < EarliestYear:
                        EarliestYear = float(row['Birth Year'])
        max_key = keywithmaxval(BirthDict)#the key with maximum value for BirthDict

        return (EarliestYear, MostRecentYear, max_key, BirthDict[max_key])
    else:#check if washington, if so, there is no Birth Year data, so output unknown information
        return 'unknown information'





def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''

    # TODO: handle raw input and complete function


    for row in city_file:
        display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')#ask the user if want to view trip data
        if display.lower() == 'no':#check the input, if no, then stop
            break
        elif display.lower() == 'yes':#if yes, then print and count
            count = 0
            while count<5:
                pprint(row)
                count += 1
            if count == 5:#when print five lines
                while True:
                    display = input('\nWould you like to view individual trip data?'
                                'Type \'yes\' or \'no\'.\n')#ask again
                    break

                if display.lower() == 'yes':
                    count = 0
                    while count<5:
                        pprint(row)
                        count += 1
                else:
                    break
        else:#if the input are not yes or no as a valid input, then ask the user input again
            print('Wrong input. Please input again')

    return


#build a function to read csv file
def csv_file(file):

    with open(file, 'r') as f_in:
        reader = csv.DictReader(f_in)
        data = []
        for line in reader:
            data.append(line)



    return data

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    city_file=csv_file(city)
    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')
    start_time = time.time()

    # What is the most popular month for start time?
    if time_period == 'none':
        # TODO: call popular_month function and print the results
        result = popular_month(city_file, time_period)
        print("Most popular month:{0}, Count:{1}, Filter:{2}".format(result[0], result[1], time_period))


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
# TODO: call popular_day function and print the results
        result = popular_day(city_file, time_period)
        print("Most popular day:{0}, Count:{1}, Filter:{2}".format(result[0], result[1], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What is the most popular hour of day for start time?
# TODO: call popular_day function and print the results
    result = popular_hour(city_file, time_period)
    print("Most popular hour:{0}, Count:{1}, Filter:{2}".format(result[0], result[1], time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What is the total trip duration and average trip duration?
# TODO: call trip_duration function and print the results
    result = trip_duration(city_file, time_period)
    print("Total Duration:{0}, Count:{1}, Average Duration:{2}, Filter:{3}".format(result[0], result[1], result[2],
                                                                               time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What is the most popular start station and most popular end station?
# TODO: call popular_stations function and print the results
    result = popular_stations(city_file, time_period)
    print("Start Station:{0}, Count:{1} - End Station:{2}, Count:{3}, Filter:{4}".format(result[0], result[1], result[2],
                                                                                     result[3], time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What is the most popular trip?
# TODO: call popular_trip function and print the results
    result = popular_trip(city_file, time_period)
    print("Trip:{0}, Count:{1}, Filter:{2}".format(result[0], result[1], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What are the counts of each user type?
# TODO: call users function and print the results
    result = users(city_file, time_period)
    print("Subscribers:{0}, Customers:{1}, Filter:{2}".format(result[0], result[1], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What are the counts of gender?
# TODO: call gender function and print the results
    result = gender(city, city_file, time_period)
    if result == 'unknown information':
        print('unknown information')
    else:
        print("Male:{0}, Female:{1}, Filter:{2}".format(result[0], result[1], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

# What are the earliest, most recent, and most popular birth years?
# TODO: call birth_years function and print the results
    result = birth_years(city, city_file, time_period)
    if result=='unknown information':
        print('unknown information')
    else:
        print("Birth Years: EarliestYear:{0}, MostRecentYear:{1}, MostPopularYear:{2}, Count:{3}, Filter:{4}".format(result[0],result[1],result[2],result[3],time_period))






    print("That took %s seconds." % (time.time() - start_time))

# Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

# Restart?
    restart = input('Would you like to restart? Type \'yes\' or \'no\'.')
    if restart.lower() == 'yes':
        statistics()

if __name__ == "__main__":
    statistics()