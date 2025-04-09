def main():

    #Let's find the season under which a user's input date falls.

    print("Tell me a date by first telling me the month, then the day of the month.")
    print("For both the month and the day, make sure to only put the number it is. Jan = 1, Feb = 2, and so on until Dec = 12.")
    Month = int(input("What month is it? "))
    Day = int(input("Now what day of the month is it? "))

    #Now let's organize it using if-else statements.
    #We will organize it by determining the month and the day.
    #Certain months are entirely encapsulated within seasons, whereas other months have cutoff dates between seasons.
    #This code assigns seasonally-encapsulated months to those seasons, then separates the cornerstone months into "season 1" half and "season 2" half.

    if Month == 1 or Month == 2:
        print("The season is winter.")
    elif Month == Month == 3:
        if Day < 20:
            print("The season is winter.")
        else:
            print("The season is spring.")
    elif Month == 4 or Month == 5:
        print("The season is spring.")
    elif Month == Month == 6:
        if Day < 21:
            print("The season is spring.")
        else:
            print("The season is summer.")
    elif Month == 7 or Month == 8:
        print("The season is summer.")
    elif Month == 9:
        if Day < 23:
            print("The season is summer.")
        else:
            print("The season is fall.")
    elif Month == 10 or Month == 11:
        print("The season is fall.")
    elif Month == 12:
        if Day < 21:
            print("The season is fall.")
        else:
            print("The season is winter.")
    print("Done.")
main()
