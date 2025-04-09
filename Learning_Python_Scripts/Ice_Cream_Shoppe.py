# File which will implement the IceCreamShoppe class
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by (John Gill)
# 25 March 2023
# CS 5001

import math

class Scoop:

    '''Class Scoop
       Attributes: radius
       Methods: volume'''
    
    #JG - This class will be used by the 'IceCreamShoppe' class to operate on the 'Carton' class as we remove ice cream from it. 
    
    def __init__(self, radius):

        '''
        Constructor - creates a new instance of Scoop
        Parameters -
           self - the current object
           radius - the radius of the scoop
        '''

        #JG - This constructor creates the characteristic of 'radius' to apply to scoop.

        self.radius = radius
        
    def volume(self):

        ''' Method - calculate the volume of the scoop
        Parameters:
           self - the current object
        '''

        #JG - This method applies the equation for the volume of a sphere to the scoop object's radius.

        return (self.radius ** 3) * (4 / 3) * (math.pi)
    
    def scoopstring(self):

        #JG - This method returns a nice and shiny, polished term to identify the scoop in question when printing it out.

        return f"{self.radius}-radius"
        
class Carton:

    ''' Class: Carton
        Attributes: contains
        Methods: hasEnoughFor, remove'''
    
    #JG - This 'IceCreamShoppe' class will use the 'Scoop' class to operate on this class as we remove ice cream from the carton. 
    
    def __init__(self, radius, height):

        ''' Constructor
            Parameters:
                self
                radius - radius of a carton
                height - height of a carton'''
        
        #JG - This constructor applies 'radius' and 'height' characteristics to the 'Carton' class.
        
        self.volume = ((radius ** 2) * (math.pi) * height)
        
    def hasEnoughFor(self, scoop:Scoop):

        ''' hasEnoughFor
            Parameters:
                scoop - the Scoop to be used on the Carton
            Return:
                whether or not the Carton contains enough to make a Scoop'''
        
        #JG - This method determines if the volume in the scoop is greater than the remaining volume of ice cream in the current carton. 
        #     Used in the 'serve' method of 'IceCreamShoppe.'
        
        scoop_volume = scoop.volume()
        if scoop_volume <= self.volume:
            return True
        else: 
            return False
        
    def remove(self, scoop:Scoop):

        ''' remove
            Parameters:
                scoop - the Scoop to be used on the Carton
        '''
        #JG - This method works by subtracting the volume of the scoop from the volume of the remaining ice cream in the 'Carton' object. 

        scoop_volume = scoop.volume()
        self.volume -= scoop_volume
        
class IceCreamShoppe:

    '''Class IceCreamShoppe
        Attributes: carton_radius, carton_height, cartons_used
        Methods: serve, cartonsUsed'''
    
    #JG - This class seeks to use the 'Scoop' class to operate on the 'Carton' class. It effectively uses a digital scooper to take digital ice cream out of a digital carton. 

    def __init__(self, carton_radius, carton_height):

        ''' Constructor
        Parameters: carton_radius, carton_height - dimensions for a carton
        Return: nothing'''

        #JG - This constructor calls upon the 'Carton' class to turn it into an object for this class, then keeps track of its ice cream contents as 'Scoop' operates on it.

        self.carton_radius = carton_radius
        self.carton_height = carton_height
        self.cartons_used = 1
        self.current_carton = Carton(self.carton_radius, self.carton_height)
        
    def serve(self, numScoops, scooper:Scoop):

        ''' serve method
        Parameters: numScoops - number of scoops wanted; 
            scooper - the specific Scoop to use
        Return: nothing'''

        #JG - This method spans the number of scoops given to 'IceCreamShoppe', and determines whether to add another carton to the carton list, based
        #     on the returned boolean value of the 'hasEnoughFor' method for each scoop. 

        for i in range(numScoops):   
            if not self.current_carton.hasEnoughFor(scooper):
                self.cartons_used += 1
                self.current_carton = Carton(self.carton_radius, self.carton_height)
            self.current_carton.remove(Scoop(scooper.radius))
        
    def cartonsUsed(self):

        #JG - This method tells python what the current number of used cartons is, and will only be called upon when the user is done with the program. 

        ''' cartonsUsed method
        Parameters: none
        Return: the number of cartons used so far in the Shoppe'''
        return self.cartons_used
        
        
def main():

    #JG - Here we are, the main function. After setting up the meat of this program in the classes, we are now at the face.
    #     I'm going to provide a one-time, step-by-step walkthrough of this main's processing from beginning to end, right here. 
    #     It starts by introducing itself and asking the user for the size scoopers they'd like to get ice cream with.
    #     Then, after getting the scooper sizes, it creates a Scoop object with those scoopers' dimensions.
    #     Then it asks the size of the carton they'd like to pull from, and asks them if they'd like ice cream. 
    #     If the user gives the program an inappropriate response, the program lets them know until they get it right.
    #     Then we create a shoppe variable that enacts the 'IceCreamShoppe' class with the carton's dimensions for further use.
    #     Then we enter a while loop that asks how many of each size scoop they'd like, and scoops those scoops out of the carton so long as they keep asking.
    #     Then, when they're all done getting ice cream, this program tells them how much ice cream they've attained. We do not know what they will do with it.

    print("Hello! Welcome to the Ice Cream Shoppe. Today I will be serving you ice cream. I'll ask you how many scoops you want,", "\n"
          "and you'll tell me. By the end of this, I'll tell you how many cartons of ice cream you've consumed.")
    first = int(input("What is the radius of the first scooper you'd like us to scoop your ice cream with? "))
    first_scooper = Scoop(first)

    second = int(input("And what is the radius of the second scooper? "))
    second_scooper = Scoop(second)

    carton_radius = int(input("And what is the radius of your ice cream carton? "))
    carton_height = int(input("What is the height of your ice cream carton? "))

    more = int(input("Would you like ice cream? Enter 1 for yes and enter 0 for no: "))

    while more != 1 and more != 0:
        more = int(input("Oops! Looks like you input something other than 1 or 0. Try again, 1 for yes, 0 for no: "))
    
    shoppe = IceCreamShoppe(carton_radius, carton_height)

    while more == 1:

        firstScoopNum = int(input(f"How many {first_scooper.scoopstring()} scoops would you like? "))
        
        shoppe.serve(firstScoopNum, first_scooper)
        
        secondScoopNum = int(input(f"How many {second_scooper.scoopstring} scoops would you like? "))

        shoppe.serve(secondScoopNum, second_scooper)

        more = int(input("Would you like more ice cream? Press 1 for yes, and 0 for no: "))

    print("You have used", shoppe.cartonsUsed(), "cartons of ice cream.")

main()
