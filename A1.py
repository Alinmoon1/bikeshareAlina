import time
import pandas as pd

CITY_DATA = {"chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",}
MONTH = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']   


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. Be sure to make the input .lower()
    Utilize while True: loops
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hey! Let's explore today bikeshare data!")
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Your City is: Chicago, New York City, Washington: ").lower()
        if city not in ["chicago", "new york city", "washington"]:
            print("I cant see this city,try again this command please!")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input("Your Month is: All, January, February, March, April, May, or June: ").lower()
        if month not in ["all", "january", "february", "march", "april", "may", "june"]:
            print("I cant see this month, try again this command please!")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Your Day is: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ").lower()
        if day not in ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday",]:
            print("i cant see this day, try again this command please!")
            continue
        else:
            break

    print("-" * 40)
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
    # Retrieve and load correct city

    df = pd.read_csv(CITY_DATA[city])

    # Creates new columns for analysis
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["week_day"] = df["Start Time"].dt.day_name()
    df["start_hour"] = df["Start Time"].dt.hour

    # Filter by month

    if month != "all":

        # use the index of the months list to get the corresponding int

        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # ilter by month to create the new dataframe

        df = df[df["month"] == month]

    # Filter by weekday

    if day != "all":
        df = df[df["week_day"] == day.title()]
    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    # TO DO: display the most common month

    common_month = df["month"].mode()[0]
    print("Most Common Month:", common_month)

    # TO DO: display the most common day of week

    common_day = df["week_day"].mode()[0]
    print("Most Common Day Of Week:", common_day)

    # TO DO: display the most common start hour

    сommon_hour = df["start_hour"].mode()[0]
    print("Most Common Start Hour:", сommon_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station

    start_station = df["Start Station"].mode()[0]
    print("What is the most Start Station:", start_station)
    # display most commonly used end station

    end_station = df["End Station"].mode()[0]
    print("What is the most End Station:", end_station)

    # display most frequent combination of start station and end station trip

    frequent_combination = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print("The most frequent combination of start and end stations is: ", frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()
    # display total travel time
    total_time = df["Trip Duration"].sum()
    print("The total travel time is", df["Trip Duration"].sum(), "\n")

    # display mean travel time
    av_time = df["Trip Duration"].mean()
    print("The total mean time is", df["Trip Duration"].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)

def display_raw(df):
    """Displays raw data if the users wishes to see it."""
    x = 0
    while True:
        raw = input("Do you want to see the raw data today? Enter Yes or No please:  ")
        if raw.lower() == "yes":
            print(df[x : x + 5])
            x = x + 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input("\nWould you like to restart this data? Enter yes or no please.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    main()