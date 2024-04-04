from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from tour_and_travel.models.customer import Customer
from django.views import View

from tour_and_travel.models.package import Package
from tour_and_travel.models.booking import Booking


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        packages = Package.get_packages_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, packages)
        i=0
        j=0
        my_bookings=Booking.get_bookings_by_customer(customer)
        # print(f"bookings= {my_bookings}")
        for package in packages:
            i+=1
        for book in my_bookings:
            if book.status!=True:
                j+=1

        if i<2 and j==0:

            for package in packages:
                print(cart.get(str(package.id)))
                booking = Booking(customer=Customer(id=customer),
                            package=package,
                            price=package.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(package.id)))
                booking.save()
            request.session['cart'] = {}
            return redirect('cart')


        else:
            # print("Else")
            request.session.get('cart')

            # return redirect('cart',{'message':"Cannot Book Multiple Packages At A Time"})
            return redirect('cart')

