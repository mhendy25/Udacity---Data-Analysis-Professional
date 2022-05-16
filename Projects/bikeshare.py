#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 16:44:13 2022

@author: hendy
"""

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please choose a city from Chicago, New York, or Washington: ')
        if city.lower() in CITY_DATA.keys():
            city = CITY_DATA[city.lower()]
            break
        print('Please enter a valid city name')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month from January to June: ')
        month_list = ['january','february','march','april','may','june']
        if month.lower() in month_list:
            month = month.lower()
            break
        print('Please enter a valid month: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day: ')
        day_list = ['monday','tuesday','sunday','wednesday','thursday','friday']
        if day.lower() in day_list:
            day = day.lower()
            break 
        print('Please enter a valid day')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(city)

 
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
   
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common month:',months[df['month'].mode()[0]-1])

    # TO DO: display the most common day of week
    print('Most common day:',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    print('Most common start hour:',df['Hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:',common_start_station)
    

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:',common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    print('Most frequent combination:',df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)
    


    # TO DO: display mean travel time
    print('Mean travel time:',total_travel_time/df.shape[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:','\n')
    print(df['User Type'].value_counts(),'\n')


    # TO DO: Display counts of gender
    print('Counts of gender:','\n')
    print(df['Gender'].value_counts(),'\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earliest birth year:', df['Birth Year'].min())
    print('Most recent birth year:', df['Birth Year'].max())
    print('Most common year of birth:', df['Birth Year'].mode()[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city[:10] == 'washington':
            print('Counts of user types:\n'+str(df['User Type'].value_counts()))
        else:
            user_stats(df)
        sample = 5
        start = 0
        pd.set_option('display.max_columns',200)
        while True:
            see_data = input('Do you want to see a sample of row data? [yes/no]\n')
            if see_data.lower()=='yes' and sample <= df.shape[0]-1:  
                print(df.iloc[start:sample,:])
                sample+=5
                start+=5
            elif see_data.lower() == 'no':
                  break
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
