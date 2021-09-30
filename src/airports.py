# *****************************************************************************
# *****************************************************************************
#
#		Name:		airports.py
#		Author:		Paul Robson (paul@robsons.org.uk)
#		Date:		30th September 2021
#		Reviewed: 	No
#		Purpose:	Wrapper class and support functions for airport database
#
# *****************************************************************************
# *****************************************************************************

from airportdb import *
from math import sin, cos, sqrt, atan2, radians

# *****************************************************************************
#
#									Airport Class
#
# *****************************************************************************

class Airport:
	def __init__(self,dataString):
		self.info = dataString.split(":")
		self.latitude = float(self.info[3])
		self.longitude = float(self.info[4])
	#
	# 		Simple accessors
	#
	def getIcao(self):
		return self.info[0]
	def getName(self):
		return self.info[1]
	def getCountry(self):
		return self.info[2]
	def getLatitude(self):
		return self.latitude
	def getLongitude(self):
		return self.longitude
	#
	# 		Convert to string
	#
	def __str__(self):
		return "{0},{1} [{2}] ({3},{4})".format(self.getName(),self.getCountry(),
								self.getIcao(),self.getLatitude(),self.getLongitude())
	#
	# 		Get distance between airport and a position, in kilometres.
	# 		(borrowed from Michael0x2A). This is an approximation, good enough for
	#		our purposes. 
	#
	def getDistance(self,location):

		R = 6373.0
		lat1 = radians(location[0])
		lon1 = radians(location[1])
		lat2 = radians(self.getLatitude())
		lon2 = radians(self.getLongitude())

		dlon = lon2 - lon1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		return R * c

# *****************************************************************************
#
#								  Airport Collection
#
# *****************************************************************************

class AirportDatabase:
	def __init__(self):
		self.airports = {}
		for ad in AirportRawDatabase().get():
			ap = Airport(ad)
			assert ap.getIcao() not in self.airports,"Duplicate ICAO"
			self.airports[ap.getIcao()] = ap
	#
	#		Accessors
	#
	def getAirportIcaoList(self):
		return [x for x in self.airports.keys()]
	def getAirport(self,icao):
		icao = icao.strip().upper()
		return self.airports[icao] if icao in self.airports else None
	#
	# 		Find the nearest airport, calculated simply as the sum of the differences.
	#		If you want the actual distance use Airport.getDistance()
	#	 	The quick search should be good enough if you aren't a ridiculous distance away.
	#
	def find(self,location):
		bestDistance = 99999.0
		airport = None
		for a in self.airports.values():
			dist = abs(location[0]-a.getLatitude())+abs(location[1]-a.getLongitude())
			if dist < bestDistance:
				airport = a
				bestDistance = dist
		return airport

if __name__ == "__main__":
	db = AirportDatabase()
	print(db.getAirportIcaoList())

	print(db.getAirport("EGKK"))
	search = [51.14,-0.19]   						# Gatwick position
	ap = db.find(search)
	print(ap)
	print(ap.getDistance(search))

	heathrow = db.getAirport("EGLL")
	print(heathrow.getDistance(search))				# Heathrow -> Gatwick
													# Which is about 41km.
