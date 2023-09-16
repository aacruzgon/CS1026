from Flight import *
from Airport import *

class Aviation:
    def __init__(self):
        self._allAirports = {}
        self._allCountries = {}
        self._allFlights = {}

    def getAllAirports(self):
        return self._allAirports
    
    def getAllFlights(self):
        return self._allFlights
    
    def getAllCountries(self):
        return self._allCountries
    
    def setAllAirports(self, airports):
        self._allAirports = airports

    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries

    def loadData(self,airportFile,flightFile,countriesFile):
        # Cleaning dictionaries by default to avoid duplicated data if loadData() function is called more than once during a test
        self._allCountries.clear()
        self._allAirports.clear()
        self._allFlights.clear()
        try:
            with open(countriesFile,"r",encoding='utf8') as file:
                for line in file:      
                    countriesInfo = line.split(",")
                    infoParts = []
                    # formats the file information
                    for info in countriesInfo:
                        infoPart = " ".join(info.split())
                        infoParts.append(infoPart)
                    finalPart = ",".join(infoParts)
                    countriesInfo = finalPart.split(",")
                    #appends countries information to the allCountries dictionary
                    country = countriesInfo[0]
                    continent = countriesInfo[1]
                    self._allCountries[country] = continent                
            
            with open(airportFile,"r",encoding='utf8') as file:
                for line in file:
                    airportInfo = line.split(",")
                    infoParts = []
                    # formats the file information
                    for info in airportInfo:
                        infoPart = " ".join(info.split())
                        infoParts.append(infoPart)
                    airportCode = infoParts[0]
                    airportCity = infoParts[2]
                    airportCountry = infoParts[1]
                    airportContinent = self._allCountries[airportCountry]
                    #creates airport object
                    airportObj = Airport(airportCode,airportCity,airportCountry,airportContinent)
                    self._allAirports[airportCode] = airportObj                  

            with open(flightFile, "r", encoding = 'utf8') as file:
                for line in file:
                    flightInfo = line.split(",")
                    infoParts = []
                    # formats the file information
                    for info in flightInfo:
                        infoPart = " ".join(info.split())
                        infoParts.append(infoPart)
                    noFlight = infoParts[0]
                    origAirCode = infoParts[1]
                    destAirCode = infoParts[2]
                    origObject = self._allAirports[origAirCode]
                    destObject = self._allAirports[destAirCode]
                    #creates flight Object
                    flightInfoObject = Flight(noFlight,origObject,destObject)
                    # appends flight information to allFlights dictionary
                    if origAirCode in self._allFlights.keys():
                        self._allFlights[origAirCode] = self._allFlights[origAirCode] + [flightInfoObject]
                    else:
                        self._allFlights[origAirCode] = [flightInfoObject]
            return True
        except:
            return False 

    def getAirportByCode(self,code):
            if code in self._allAirports.keys():
                return self._allAirports[code]
            else:
                return -1
    
    def findAllCityFlights(self,city):
        cities = []
        for flights in self._allFlights.values():
            for code in flights:
                #  checks if the cities match and then appends the cities
                if code.getOrigin().getCity() == city or code.getDestination().getCity() == city:
                    cities.append(code)
        return cities
    
    def findFlightByNo(self,flightNo):
        for flights in self._allFlights.values():
            for flight in flights:
                # checks if flight Number exists 
                if flight.getFlightNumber() == flightNo:
                    return flight
        return -1
    
    def findAllCountryFlights(self,country):
        countriesFlights = []
        for countries in self._allFlights.values():
            for countrys in countries:
                # check if the countries match and appends them in a list
                if countrys.getOrigin().getCountry() == country or countrys.getDestination().getCountry() == country:
                    countriesFlights.append(countrys)
        return countriesFlights
    
    def findFlightBetween(self,origAirport,destAirport):
        directFlight = None
        connectingAirports = set()
        singleHopAirports = set()
        # Cheks for directFlights and connecting flights
        for flights in self._allFlights.get(origAirport.getCode(),[]):
            if flights.getDestination() == destAirport:
                directFlight = flights
                break
            else:
                connectingAirports.add(flights.getDestination().getCode())

        # returns direct flight representation
        if directFlight != None:
            return f"Direct Flight({directFlight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
        
        # checks all the singleHopAirports in connecting Airports and appends them to a set of single hop airports
        for airport_code in connectingAirports:
            for flight in self._allFlights.get(airport_code, []):
                if flight.getDestination() == destAirport:
                    singleHopAirports.add(airport_code)

        if singleHopAirports:
            return singleHopAirports
        # returns -1 if there are no direct flights and no single-hop connecting flights
        return -1
    
    def findReturnFlight(self, firstFlight):
        originationCode = firstFlight.getOrigin().getCode()
        destinationCode = firstFlight.getDestination().getCode()
        # checks if flights happen from destination to the origin flight
        if destinationCode in self._allFlights:
            for flight in self._allFlights[destinationCode]:
                if flight.getDestination().getCode() == originationCode:
                    return flight
        # I still dont understand why return -1 works here, but it doesnt work with an else statement
        return -1
    
    def findFlightsAcross(self,ocean):
        greenZone = ["North America","South America"]
        redZone = ["Asia","Australia"]
        blueZone = ["Africa","Europe"]
        flightCodes = set()
        # finds all flights continent origin and destination
        if ocean == "Atlantic":
            for flights in self._allFlights.values():
                for flight in flights:
                    continentOfOrigin = flight.getOrigin().getContinent()
                    continentOfDest = flight.getDestination().getContinent()
                    if (continentOfOrigin in greenZone and continentOfDest in blueZone) or (continentOfOrigin in blueZone and continentOfDest in greenZone):
                        flightNo = flight.getFlightNumber()
                        flightCodes.add(flightNo)
        elif ocean == "Pacific":
            for flights in self._allFlights.values():
                for flight in flights:
                    continentOfOrigin = flight.getOrigin().getContinent()
                    continentOfDest = flight.getDestination().getContinent()
                    if (continentOfOrigin in greenZone and continentOfDest in redZone) or (continentOfOrigin in redZone and continentOfDest in greenZone):
                        flightNo = flight.getFlightNumber()
                        flightCodes.add(flightNo)
        # checks if the set has no flight codes
        if not(flightCodes):
            return -1 
        
        return flightCodes


    




        






        






   