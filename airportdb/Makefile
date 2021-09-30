ifeq ($(OS),Windows_NT)
include ..\documents\common.make
else
include ../documents/common.make
endif

all: airportdb.py

airportdb.py : GlobalAirportDatabase.txt extract.py
	python extract.py
	python test.py
	$(CCOPY) airportdb.py ..$(S)src	


