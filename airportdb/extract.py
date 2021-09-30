# *****************************************************************************
# *****************************************************************************
#
#		Name:		extract.py
#		Author:		Paul Robson (paul@robsons.org.uk)
#		Date:		30th September 2021
#		Reviewed: 	No
#		Purpose:	Extract airport data to a better format from
#  					GlobalAirportDatabase.txt
#
# *****************************************************************************
# *****************************************************************************

import sys
#
# 		Anything beginning with these we want. Empty string is everything, for testing
#		purposes.
#
masks = [ "NZ","EG",""]
airportList = []
#
# 		Extract information from the GAD txt file, we want the ICAO, Name, Country and Position.
#
for airport in [x.strip().lower() for x in open("GlobalAirportDatabase.txt").readlines() if x.strip() != ""]:
	air = airport.split(":")
	#
	#	Get basic information
	#
	icao = air[0].upper()
	name = air[3] if air[2] == "N/A" else air[2]
	country = air[4]
	latitude = float(air[14])
	longitude = float(air[15])
	#
	#	Some airports are in the database, but have no position, they have lat & long 0.00 
	#	if any of these are required we will have to add them manually
	#
	if latitude != 0.0 or longitude != 0.0:
		passed = False
		for m in masks:
			passed = passed or icao.startswith(m)
		if passed:
			info = ":".join([icao.upper(),name.title(),country.title(),str(latitude),str(longitude)])
			airportList.append(info)
#
# 		Generate Python class
#
h = open("airportdb.py","w")
h.write("#\n#\tThis is automatically generated.\n#\n")		
h.write("class AirportRawDatabase:\n")
h.write("\tdef get(self):\n")
h.write("\t\ts = \"\"\"\n")
for l in airportList:
	h.write("\t\t\t|{0}\n".format(l))
h.write("\t\t\"\"\".strip().split(\"|\")\n")
h.write("\t\treturn [x.strip() for x in s if x.strip() != \"\"]\n")
