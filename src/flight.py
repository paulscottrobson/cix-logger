# *****************************************************************************
# *****************************************************************************
#
#		Name:		flight.py
#		Author:		Paul Robson (paul@robsons.org.uk)
#		Date:		30th September 2021
#		Reviewed: 	No
#		Purpose:	Represents a single flight.
#
# *****************************************************************************
# *****************************************************************************

from airports import *

# *****************************************************************************
#
#								Flight class
#
# *****************************************************************************

class Flight:
	def __init__(self,jsonData):
		self.data = jsonData
		self.months = "/Jan/Feb/Mar/Apr/May/Jun/Jul/Aug/Sep/Oct/Nov/Dec".split("/")
	#
	# 		Accessors
	#
	def getVatsimID(self):
		return self.data["cid"]
	def getName(self):
		return self.data["name"]
	def getCallSign(self):
		return self.data["callsign"]
	def getSpeed(self):
		return self.data["groundspeed"]
	def getPosition(self):
		return [self.data["latitude"],self.data["longitude"]]

	#
	# 		Get Zulu time in a nicer format. This is the time of the data in the server
	#
	def getTime(self):
		raw = self.data["last_updated"]
		return raw[11:19]+"Z "+raw[8:10]+" "+self.months[int(raw[5:7])]
	#
	#  		Get the information string returned to the user.
	#
	def getInformationString(self,airportID):
		name = self.getName().upper().replace(".","").replace(" ","")
		time = self.data["last_updated"][5:20].replace("-","").replace(":","").replace("T",".")
		fmt = "{0}.{1}.{2}.{3}".format(self.getVatsimID(),name,airportID.upper(),time)
		return fmt+self.calculateChecksum(fmt.replace(".",""))
	#
	# 		Simple checksum calculator
	#
	def calculateChecksum(self,s):
		checkSum = 0
		for i in range(0,len(s)):
			checkSum = checkSum + ord(s[i]) * (i + 1) 
		return str(checkSum % 1000)

########'2021-09-30T07:53:47.2506606Z'		
if __name__ == "__main__":
	db = AirportDatabase()
	testData = {'cid': 1238470, 'name': 'Sterling Paulsen KHOU', 'callsign': 'JAS713', 'server': 'USA-EAST', 'pilot_rating': 3, 'latitude': 36.82819, 'longitude': -6.0193, 'altitude': 1660, 'groundspeed': 173, 'transponder': '2200', 'heading': 198, 'qnh_i_hg': 30.18, 'qnh_mb': 1022, 'flight_plan': {'flight_rules': 'I', 'aircraft': 'B738/?-VGDW/C', 'aircraft_faa': 'B738/L', 'aircraft_short': 'B738', 'departure': 'LGSA', 'arrival': 'LEJR', 'alternate': 'LEMG', 'cruise_tas': '470', 'altitude': '38000', 'deptime': '0410', 'enroute_time': '0415', 'fuel_time': '0711', 'remarks': 'REG/N713TX OPR/JAS CALL/JETSETTER /V/ SEL/JPDH', 'route': 'PLH1T PLH M978 TUC UM978 MORJA UA411 MOS UM744 MGA MGA2U', 'revision_id': 7, 'assigned_transponder': '0000'}, 'logon_time': '2021-09-29T20:11:58.3590897Z', 'last_updated': '2021-09-30T07:53:47.2506606Z'}    
	fl = Flight(testData)
	print(fl.getInformationString("EGSV"))
	print(fl.getVatsimID())
	print(fl.getName())	
	print(fl.getCallSign())		
	print(fl.getSpeed())
	print(fl.getTime())
	print(fl.getPosition())
	airport = db.find(fl.getPosition())
	print(airport)
	print(airport.getDistance(fl.getPosition()))