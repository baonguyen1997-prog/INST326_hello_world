''' Developing a module conatining a car class. Instance of the class will be able to turn and drive forward.

Driver: Bao Nguyen
Navigator:  Chaerim Lee
Assignment: INST 326 Exercise-2
Date: 10/08/22
Challenges Encountered: 

The most challenging part was the sanity_check() function
'''

from math import cos, radians, sin
from operator import mod
import sys



class Car():
    """ this class with make the car turn and drive forward

    Definitions:
        x (float): x coordinate of the car
        y (float): y coordinate of the car
        heading(float): the starting heading
        turn(float): assign value to the heading attribute
        drive(float): updates x and y attributes

        
    """
   
   
    def __init__(self, x=0, y=0, heading=0):
        """Initialize three values of car class.

        Args:
            x (int, optional): the initial x coordinate. Defaults to 0.
            y (int, optional): the initial y coordinate. Defaults to 0.
            heading (int, optional): the initial heading coordinate. Defaults to 0.
        """
        self.x = x
        self.y = y
        self.heading = heading

    
    
    def turn(self, degrees):
        """this method takes two required parameters and assign a new value to heading values.

        Args:
            degrees (Float): a positive number of degree indicates a clockwise turn and a negative
                number of degree indicates counterclockwise turn.

        Side effects: 
            changes the value of heading attribute.
        """
        #Assign a new value to the heading attribute
        self.heading =((self.heading + degrees) % 360)

    
    
    
    def drive(self, d):
        """Updates current value of attributes x and y

        Args:
            d (float): distance

        Side effects:
            changes the value of x and y attribute.
        """
        self.x += d*(sin(radians(self.heading)))
        self.y -= d*(cos(radians(self.heading)))



def sanity_check():
    """Generates location and heading.

    Returns:
        float: the location of the car

    Side effects:
        Display the location and heading.
    """
    #instance of the car
    location = Car()
    
    location.turn(90)
    location.drive(10)
    location.turn(30)
    location.drive(20)

    #print location and heading
    print("Location: ", location.x, ", ", location.y)
    print("Heading: ", location.heading)

    return location
   

    
if __name__ == "__main__":
    """invokes sanity_check function.
    """
    sanity_check()
    


