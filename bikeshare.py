import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). 
    while True:
        city = input(
                     "Please input one of the following: Chicago, New York City, or Washington: "
                     ).lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('That is not an option, please try again.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
                      "Please input one month from January to June or 'all': "
                      ).lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('That is not an option, please try again.')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
                    "Please input a day of the week from Monday to Sunday or 'all': "
                    ).lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 
                       'saturday', 'sunday', 'all'):
            print('That is not an option, please try again.')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filter by month and day if applicable.
    Changes 'Start Time' and 'End Time' to type: datetime
    Adds columns (int) 'month' and (str) 'day_of_week' from 'Start Time'

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 
    df                = pd.read_csv(CITY_DATA[city])
    df['Start Time']  = pd.to_datetime(df['Start Time'])
    df['End Time']    = pd.to_datetime(df['End Time'])
    df['month']       = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month  != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month  = months.index(month) + 1
        df     = df[df['month'] == month]

    if day != 'all':
        df  = df[df['day_of_week'] == day.title()]
   
    return df, city, month, day


def time_stats(df, city, month, day):
    """
    Displays statistics on the most frequent times of travel within filtered data.
    Adds column (int) 'hour' as the hour in military time from 'Start Time'
    
    Args:
        (dataframe) df - Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
      """

    print(f'\nCalculating The Most Frequent Times of Travel in {city.title()}...\n')
    start_time = time.time()

    # TO DO: display the most common month and change display from (int) to (str)
    popular_month = df['month'].mode()[0]
    
    if popular_month   == 1:
        popular_month  = 'January'
    elif popular_month == 2:
        popular_month  = 'February'
    elif popular_month == 3:
        popular_month  = 'March'
    elif popular_month == 4:
        popular_month  = 'April'
    elif popular_month == 5:
        popular_month  = 'May'
    else:
        popular_month  = 'June'

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour in military time
    df['hour']   = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    #Reformat 'popular_hour' from military time to standard time
    if popular_hour   <= 11:
        popular_hour  =  str(popular_hour)         + ' AM'
    elif popular_hour == 12:
        popular_hour  =  str(popular_hour)         + ' noon'
    elif popular_hour >  12 and popular_hour <= 23:
        popular_hour  =  str((popular_hour - 12))  + ' PM'
    elif popular_hour == 24:
        popular_hour  =  str(popular_hour)         + ' midnight'

    #Print most popular month if user selected 'all'
    if month   == 'all' and day == 'all':
        print(f'The most popular month to travel is {popular_month}.') 
    elif month == 'all' and day != 'all':
        print(f'The most popular month to travel on a {day.title()} is {popular_month}.') 
    
    #Print most popular day if user selected 'all'
    if month   == 'all' and day == 'all':
        print(f'The most popular day of the week to travel is {popular_day_of_week}.') 
    elif month != 'all' and day == 'all':
        print(f'The most popular day of the week to travel in {popular_month} is {popular_day_of_week}.')
    
    #Print most popular hour, phrasing based on month and/or day == 'all' or != 'all'
    if month   == 'all' and day == 'all':
        print(f'The most popular hour to travel is {popular_hour}.')
    elif month == 'all' and day != 'all':
        print(f'The most popular hour to travel on a {day.title()} is {popular_hour}.')
    elif month != 'all' and day == 'all':
        print(f'The most popular hour to travel in {popular_month} is {popular_hour}.')
    elif month != 'all' and day != 'all':
        print(f'The most popular hour to travel in {popular_month} on a {day.title()} is {popular_hour}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Adds column (str) 'Trip Stations' from combination of 'Start Station' and 'End Station'
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station   = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Stations']   = df['Start Station'] + ' to ' + df['End Station']
    popular_trip_stations = df['Trip Stations'].mode()[0]

    print(f'The most popular starting station is: {popular_start_station}')
    print(f'The most popular ending station is:   {popular_end_station}')
    print(f'The most popular trip is:             {popular_trip_stations}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time - 'End Time' and 'Start Time' must be dtype: datetime
    travel_time = df['End Time'] - df['Start Time']
    print(f'Total travel time was:   {travel_time.sum()}')
    
    # TO DO: display mean travel time
    print(f'Average travel time was: {travel_time.mean()}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('By User Type:')
        print(df['User Type'].value_counts())
    except KeyError:
        print('User type data is not available')

    # TO DO: Display counts of gender
    try:
        print('\nBy Gender:')
        print(df['Gender'].value_counts())
    except KeyError:
        print('Gender data is not available.')                  

    # TO DO: Display earliest, most recent, and most common year of birth
    try:    
        print('\nBy Birth year:')
        print(f"The earliest user birth year was:    {int(df['Birth Year'].min())}")
        print(f"The most recent user birth year was: {int(df['Birth Year'].max())}")
        print(f"The most common user birth year was: {int(df['Birth Year'].mode()[0])}")
    except KeyError:
        print('Birth year data is not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Displays 5 lines of raw data upon request.
    Asks user if they want to display 5 rows of raw data. Keeps asking as long user inputs 'yes'.
    Loop stops once user inputs 'no'.

    Args:
        (str) five_rows - "yes" or "no" if user wants to display 5 rows of data
    """
   
    #Set DataFrame row index to 0
    row_i = 0
    
    #Loop resets index to filtered data and prints the df rows by index advancing by 5 on each 'yes' loop
    #Loop breaks if user inputs 'no'
    while True:
        five_rows = input('\nWould you like to display 5 rows of the raw data? Enter yes or no.\n').lower()
        if five_rows not in ('yes', 'no'):
            print('That is not an option, please enter yes or no')
        elif five_rows == 'yes':
            print(pd.DataFrame(df.reset_index(drop=True), index=[row_i, row_i + 1, row_i + 2, row_i + 3, row_i + 4]))
            row_i += 5
            continue
        else:
            break 

    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        df, city, month, day = load_data(city, month, day)
        time_stats(df, city, month, day)
        
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
