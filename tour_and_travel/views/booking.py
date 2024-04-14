from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from tour_and_travel.models.customer import Customer
from django.views import View

from tour_and_travel.models.package import Package
from tour_and_travel.models.booking import Booking
from tour_and_travel.middlewares.auth import auth_middleware

class bookingView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        bookings = Booking.get_bookings_by_customer(customer) # it is defined in bookings.py modles
        
        # print(bookings)
        return render(request , 'booking.html'  , {'bookings' : bookings})
