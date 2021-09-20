# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:30:35 2019

@author: farjana
"""
#Project 1
#Unit conversion from Rod (distance)
#Prompt for a floating points
#convert rod(distance) to other standard units
#Input integer
#Convert rods to the following distance units
#Round all the floating to 3 decimal places

n_float = float(input ("Input rods: ")) #Prompt for a floating points
print("You input", n_float, "rods.") #Input integer

print()
print("Conversions")  #convert rods

Meters = (n_float) * 5.0292  # rod = 5.0292 meters
Feet = (Meters)/0.3048    # Foot = 0.3048 meters
Miles = (Meters)/1609.34  # one Mile = 1609.34 meters
Furlongs = (n_float)/40   # one Furlong = 40 rods
Minutes = (Miles/3.1)*60  # one hour = 60 minutes, 3.1 miles per 60 minutes

#Print the following:
print("Meters:", round(Meters, 3))
print("Feet:", round(Feet, 3))
print("Miles:", round(Miles, 3))
print("Furlongs:", round(Furlongs, 3))
print("Minutes to walk", n_float, "rods:", round(Minutes, 3))

