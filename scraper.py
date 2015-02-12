import urllib2
import xml.etree.ElementTree as ET
import json
routes = urllib2.urlopen("http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=actransit").read()

routes_ET = ET.fromstring(routes)


route_Arr = []
for r in routes_ET:
	route_Arr.append(r.attrib)

#print route_Arr

def shrtDir(nw):
	dirs = {"West": "W", "South": "S", "North": "N", "East": "E", "Kounterc" : "KC", "Clockwis": "CW"}
	if nw in dirs:
		return dirs[nw]
	else:
		return nw


stops = []
for i in xrange(len(route_Arr)):
	stop = urllib2.urlopen("http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=actransit&r="+route_Arr[i]['tag']).read()
	stop_ET = ET.fromstring(stop)
	route_stops = []
	direct = []
	for d in stop_ET.iter('direction'):
		cDir = shrtDir(d.get('name'))
		direct.append({"dir": cDir, "to": d.get('title')}) 
		for st in d:
			#print st.attrib
			for s in stop_ET.iter('stop'):
			# if stop doesn't have attribute lat:
				if 'lat' in s.attrib:
					if s.get('tag') == st.get('tag'):
						#	append direction to where stop['tag'] == stop['tag']with other info
						s.set('dir', cDir)
						route_stops.append(s.attrib)
						#d.remove(st)

	stops.append({"route": {"tag":route_Arr[i]['tag'], "title": route_Arr[i]['title'],"directions": direct, "stops": route_stops}})
	# for s in stop_ET.iter('stop'):
	# 	print s.attrib
stopsJson = json.JSONEncoder(stops)
with open('actransit_stops.txt', 'w') as jsonFile:
    json.dump(stops, jsonFile)
