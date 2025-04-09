''' 
    John Gill
    Dr. Lindsay Jamieson
    CS 5001
    25 April 2023 
'''
import datetime

'''We'll be starting with the compatibility dictionary. This is in a global reference frame to be accessed anywhere in the program.
    This dictionary contains a subset of 12 dictionaries: one for each zodiac sign. Each of these sub-dictionaries 
    holds information on the compatibility their zodiac sign shares with each other zodiac sign. It maintains internal
    consistency, meaning that each key-value pair in each of these dictionaries is the same for their same respective pair in each
    other sub-dictionary, such that if one were to find "Libra" in "Capricorn", it would return the same value as 
    "Capricorn" in "Libra."'''

Sign_Compatibility_Dictionary = {

    "Capricorn": {"Virgo": 100.0, "Taurus": 100.0, "Capricorn": 85.71,"Scorpio": 71.42,
            "Pisces": 71.42,"Cancer": 57.14,"Sagittarius": 42.85,"Aquarius": 42.85,
            "Gemini": 28.57,"Leo": 28.57,"Aries": 14.28,"Libra": 14.28},

    "Aries": {"Leo": 100.0, "Sagittarius": 100.0, "Aries": 85.71, "Gemini": 71.42, 
            "Aquarius": 71.42, "Libra": 57.14, "Taurus": 42.85, "Pisces": 42.85, 
            "Virgo": 28.57, "Scorpio": 28.57, "Cancer": 14.28, "Capricorn": 14.28},

    "Taurus": {"Virgo": 100.0, "Capricorn": 100.0, "Taurus": 85.71,"Cancer": 71.42,
            "Pisces": 71.42, "Scorpio": 57.14, "Gemini": 42.85, "Aries": 42.85,
            "Libra": 28.57, "Sagittarius": 28.57, "Leo": 14.28, "Aquarius": 14.28},

    "Gemini": {"Libra": 100.0, "Aquarius": 100.0, "Gemini": 85.71, "Leo": 71.42,
            "Aries": 71.42, "Sagittarius": 57.14, "Taurus": 42.85, "Cancer": 42.85,
            "Scorpio": 28.57, "Capricorn": 28.57, "Pisces": 14.28, "Virgo": 14.28},

    "Cancer": {"Pisces": 100.0, "Scorpio": 100.0, "Cancer": 85.71, "Virgo": 71.42,   
            "Taurus": 71.42, "Capricorn": 57.14, "Gemini": 42.85, "Leo": 42.85,
            "Sagittarius": 28.57, "Aquarius": 28.57, "Aries": 14.28, "Libra": 14.28},

    "Leo": {"Aries": 100.0, "Sagittarius": 100.0,  "Leo": 85.71, "Gemini": 71.42,
            "Libra": 71.42, "Aquarius": 57.14, "Cancer": 42.85, "Virgo": 42.85,
            "Capricorn": 28.57, "Pisces": 28.57,  "Taurus": 14.28, "Scorpio": 14.28,},

    "Virgo": {"Taurus": 100.0, "Capricorn": 100.0, "Virgo": 85.71, "Scorpio": 71.42, 
            "Cancer": 71.42, "Pisces": 57.14, "Libra": 42.85, "Leo": 42.85, "Aries": 28.57,
            "Aquarius": 28.57, "Gemini": 14.28, "Sagittarius": 14.28},

    "Libra": {"Gemini": 100.0, "Aquarius": 100.0, "Libra": 85.71, "Sagittarius": 71.42,
            "Leo": 71.42, "Aries": 57.14, "Virgo": 42.85, "Scorpio": 42.85,
            "Taurus": 28.57, "Pisces": 28.57, "Cancer": 14.28, "Capricorn": 14.28},

    "Scorpio": {"Cancer": 100.0, "Pisces": 100.0, "Scorpio": 85.71, "Virgo": 71.42,
            "Capricorn": 71.42, "Taurus": 57.14, "Libra": 42.85, "Sagittarius": 42.85, 
            "Aries": 28.57, "Gemini": 28.57, "Leo": 14.28, "Aquarius": 14.28},

    "Sagittarius": {"Aries": 100.0, "Leo": 100.0, "Sagittarius": 85.71, "Aquarius": 71.42,
            "Libra": 71.42, "Gemini": 57.14, "Scorpio": 42.85, "Capricorn": 42.85,
            "Taurus": 28.57, "Cancer": 28.57, "Virgo": 14.28, "Pisces": 14.28},

    "Aquarius": {"Gemini":100.0, "Libra": 100.0, "Aquarius": 85.71, "Sagittarius": 71.42,
            "Aries": 71.42, "Leo": 57.14, "Capricorn": 42.85, "Pisces": 42.85,
            "Cancer": 28.57, "Virgo": 28.57, "Taurus": 14.28, "Scorpio": 14.28,},

    "Pisces": {"Cancer": 100.0, "Scorpio": 100.0, "Pisces": 85.71, "Taurus": 85.71,
            "Capricorn": 71.42, "Virgo": 71.42, "Aries": 57.14, "Aquarius": 42.85,
            "Leo": 28.57, "Libra": 28.57, "Gemini": 14.28, "Sagittarius": 14.28}
            }

class Zodiac:
    
    def __init__(self, date_string):

        '''This class determines the zodiac signs a user's sun, moon, and planets were in on the date of their birth.
            Birthdate is the only parameter.'''

        # Define what's an acceptable birthdate format.

        try:
            self.date = datetime.datetime.strptime(date_string, '%m/%d/%Y %H:%M')
        except ValueError:
            raise ValueError("Invalid date format, please use MM/DD/YYYY HH:MM format")
        
    def sun_sign(self):

        # Determine the sun sign based on the days in the month. Easiest method since there's no math.

        month = self.date.month
        day = self.date.day
        if month == 12:
            astro_sign = "Sagittarius" if day < 22 else "Capricorn"
        elif month == 1:
            astro_sign = "Capricorn" if day < 20 else "Aquarius"
        elif month == 2:
            astro_sign = "Aquarius" if day < 19 else "Pisces"
        elif month == 3:
            astro_sign = "Pisces" if day < 21 else "Aries"
        elif month == 4:
            astro_sign = "Aries" if day < 20 else "Taurus"
        elif month == 5:
            astro_sign = "Taurus" if day < 21 else "Gemini"
        elif month == 6:
            astro_sign = "Gemini" if day < 21 else "Cancer"
        elif month == 7:
            astro_sign = "Cancer" if day < 23 else "Leo"
        elif month == 8:
            astro_sign = "Leo" if day < 23 else "Virgo"
        elif month == 9:
            astro_sign = "Virgo" if day < 23 else "Libra"
        elif month == 10:
            astro_sign = "Libra" if day < 23 else "Scorpio"
        elif month == 11:
            astro_sign = "Scorpio" if day < 22 else "Sagittarius"

        print("Sun: ", astro_sign)    
        return astro_sign

    def moon_sign(self):

        '''All the rest of the methods in this class operate the same way.
            We start by initializing the orbits with a date when they first entered
            a new star sign, long enough ago so that nearly anyone alive today could use it. After that, we create
            a list of zodiac signs in order, starting with the sign that the moon or planet first enters at the start date.
            Then, we want the days per sign, which is calculated by getting the total orbit time and dividing
            it by the number of signs, 12. Then we divide the total number of days it had been since the start date of orbit to the given birthdate,
            to see how many times the body had changed zodiac signs. We then run that number modulo 12, which tells us how many
            signs it has gone through since its last full cycle through all 12 signs, and we use that number as the index
            to indicate which sign the body was in on that birthday.'''

        start_date = datetime.datetime(1914, 8, 7, 9, 4) # Start date for the moon in early 20th century when it first entered Pisces.
        signs = ["Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", 
                 "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius"] # Begin at Pisces.
        days_per_sign = 27.321582 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit. 
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list. The % remainder represents the sign after the last full cycle.
        print("Moon:", signs[sign_index])
        return signs[sign_index]
    
    def mercury_sign(self):

        start_date = datetime.datetime(1916, 7, 22, 20, 20) # Start date for Mercury entering a new sign in the early 20th century.
        signs = ["Cancer", "Leo", "Virgo", "Libra","Scorpio", "Sagittarius", 
                 "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini"] # Begin at Cancer.
        days_per_sign = 87.9691 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of sign changes since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Mercury:", signs[sign_index])
        return signs[sign_index]
    
    def venus_sign(self):

        start_date = datetime.datetime(1913, 6, 30, 22, 8) # Start date for Venus entering Taurus in early 20th century.
        signs = ["Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
                 "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Aries"] # Begin at Taurus.
        days_per_sign = 224.701 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Venus:", signs[sign_index])
        return signs[sign_index]
    
    def mars_sign(self):

        start_date = datetime.datetime(1910, 1, 10, 1, 57) # Start date for Mars entering Sagittarius in early 20th century.
        signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", 
                 "Sagittarius", "Capricorn", "Aquarius", "Pisces"] # Begin at Aries.
        days_per_sign = 686.980 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Mars:", signs[sign_index])
        return signs[sign_index]

    def jupiter_sign(self):

        start_date = datetime.datetime(1916, 1, 4, 12, 57) # Start date for Jupiter entering Leo in the early 20th century.
        signs = ["Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
                 "Libra", "Scorpio", "Sagittarius", "Capricorn","Aquarius"] # Begin at Pisces.
        days_per_sign = 4332.589 / 12 # 1/12th the orbital period in days
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Jupiter:", signs[sign_index])
        return signs[sign_index]
    
    def saturn_sign(self):

        start_date = datetime.datetime(1916, 8, 2, 4, 6) # Start date for Saturn entering Leo in the early 20th century.
        signs = ["Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", 
                 "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini"] # Begin at Cancer.
        days_per_sign = 10759.22 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Saturn:", signs[sign_index])
        return signs[sign_index]
    
    def uranus_sign(self):

        start_date = datetime.datetime(1902, 12, 31, 15, 55) # Start date for Uranus entering Aquarius in the early 20th century. 
        signs = ["Sagittarius", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", 
                 "Cancer", "Leo", "Virgo", "Libra", "Scorpio"] # Begin at Sagittarius.
        days_per_sign = 30685.4 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Uranus:", signs[sign_index])
        return signs[sign_index]
    
    def neptune_sign(self):

        start_date = datetime.datetime(1911, 8, 21, 23, 23) # Start date for Neptune entering Cancer in the early 20th century.
        signs = ["Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", 
                 "Capricorn","Aquarius", "Pisces", "Aries", "Taurus", "Gemini"] # Begin at Cancer.
        days_per_sign = 60189 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Neptune:", signs[sign_index])
        return signs[sign_index]
    
    def pluto_sign(self):

        start_date = datetime.datetime(1905, 8, 20, 15, 1) # start date for Pluto entering Gemini in the early 20th century.
        signs = ["Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", 
                 "Sagittarius", "Capricorn","Aquarius", "Pisces", "Aries", "Taurus"] # Begin at Gemini.
        days_per_sign = 90560 / 12 # 1/12th the orbital period in days.
        cycles_since_start = ((self.date - start_date).total_seconds() / (3600 * 24)) / days_per_sign # The number of days since the start date of orbit.
        sign_index = int(cycles_since_start % 12) # The index of the sign in the list.
        print("Pluto:", signs[sign_index])
        return signs[sign_index]

class Compatibility:

    '''This class takes zodiac signs given to it, and searches through the Sign Compatibility Dictionary
        to return the compatibility value associated with them. It takes the sun, moon, and planets as parameters.
        Each astronomical body has its own method dedicated for determining the zodiac compatibility of the 
        pair of people at its junction. Then there are four more methods: overall, romantic, friendship, and
        business compatibility. Those are calculated by taking the values returned from the compatibility dictionary,
        and calculating the average compatibility score based on the relevant astronomical bodies.'''

    def __init__(self, sun, moon, mercury, venus, mars, saturn, jupiter, neptune, uranus, pluto):
        self.sun = sun
        self.moon = moon
        self.mercury = mercury
        self.venus = venus
        self.mars = mars
        self.saturn = saturn
        self.jupiter = jupiter
        self.uranus = uranus
        self.neptune = neptune
        self.pluto = pluto

    def sun_compatibility(sun1, sun2):

        print("Your sun sign compatibility is ", Sign_Compatibility_Dictionary[sun1][sun2], "%")
        return float(Sign_Compatibility_Dictionary[sun1][sun2])
    
    def moon_compatibility(moon1, moon2):

        print("Your moon sign compatibility is ", Sign_Compatibility_Dictionary[moon1][moon2], "%")
        return float(Sign_Compatibility_Dictionary[moon1][moon2])
    
    def mercury_compatibility(mercury1, mercury2):

        print("Your Mercury sign compatibility is ", Sign_Compatibility_Dictionary[mercury1][mercury2], "%")
        return float(Sign_Compatibility_Dictionary[mercury1][mercury2])
    
    def venus_compatibility(venus1, venus2):

        print("Your Venus sign compatibility is", Sign_Compatibility_Dictionary[venus1][venus2], "%")
        return float(Sign_Compatibility_Dictionary[venus1][venus2])
    
    def mars_compatibility(mars1, mars2):

        print("Your Mars sign compatibility is", Sign_Compatibility_Dictionary[mars1][mars2], "%")
        return float(Sign_Compatibility_Dictionary[mars1][mars2])
    
    def saturn_compatibility(saturn1, saturn2):

        print("Your Saturn sign compatibility is", Sign_Compatibility_Dictionary[saturn1][saturn2], "%")
        return float(Sign_Compatibility_Dictionary[saturn1][saturn2])
    
    def jupiter_compatibility(jupiter1, jupiter2):

        print("Your Jupiter sign compatibility is", Sign_Compatibility_Dictionary[jupiter1][jupiter2], "%")
        return float(Sign_Compatibility_Dictionary[jupiter1][jupiter2])    
    
    def uranus_compatibility(uranus1, uranus2):

        print("Your Uranus sign compatibility is", Sign_Compatibility_Dictionary[uranus1][uranus2], "%")
        return float(Sign_Compatibility_Dictionary[uranus1][uranus2])
    
    def neptune_compatibility(neptune1, neptune2):

        print("Your Neptune sign compatibility is", Sign_Compatibility_Dictionary[neptune1][neptune2], "%")
        return float(Sign_Compatibility_Dictionary[neptune1][neptune2])
    
    def pluto_compatibility(pluto1, pluto2):

        print("Your Pluto sign compatibility is", Sign_Compatibility_Dictionary[pluto1][pluto2], "%")
        return float(Sign_Compatibility_Dictionary[pluto1][pluto2])
    
    def Overall_Compatibility(sun, moon, mercury, venus, mars, jupiter, saturn, neptune, uranus, pluto):

        # Average score of the signs of all astronomical bodies.

        compatibility = (sun + moon + mercury + venus + mars + jupiter + saturn + neptune + uranus + pluto) / 10

        # Round that number to 2 significant digits.

        rounded = round(compatibility, 2)
        
        print("Your overall compatibility is " + str(rounded) + "%")
        return float(rounded)

    def Romantic_Compatibility(moon, venus, mars):

        # Average score of the astronomical bodies responsible for romantic traits.
        # Moon = emotions.
        # Venus = heart.
        # Mars = passion.

        compatibility = (moon + venus + mars) / 3

        # Round that number to 2 significant digits.

        rounded = round(compatibility, 2)

        print("Your romantic compatibility is " + str(rounded) + "%")
        return float(rounded)

    def Friendship_Compatibility(sun, mercury, saturn):

        # Average score of the astronomical bodies responsible for friendship traits.
        # Sun = personality.
        # Mercury = communication.
        # Saturn = base.

        compatibility = (sun + mercury + saturn) / 3

        # Round that number to 2 significant digits.

        rounded = round(compatibility, 2)

        print("Your friendship compatibility is " + str(rounded) + "%")
        return float(rounded)

    def Business_Compatibility(sun, moon, jupiter):

        # Average score of the astronomical bodies responsible for business traits.
        # Sun = personality.
        # Moon = emotions.
        # Jupiter = prosperity/growth/luck.

        compatibility = (sun + moon + jupiter) / 3

        # Round that number to 2 significant digits.

        rounded = round(compatibility, 2)

        print("Your business compatibility is " + str(rounded) + "%")
        return float(rounded)
    
def main():

    # Ask user for birthdate input.
    
    bday_Month1 = None
    while bday_Month1 is None:
        try:
            bday_Month1 = int(input("Give me your birth month in MM format (1-12): "))
            if not 1 <= bday_Month1 <= 12:
                print("That wasn't in the specified range! Try again in MM format (1-12): ")
                bday_Month1 = None
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 12.")
            bday_Month1 = None

    bday_Day1 = None
    while bday_Day1 is None:
        try:
            bday_Day1 = int(input("Give me the day of that birth month in DD format (1-31): "))
            if not 1 <= bday_Day1 <= 31:
                print("That wasn't in the specified range! Try again in DD format (1-31).")
                bday_Day1 = None
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 31.")
            bday_Day1 = None

    bday_Year1 = None
    while bday_Year1 is None:
        try:
            bday_Year1 = int(input("And now give me the year of your birth in YYYY format, after 1917: "))
            if not 1917 <= bday_Year1 <= 9999:
                print("That's not in the specified range of 1917-9999!")
                bday_Year1 = None
        except ValueError:
            print("Invalid input! Please enter a number betwenn 1917 and 9999.")
            bday_Year1 = None

    bday_Hour1 = None
    while bday_Hour1 is None: 
        try:
            bday_Hour1 = int(input("What hour of the day were you born, in military time? "))
            if not 0 <= bday_Hour1 <= 23:
                print("Try again with the hour in military time.")
                bday_Hour1 = None
        except ValueError:
            print("Invalid input! Try again with the hour in military time, from 0-23.")
            bday_Hour1 = None

    bday_Minute1 = None
    while bday_Minute1 is None:
        try:
            bday_Minute1 = int(input("Now what minute of the hour were you born? "))
            if not 0 <= bday_Minute1 <= 59:
                print("Try again with the minute of the hour you were born, between 0-59.")
                bday_Minute1 = None
        except ValueError:
            print("Invalid input! Enter a minute number between 0-59.")
            bday_Minute1 = None

    # Convert inputs to birthdate string.

    birthdate1 = "{}/{}/{} {:02d}:{:02d}".format(bday_Month1, bday_Day1, bday_Year1, bday_Hour1, bday_Minute1)

    print("\n")
    
    # Create a Zodiac object with the user's birthdate.

    zodiac1 = Zodiac(birthdate1)

    # Get the signs their sun, moon, and planets were in on that birthdate.

    Sun1 = str(zodiac1.sun_sign())
    Moon1 = str(zodiac1.moon_sign())
    Mercury1 = str(zodiac1.mercury_sign())
    Venus1 = str(zodiac1.venus_sign())
    Mars1 = str(zodiac1.mars_sign())
    Jupiter1 = str(zodiac1.jupiter_sign())
    Saturn1 = str(zodiac1.saturn_sign())
    Uranus1 = str(zodiac1.uranus_sign())
    Neptune1 = str(zodiac1.neptune_sign())
    Pluto1 = str(zodiac1.pluto_sign())
    
    print("\n")

    # Do it all over again for the second person.

    bday_Month2 = None
    while bday_Month2 is None:
        try:
            bday_Month2 = int(input("Now give me your birth month in MM format (1-12), person 2: "))
            if not 1 <= bday_Month2 <= 12:
                print("That wasn't in the specified range! Try again in MM format (1-12): ")
                bday_Month2 = None
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 12.")
            bday_Month2 = None

    bday_Day2 = None
    while bday_Day2 is None:
        try:
            bday_Day2 = int(input("Give me the day of that birth month in DD format (1-31): "))
            if not 1 <= bday_Day2 <= 31:
                print("That wasn't in the specified range! Try again in DD format (1-31).")
                bday_Day2 = None
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 31.")
            bday_Day2 = None

    bday_Year2 = None
    while bday_Year2 is None:
        try:
            bday_Year2 = int(input("And now give me the year of your birth in YYYY format, after 1917: "))
            if not 1917 <= bday_Year2 <= 9999:
                print("That's not in the specified range of 1917 -9999!")
                bday_Year2 = None
        except ValueError:
            print("Invalid input! Please enter a number betwenn 1917 and 9999.")
            bday_Year2 = None

    bday_Hour2 = None
    while bday_Hour2 is None: 
        try:
            bday_Hour2 = int(input("What hour of the day were you born, in military time? "))
            if not 0 <= bday_Hour2 <= 23:
                print("Try again with the hour in military time.")
                bday_Hour2 = None
        except ValueError:
            print("Invalid input! Try again with the hour in military time, from 0-23.")
            bday_Hour2 = None

    bday_Minute2 = None
    while bday_Minute2 is None:
        try:
            bday_Minute2 = int(input("Now what minute of the hour were you born? "))
            if not 0 <= bday_Minute2 <= 59:
                print("Try again with the minute of the hour you were born, between 0-59.")
                bday_Minute2 = None
        except ValueError:
            print("Invalid input! Enter a minute number between 0-59.")
            bday_Minute2 = None

    birthdate2 = "{}/{}/{} {:02d}:{:02d}".format(bday_Month2, bday_Day2, bday_Year2, bday_Hour2, bday_Minute2)

    print("\n")

    zodiac2 = Zodiac(birthdate2)

    Sun2 = str(zodiac2.sun_sign())
    Moon2 = str(zodiac2.moon_sign())
    Mercury2 = str(zodiac2.mercury_sign())
    Venus2 = str(zodiac2.venus_sign())
    Mars2 = str(zodiac2.mars_sign())
    Jupiter2 = str(zodiac2.jupiter_sign())
    Saturn2 = str(zodiac2.saturn_sign())
    Uranus2 = str(zodiac2.uranus_sign())
    Neptune2 = str(zodiac2.neptune_sign())
    Pluto2 = str(zodiac2.pluto_sign())
    
    print("\n")

    # Now we show them their slate of compatibility.

    sun_compatibility = Compatibility.sun_compatibility(Sun1, Sun2)
    moon_compatibility = Compatibility.moon_compatibility(Moon1, Moon2)
    mercury_compatibility = Compatibility.mercury_compatibility(Mercury1, Mercury2)
    venus_compatibility = Compatibility.venus_compatibility(Venus1, Venus2)
    mars_compatibility = Compatibility.mars_compatibility(Mars1, Mars2)
    jupiter_compatibility = Compatibility.jupiter_compatibility(Jupiter1, Jupiter2)
    saturn_compatibility = Compatibility.saturn_compatibility(Saturn1, Saturn2)
    uranus_compatibility = Compatibility.uranus_compatibility(Uranus1, Uranus2)
    neptune_compatibility = Compatibility.neptune_compatibility(Neptune1, Neptune2)
    pluto_compatibility = Compatibility.pluto_compatibility(Pluto1, Pluto2)

    print("\n")

    # And now we tell them their compatibilities in life's major arenas.

    romantic = Compatibility.Romantic_Compatibility(moon_compatibility, venus_compatibility, mars_compatibility)
    friendship = Compatibility.Friendship_Compatibility(sun_compatibility, mercury_compatibility, saturn_compatibility)
    business = Compatibility.Business_Compatibility(sun_compatibility, moon_compatibility, jupiter_compatibility)
    overall = Compatibility.Overall_Compatibility(sun_compatibility, moon_compatibility, mercury_compatibility, venus_compatibility, 
    mars_compatibility, jupiter_compatibility, saturn_compatibility, uranus_compatibility, neptune_compatibility, pluto_compatibility)

if __name__ == "__main__":
    main()
