import urllib.request, json 
with urllib.request.urlopen("https://data.vatsim.net/v3/vatsim-data.json") as url:
    data = json.loads(url.read().decode())
    print(data["pilots"][0])
    open("vatsim.txt","w").write(json.dumps(data))

#
#   Sterling Paulsen is immortalised by being my test data.
#
# {'cid': 1238470, 'name': 'Sterling Paulsen KHOU', 'callsign': 'JAS713', 'server': 'USA-EAST', 
#  'pilot_rating': 3, 'latitude': 36.82819, 'longitude': -6.0193, 'altitude': 1660, 
#  'groundspeed': 173, 'transponder': '2200', 'heading': 198, 'qnh_i_hg': 30.18, 
# 'qnh_mb': 1022, 'flight_plan': {'flight_rules': 'I', 'aircraft': 'B738/?-VGDW/C', 
#  'aircraft_faa': 'B738/L', 'aircraft_short': 'B738', 'departure': 'LGSA', 
#  'arrival': 'LEJR', 'alternate': 'LEMG', 'cruise_tas': '470', 'altitude': '38000', 
# 'deptime': '0410', 'enroute_time': '0415', 'fuel_time': '0711', 
# 'remarks': 'REG/N713TX OPR/JAS CALL/JETSETTER /V/ SEL/JPDH', 
# 'route': 'PLH1T PLH M978 TUC UM978 MORJA UA411 MOS UM744 MGA MGA2U', 'revision_id': 7, 
# 'assigned_transponder': '0000'}, 'logon_time': '2021-09-29T20:11:58.3590897Z', 
# 'last_updated': '2021-09-30T07:53:47.2506606Z'}    