from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from booking.booking import Booking


# Create your views here.

def order_create(request):
  booking = Booking(request)
  if request.method == "POST":
    form = OrderCreateForm(request.POST, request=request)
    if form.is_valid():
      order = form.save()
      for item in booking:
        OrderItem.objects.create(order=order,
                                 saunas=item['sauna'],
                                 price_per_hour=item['price'],
                                 quantity = item['quantity'])
        
      booking.clear()
      return render(request,
                    'order/created.html',
                    {'order':order,
                     'form':form})
      
  else:
    form = OrderCreateForm(request=request)
  return render(request,
                'order/create.html',
                {'booking':booking,
                 'form':form})
  