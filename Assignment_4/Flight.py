from Airport import *

class Flight:

    def __init__(self, flightNo, origAirport, destAirport):
        if not ((isinstance(origAirport,Airport)) and (isinstance(destAirport, Airport))):
            raise TypeError ("The origin and destination must be Airport objects")
        if not ((isinstance(flightNo, str)) and (len(flightNo) == 6) and (flightNo[:3].isalpha()) and (flightNo[3:].isdigit())):
            raise TypeError ("The flight number format is incorrect")
        # non public instances attributes
        self._flightNo = flightNo
        self._origAirport = origAirport
        self._destAirport = destAirport

    def __repr__(self):
        if self.isDomesticFlight():
            flightType = "domestic"
        else:
            flightType = "international"
        return f'Flight({self._flightNo}): {self._origAirport.getCity()} -> {self._destAirport.getCity()} [{flightType}]'
 
    def __eq__(self, other):
        if isinstance(other, Flight):
            return self._origAirport == other._origAirport and self._destAirport == other._destAirport
        return False 

    def getFlightNumber(self):
        return self._flightNo
    
    def getOrigin(self):
        return self._origAirport
    
    def getDestination(self):
        return self._destAirport
    
    def isDomesticFlight(self):
        return self._origAirport.getCountry() == self._destAirport.getCountry()
                        
    def setOrigin(self,origin):
        self._origAirport = origin

    def setDestination(self,destination):
        self._destAirport = destination
    
    

    
   


      