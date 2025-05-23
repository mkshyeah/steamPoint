from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create_booking(request):
    return render(request, "booking/booking.html")