from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from tour_and_travel.models.customer import Customer
from django.views import View

from tour_and_travel.models.package import Package
from tour_and_travel.models.booking import Booking
from django.utils import timezone
import datetime




class CheckOut(View):
    def post(self, request):
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        packages = Package.get_packages_by_id(list(cart.keys()))
        message = None
        error = False
        remarks = request.POST.get(f'remark')
        phone = request.POST.get(f'phone')
        # if len(phone) < 10:
        #      message = 'Phone Number must be 10 char Long!!'
        #      error=True
        # else:
        #     try:
        #         int(phone)
        #     except:
        #         message = 'Enter Phone Number Correctly!!'
        #         error=True
        print(remarks)
        print(phone)


        # Dictionary to store end dates of the bookings
        booking_end_dates = {}

        # Get the list of dates being booked along with end dates
        for package in packages:
            traveldate = request.POST.get(f'traveldate{package.id}')
            duration = package.duration
            travel_date = datetime.datetime.strptime(traveldate, '%Y-%m-%d').date()
            end_date = travel_date + datetime.timedelta(days=duration)
            booking_end_dates[travel_date] = end_date

        # Get the existing bookings for the customer
        existing_bookings = Booking.objects.filter(customer_id=customer_id)

        # Check for date collisions
        for start_date, end_date in booking_end_dates.items():
            for booking in existing_bookings:
                booking_start_date = booking.traveldate
                booking_end_date = booking_start_date + datetime.timedelta(days=booking.package.duration)
                if (start_date <= booking_start_date <= end_date) or (start_date <= booking_end_date <= end_date):
                    error = True
                    message = "Booking failed! Package cannot be booked for overlapping dates."
                    break
            if error:
                break

        if not packages:
            message = "Unable to Check-Out!"
            error = True
            return render(request, 'cart.html', {'message': message, 'error': error})

        elif not error:
            # Create bookings
            for package in packages:
                traveldate = request.POST.get(f'traveldate{package.id}')
                booking = Booking(customer=Customer(id=customer_id),
                                  package=package,
                                  price=package.price,
                                  traveldate=traveldate,
                                  remarks=remarks,
                                  phone=phone,
                                  no_of_people=cart.get(str(package.id)))
                booking.save()
            message = "Successfully Booked!"
            request.session['cart'] = {}
            return render(request, 'cart.html', {'message': message, 'error': error})

        else:
            error=True
            message = "Booking failed! Package cannot be booked for the same date as another package."
            ids = list(request.session.get('cart').keys())
            packages = Package.get_packages_by_id(ids)
            return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )



        # return render(request, 'cart.html', {'message': message, 'error': error})



# class CheckOut(View):
#     def post(self, request):
#         customer_id = request.session.get('customer')
#         cart = request.session.get('cart')
#         packages = Package.get_packages_by_id(list(cart.keys()))
#         message = None
#         error = False

#         # Get the list of dates being booked
#         date_being_booked = [request.POST.get(f'traveldate{package.id}') for package in packages]

#         # Convert date strings to datetime objects
#         date_being_booked = [datetime.datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_being_booked]

#         # Get the existing bookings for the customer for the given dates
#         existing_bookings = Booking.objects.filter(customer_id=customer_id, traveldate__in=date_being_booked)

#         # Collect all dates being booked to check for duplicates
#         all_dates = set()
#         for date in date_being_booked:
#             if date in all_dates:
#                 error = True
#                 message = "Booking failed! Multiple packages cannot be booked for the same date."
#                 break
#             all_dates.add(date)

#         if not error:
#             if not packages:
#                 message = "Unable to Check-Out!"
#                 error = True
#                 return render(request, 'cart.html', {'message': message, 'error': error})
#             elif existing_bookings.exists():
#                 error = True
#                 message = "Booking failed! Package cannot be booked for the same date as another package."
#                 ids = list(request.session.get('cart').keys())
#                 packages = Package.get_packages_by_id(ids)
#                 return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )
                
#             else:
#                 # Create bookings
#                 for package in packages:
#                     traveldate = request.POST.get(f'traveldate{package.id}')
#                     booking = Booking(customer=Customer(id=customer_id),
#                                       package=package,
#                                       price=package.price,
#                                       traveldate=traveldate,
#                                       no_of_people=cart.get(str(package.id)))
#                     booking.save()
#                 message = "Successfully Booked!"
#                 request.session['cart'] = {}
#                 return render(request, 'cart.html', {'message': message, 'error': error})
#         else:
#             error=True
#             message = "Booking failed! Package cannot be booked for the same date as another package."
#             ids = list(request.session.get('cart').keys())
#             packages = Package.get_packages_by_id(ids)
#             return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )








# class CheckOut(View):
#     def post(self, request):
#         customer_id = request.session.get('customer')
#         cart = request.session.get('cart')
#         packages = Package.get_packages_by_id(list(cart.keys()))
#         message = None
#         error = False

#         # Get the list of dates being booked
#         date_being_booked = [request.POST.get(f'traveldate{package.id}') for package in packages]

#         # Convert date strings to datetime objects
#         date_being_booked = [datetime.datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_being_booked]

#         # Get the existing bookings for the customer for the given dates
#         existing_bookings = Booking.objects.filter(customer_id=customer_id, traveldate__in=date_being_booked)


#         if not packages:
#             message = "Unable to Check-Out!"
#             error = True
#             return render(request, 'cart.html', {'message': message, 'error': error})
#         elif existing_bookings.exists():
#             error = True
#             message = "Booking failed! Package cannot be booked for the same date as another package."
#             ids = list(request.session.get('cart').keys())
#             packages = Package.get_packages_by_id(ids)
#             return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )

#         else:
#             # Create bookings
#             for package in packages:
#                 traveldate = request.POST.get(f'traveldate{package.id}')
#                 booking = Booking(customer=Customer(id=customer_id),
#                                   package=package,
#                                   price=package.price,
#                                   traveldate=traveldate,
#                                   no_of_people=cart.get(str(package.id)))
#                 booking.save()
#             message = "Successfully Booked!"
#             request.session['cart'] = {}
#             return render(request, 'cart.html', {'message': message, 'error': error})


       



# class CheckOut(View):
#     def post(self, request):
#         # address = request.POST.get('remark')
#         # phone = request.POST.get('phone')
#         # traveldate=request.POST.get('traveldate')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         packages = Package.get_packages_by_id(list(cart.keys()))
#         no_of_prods=len(packages)
#         i=0
#         j=0
#         message=None
#         error=False
#         my_bookings=Booking.get_bookings_by_customer(customer)
#         bookeddates=[]
#         date_being_booked=[]
       
#         for book in my_bookings:
#             # if book.status==False :
#             #     bookeddates.append(book.traveldate)
#             pass
#                 # j+=1
#         for package in packages:
#             # # i+=1
#             # date_being_booked.append(request.POST.get(f'traveldate{package.id}'))
#             pass


#         # for i in range(len(date_being_booked)):
#         #     for j in range(0,len(date_being_booked)-i-1):
#         #         if date_being_booked[j]==date_being_booked[i]:
#         #             print("not available")


#         print(date_being_booked)
#         print(bookeddates)
        

#         # if i<2 and j==0:
#             # print(datetime.datetime.today),
#             #
#         for package in packages:
#             # print(f"traveldate{package.id}")
#             traveldate=request.POST.get(f'traveldate{package.id}')

#             # print(cart.get(str(package.id)))

#             booking = Booking(customer=Customer(id=customer),
#                         package=package,
#                         price=package.price,
#                         # address=address,
#                         # phone=phone,
#                         traveldate=traveldate,
#                         # travel_date=datetime.datetime.today,  #
#                         no_of_people=cart.get(str(package.id)))
#             booking.save()
#             message="   Successfully Booked!"

#         request.session['cart'] = {}
#         # return redirect('cart')
        
#         if no_of_prods==0:
#             message="   Unable to Check-Out!"
#             error=True
#         # elif:
#         #     message=

#         # print(message)
#         # return redirect('cart')
#         return render(request , 'cart.html' , {'message' : message,'error':error} )
##############################
        # else:
        #     ids = list(request.session.get('cart').keys())
        #     packages = Package.get_packages_by_id(ids) # it is defined in packages.py modles
        #     message="   Only one package can be booked at a time! "
        #     error=True
        #     return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )


# from django.shortcuts import render, redirect,HttpResponse
# from tour_and_travel.models.customer import Customer
# from django.views import View
# from tour_and_travel.models.package import Package
# from tour_and_travel.models.booking import Booking
# import datetime
# import forms

# class CheckOut(View):
#     def post(self, request):
#         # traveldate_form = forms.TravelDateForm(request.POST) 
#         # contact_form = forms.ContactForm(request.POST)        
#         traveldate=request.POST.get('traveldate') # Retrieve the travel date from the form
#         address = request.POST.get('remark')
#         phone = request.POST.get('phone')
#         # print(traveldate_form.is_valid())
#         # print(contact_form.is_valid())
#         # if traveldate_form.is_valid() and contact_form.is_valid():
#             # traveldate = traveldate_form.cleaned_data['traveldate']
#             # address = contact_form.cleaned_data['address']
#             # phone = contact_form.cleaned_data['phone'] # indent <-
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         packages = Package.get_packages_by_id(list(cart.keys()))
#         no_of_prods=len(packages)
#         i=0
#         j=0
#         message=None
#         error=False
#         my_bookings=Booking.get_bookings_by_customer(customer)
#         print(traveldate)
#         print(address)
#         print(phone)
#         for package in packages:
#             i+=1
#         for book in my_bookings:
#             if book.status!=True:
#                 j+=1
#         # if not traveldate:
#         if i<2 and j==0:
#             for package in packages:
#                 # if traveldate:
#                 booking = Booking(customer=Customer(id=customer),
#                             package=package,
#                             price=package.price,
#                             address=address,
#                             phone=phone,
#                             traveldate=traveldate,
#                             no_of_people=cart.get(str(package.id)))
#                 # else: 
#                 #     booking = Booking(customer=Customer(id=customer),
#                 #                 package=package,
#                 #                 price=package.price,
#                 #                 address=address,
#                 #                 phone=phone,
#                 #                 traveldate=traveldate,
#                 #                 no_of_people=cart.get(str(package.id)))
#                 booking.save()
#                 message="Successfully Booked!"

#             request.session['cart'] = {}
            
#             if no_of_prods==0:
#                 message="Unable to Check-Out!"
#                 error=True

#             return render(request , 'cart.html' , {'message' : message,'error':error} )

#         else:
#             ids = list(request.session.get('cart').keys())
#             packages = Package.get_packages_by_id(ids)
#             message="Only one package can be booked at a time!"
#             error=True
#             return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )
#         # else:
#         #     print(traveldate_form.cleaned_data['traveldate'])
#         #     ids = list(request.session.get('cart').keys())
#         #     packages = Package.get_packages_by_id(ids)
#         #     message="Error"
#         #     error=True
#         #     return render(request, 'cart.html', {'traveldate_form': traveldate_form, 'contact_form': contact_form,'message' : message,'error':error,'packages' : packages})
#             # return render(request , 'cart.html' , {'message' : message,'error':error,'packages' : packages} )
#     # def get(self,request):
#     #     pass