from airportdb import *
d = AirportRawDatabase().get()
print("Number of airports selected",len(d))