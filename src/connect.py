# *****************************************************************************
# *****************************************************************************
#
#		Name:		connect.py
#		Author:		Paul Robson (paul@robsons.org.uk)
#		Date:		30th September 2021
#		Reviewed: 	No
#		Purpose:	Handles connections to VATSIM and data extraction.
#
# *****************************************************************************
# *****************************************************************************

import urllib.request,json

from flight import *
from airports import *

# *****************************************************************************
#
# 							Connection classes
#
# *****************************************************************************

class AbstractConnection:
	def __init__(self):
		self.vatsimData = self.getVatsimData()
	#
	def getVatsimData(self):
		assert False		
	#
	# 		Locate a pilot record by ID
	#
	def find(self,vatsimID):
		for p in self.vatsimData["pilots"]:
			if p["cid"] == vatsimID:
				return p
		return nil

# *****************************************************************************
#
# 			Used for testing, it's a presaved dump of the Vatsim text
#
# *****************************************************************************

class TestConnection(AbstractConnection):		
	def getVatsimData(self):
		txt = open("../misc/vatsim.txt").read(-1)
		vatSimData = json.loads(txt)
#		for p in self.vatSimData["pilots"]:
#			print(p["cid"],p["name"])
		return vatSimData

# *****************************************************************************
#
# 						Acquire Vatsim live data from server.
#
# *****************************************************************************

class LiveConnection(AbstractConnection):
	def getVatsimData(self):
		with urllib.request.urlopen("https://data.vatsim.net/v3/vatsim-data.json") as url:
			return json.loads(url.read().decode())

if __name__ == "__main__":
	prec = LiveConnection().find(1438978)
	db = AirportDatabase()
	fl = Flight(prec)
	print(fl.getVatsimID())
	print(fl.getName())	
	print(fl.getCallSign())		
	print(fl.getSpeed())
	print(fl.getTime())
	print(fl.getPosition())
	airport = db.find(fl.getPosition())
	print(airport)
	print(airport.getDistance(fl.getPosition()))
	print("--------------")