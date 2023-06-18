# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:39:42 2023

@author: Robert Kus
"""

"""
    Calculating the magnitude, angle, and acceleration of two Tension 
    forces at different angles
"""


""" Import the math module to use math equations like power and trig equations"""
import math

"""
Step 1: Collect user inputs and validating for errors.
           If a user enters an invalid input, they will need to enter 
           their values again until they are valid to get the final output.
"""

while True:
    try:
        force1 = int(input("What is the value of the left-most/F1 (in N)? "))
        angle1 = int(input("At what angle is F1 from the x axis? "))
        force2 = int(input("What is the value of the Right-most/F2 (in N)? "))
        angle2 = int(input("At what angle is F2 from the x axis? "))
        mass = int(input("What is the mass of the object (in kg)? " ))
    except ValueError:
        print("Sorry, I didn't get that...")
        continue
    else:
        break

"""Step 2: Perform remaining calculations needed to produce final output"""

tensionX = force1 * math.cos(math.radians(angle1)) + force2 * math.cos(math.radians(angle2))
tensionY = force1 * math.sin(math.radians(angle1)) - force2 * math.sin(math.radians(angle2))

magnitude = (tensionX**2 + tensionY**2)**0.5
acceleration = magnitude/mass

"""Step 3: Produce final output statement"""

print("\nTension Magnitude: " + str(magnitude) + " N")
print("\nAcceleration of object: " + str(acceleration) + " m/s*2")
