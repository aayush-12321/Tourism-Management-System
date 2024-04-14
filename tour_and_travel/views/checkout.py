from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from tour_and_travel.models.customer import Customer
from django.views import View

from tour_and_travel.models.package import Package
from tour_and_travel.models.booking import Booking
from django.utils import timezone
import datetime



'''
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        packages = Package.get_packages_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, packages)
        no_of_prods=len(packages)
        print(no_of_prods)

        message=None
        error=False

        
        for package in packages:
            
            # print(cart.get(str(package.id)))
            booking = booking(customer=Customer(id=customer),
                        package=package,
                        price=package.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(package.id)))
            booking.save()
            message="   booking Placed!"

        request.session['cart'] = {}
            
            
        # print(f"Is Placed: {is_placed}")

        
        if no_of_prods==0:
            message="   Unable to Check-Out!"
            error=True
        # elif:
        #     message=

        # print(message)
        # return redirect('cart')
        return render(request , 'cart.html' , {'message' : message,'error':error} )

'''

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('remark')
        phone = request.POST.get('phone')
        traveldate=request.POST.get('traveldate')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        packages = Package.get_packages_by_id(list(cart.keys()))
        no_of_prods=len(packages)
        print(traveldate)
        # print(address, phone, customer, cart, packages)
        i=0
        j=0
        message=None
        error=False
        my_bookings=Booking.get_bookings_by_customer(customer)
        # print(f"bookings= {my_bookings}")
        for package in packages:
            i+=1
        for book in my_bookings:
            if book.status!=True:
                j+=1

        if i<2 and j==0:
            # print(datetime.datetime.today),

            for package in packages:
                # print(cart.get(str(package.id)))

                booking = Booking(customer=Customer(id=customer),
                            package=package,
                            price=package.price,
                            address=address,
                            phone=phone,
                            traveldate=traveldate,
                            # travel_date=datetime.datetime.today,  #
                            quantity=cart.get(str(package.id)))
                booking.save()
                message="   Successfully Booked!"

            request.session['cart'] = {}
            # return redirect('cart')
            
            if no_of_prods==0:
                message="   Unable to Check-Out!"
                error=True
            # elif:
            #     message=

            # print(message)
            # return redirect('cart')
            return render(request , 'cart.html' , {'message' : message,'error':error} )

        else:
            ids = list(request.session.get('cart').keys())
            packages = Package.get_packages_by_id(ids) # it is defined in packages.py modles
            message="   Only one package can be booked at a time! "
            error=True
            return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )

