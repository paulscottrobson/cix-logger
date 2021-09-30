# *****************************************************************************
# *****************************************************************************
#
#		Name:		__main__.py
#		Author:		Paul Robson (paul@robsons.org.uk)
#		Date:		30th September 2021
#		Reviewed: 	No
#		Purpose:	Main Program
#
# *****************************************************************************
# *****************************************************************************

import sys

from flight import *
from airports import *
from connect import *



if len(sys.argv) != 2:
	print("Please supply the VATSIM ID of the aviator e.g. python cixlogger.pyz 142307")
	sys.exit(0)
#
# 		Connect to VATSIM and access the flight information, create a flight object with it.
#
flight = Flight(LiveConnection().find(int(sys.argv[1])))
if flight is None:
	print("\tI cannot find Vatsim ID "+sys.argv[1])
	sys.exit(0)

#
# 		Find out where the aircraft is nearest to, how fast it is travelling
#
speed = flight.getSpeed()
airport = AirportDatabase().find(flight.getPosition())
distance = airport.getDistance(flight.getPosition())

print("*** VATSIM Logger v0.0 (30-09-21) ***\n")

print("\tYou are         : {0}".format(flight.getName()))
print("\tNearest airport : {0} ({1})".format(airport.getName(),airport.getCountry()))
print("\tDistance (km)   : {0}".format(int(distance)))
print("\tSpeed (km/h)    : {0}".format(speed))
print("")

reject = False 
if distance > 2:
	print("\t\tYou are too far from the airport")
	reject = True
if speed > 10:
	print("\t\tYou are not stationary")
	reject = True 

if not reject:
	print("You are stationary at the airport.\nPlease contact * sending the text below:")
	print("\t{0}".format(flight.getInformationString(airport.getIcao())))



