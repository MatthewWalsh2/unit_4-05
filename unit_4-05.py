# created by Matthew Walsh
# created for ICS3U
# created on nov 2017
# calculate volume of cylinder

import math
 
radius = raw_input('Enter the radius: ')
radius = int(radius)

height = raw_input('Enter the height: ')
height = int(height)

def volume(radius, height):
    #calculate volume
    volume_of_cylinder = 2 * math.pi * (radius * radius) * float(height)
    return volume_of_cylinder
    
try:
    print('The volume of the cylinder is: ' + str(round(volume(radius, height), 3)))
    
except:
    print('Please input your number')
