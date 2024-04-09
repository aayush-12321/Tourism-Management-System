from django.shortcuts import render , redirect,HttpResponse

from django.contrib.auth.hashers import  check_password
from tour_and_travel.models.customer import Customer
from django.views import  View
from tour_and_travel.models.package import  Package

class cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        packages = Package.get_packages_by_id(ids) # it is defined in packages.py modles
        # print(packages)
        return render(request , 'cart.html' , {'packages' : packages} )

