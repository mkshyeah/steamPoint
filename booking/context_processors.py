from .booking import Booking

def booking(request):
  return {'booking': Booking(request)}