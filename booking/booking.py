from decimal import Decimal
from itertools import product

from django.conf import settings
from users.models import Saunas

class Booking:
    def __init__(self,request):
        self.session = request.session
        booking = self.session.get(settings.BOOKING_SESSION_ID)
        if not booking:
            booking = self.session[settings.BOOKING_SESSION_ID] = {}
        self.booking = booking


    def add(self,sauna,quantity=1, override_quantity=False):
        sauna_id = str(sauna.id)
        if sauna_id not in self.booking:
            self.booking[sauna_id] = {'quantity':0,
                                      'price':str(sauna.price_per_hour)}
        if override_quantity:
            self.booking[sauna_id]['quantity'] = quantity
        else:
            self.booking[sauna_id]['quantity'] = quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self,sauna):
        sauna_id = str(sauna.id)
        if sauna_id in self.booking:
            del self.booking[sauna_id]
            self.save()

    def __iter__(self):
        sauna_ids = self.booking.keys()
        saunas = Saunas.objects.filter(id__in=sauna_ids)
        booking = self.booking.copy()
        for sauna in saunas:
            booking[str(sauna.id)]['sauna'] = sauna
        for item in booking.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.booking.values())

    def clear(self):
        del self.session[settings.BOOKING_SESSION_ID]
               
    def get_total_price(self):
      total = sum((Decimal(item['price'])-(Decimal(item['price'])
              * Decimal(item['sauna'].discount/100)))*item['quantity']
                for item in self.booking.values())
      return format(total, '.2f')


