from django.shortcuts import render, redirect
from tour_and_travel.models.customer import Customer
from django.views import View
from tour_and_travel.models.package import Package
from tour_and_travel.models.booking import Booking
import datetime



class CheckOut(View):
    def post(self, request):
        traveldate=request.POST.get('traveldate') # Retrieve the travel date from the form
       
        return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )
