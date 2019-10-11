from rpyc import ThreadedServer, Service
from flight import Flight
from datetime import datetime, timedelta
import sys

port = int(sys.argv[1])

class FlightService(Service):
  def __init__(self):
    flight1 = Flight('VNA360', 'Vietnam', 'Netherlands', 100, datetime(2019, 12, 30, 11, 45), timedelta(hours=12, minutes=30))
    flight2 = Flight('VJ974', 'VietNam', 'USA', 100, datetime(2019, 9, 30, 16, 15), timedelta(hours=18, minutes=15))
    flight3 = Flight('VJ332', 'VietNam', 'NewZealand', 100, datetime(2019, 1, 24, 4, 35), timedelta(hours=5, minutes=40))
    self.flights = [flight1, flight2, flight3]

  def getFlight(self, flightCode):
    for f in self.flights:
      if f.code == flightCode:
        return f
  
  def exposed_getAvailableFlights(self):
    return [flight.code for flight in self.flights]
  
  def exposed_bookAseat(self, flightCode):
    if flightCode in self.exposed_getAvailableFlights():
      foundFlight = self.getFlight(flightCode)
      foundFlight.bookASeat()
      return True
    return False
  
  def exposed_returnTicket(self, flightCode):
    if flightCode in self.exposed_getAvailableFlights():
      foundFlight = self.getFlight(flightCode)
      foundFlight.returnTicket()
      return True
    return False
  
  def exposed_viewFlightDetail(self, flightCode):
    if flightCode in self.exposed_getAvailableFlights():
      foundFlight = self.getFlight(flightCode)
      return foundFlight.viewDetail()
    return "There is no such flight"

if __name__ == '__main__':
  t = ThreadedServer(FlightService, port=port)
  t.start()