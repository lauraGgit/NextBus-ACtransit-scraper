# NextBus-JSON-scraper
This is a scraper of all the stops on the for a particular agency on the [NextBus API](http://api-portal.anypoint.mulesoft.com/nextbus/api/nextbus-api) converted from multiple XML calls to a single Json.

No API key is needed!

## Running the Code
Run <code>python scraper.py</code> in your command line to generate the agency_stops.txt file.

##Updating the Transit Agency
You can update the agency by changing line 4 of <code>scraper.py</code>
	agency = "actransit"

You can find your transit agency by looking at the tag element on this xml file [http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList]