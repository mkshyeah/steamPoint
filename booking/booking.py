from decimal import Decimal
from itertools import product

from django.conf import settings
from ..users.models import Saunas

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
                                      'price':str(sauna.price)}
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
        saunas = Saunas.object.filter(id_in=sauna_ids)
        booking = self.cart.copy()
        for sauna in saunas:
            booking[str(product.id)]['product'] = product
        for item in booking.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.booking.values())

    def clear(self):
        del self.session[settings.BOOKING_SESSION_ID]


