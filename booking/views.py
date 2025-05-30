from itertools import product

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from users.models import Saunas
from booking.booking import Booking
from .forms import BookingAddSaunaForm

@require_POST
def booking_add(request,sauna_id):
    booking = Booking(request)
    sauna = get_object_or_404(Saunas, id=sauna_id)
    form = BookingAddSaunaForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        booking.add(sauna=sauna,
                    quantity=cd['quantity'],
                    override_quantity=cd['override'])

    return redirect('booking:booking_detail')

@require_POST
def booking_remove(request, sauna_id):
    booking = Booking(request)
    sauna = get_object_or_404(Saunas, id=sauna_id)
    booking.remove(sauna)
    return redirect('booking:booking_detail')

def booking_detail(request):
    booking = Booking(request)
    return  render(request,'booking/detail.html',{'booking':booking})
