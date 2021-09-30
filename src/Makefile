ifeq ($(OS),Windows_NT)
include ..\documents\common.make
else
include ../documents/common.make
endif

all: cixlogger.pyz

run: cixlogger.pyz 	
	python cixlogger.pyz 1505974

cixlogger.pyz: airports.py connect.py __main__.py flight.py airportdb.py
	rm cixlogger.pyz
	make -C ..$(S)airportdb
	zip cixlogger.pyz *.py
	$(CCOPY) cixlogger.pyz ..