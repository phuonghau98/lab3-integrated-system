import rpyc
import sys

host = sys.argv[1]
port = sys.argv[2]

conn = rpyc.connect(host, port)

def printMenu():
  print("1. Check available flights")
  print("2. Get full detail of a flight")
  print("3. Book a seat on a flight")
  print("4. Return a ticket")

while True:
  printMenu()
  c = int(input('Enter your choice: '))
  if c == 0:
    break

  if c == 1:
    flights = conn.root.getAvailableFlights()
    print("Available flights:")
    for f in flights:
      print("\t" + f)

  if c == 2:
    flightCode = input("Input a flight you want to view full detail: ")
    result = conn.root.viewFlightDetail(flightCode)
    print(result)

  if c == 3:
    flightCode = input("Input a flight code you want to book a seat: ")
    result = conn.root.bookAseat(flightCode)
    if result:
      print("A seat has been booked successfully on flight {}".format(flightCode))
    else: print("Error: Something went wrong")
  
  if c == 4:
    flightCode = input("Input a flight code of flight of which you want to return ticket: ")
    result = conn.root.returnTicket(flightCode)
    if result:
      print("A seat has been booked successfully on flight {}".format(flightCode))
    else: print("Error: Something went wrong")