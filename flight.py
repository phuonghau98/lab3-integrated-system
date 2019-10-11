from datetime import datetime, timedelta

class Flight:
  def __init__(self, code, departure, arrival, seatTotal, boardingTime, estTime):
    self._code = code
    self._departure = departure
    self._arrival = arrival
    self._seatTotal = seatTotal
    self._seatSold = 0
    self._boardingTime = boardingTime
    self._estTime = estTime
  
  @property
  def availableSeat(self):
    return self._seatTotal - self._seatSold

  @property
  def code(self):
    return self._code

  def viewDetail(self):
    return 'Flight: {} | Departure: {} | Arrival: {} | Boarding Time: {} | Seat total: {} | Available seat: {} \
      '.format(self._code, self._departure, self._arrival, self._boardingTime, self._seatTotal, self.availableSeat)

  def bookASeat(self):
    if self.availableSeat > 0:
      self._seatSold += 1
      return True
    return False

  def returnTicket(self):
    if self._seatSold > 0:
      self._seatSold -= 1
      return True
    return False
