from django.shortcuts import render,redirect
from django.urls import reverse
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
        discounted_price = item['sauna'].sell_price() 
        OrderItem.objects.create(order=order,
                                 saunas=item['sauna'],
                                 price_per_hour=discounted_price,
                                 quantity = item['quantity'])
        
      booking.clear()
      request.session['order_id'] = order.id
      return redirect(reverse('payment:process'))
      
  else:
    form = OrderCreateForm(request=request)
  return render(request,
                'order/create.html',
                {'booking':booking,
                 'form':form})
  