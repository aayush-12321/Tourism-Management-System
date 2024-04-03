from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        # print(address, phone, customer, cart, products)
        i=0
        j=0
        my_bookings=Order.get_orders_by_customer(customer)
        # print(f"bookings= {my_bookings}")
        for product in products:
            i+=1
        for book in my_bookings:
            if book.status!=True:
                j+=1

        if i<2 and j==0:

            for product in products:
                print(cart.get(str(product.id)))
                order = Order(customer=Customer(id=customer),
                            product=product,
                            price=product.price,
                            address=address,
                            phone=phone,
                            quantity=cart.get(str(product.id)))
                order.save()
            request.session['cart'] = {}
            return redirect('cart')


        else:
            # print("Else")
            request.session.get('cart')

            # return redirect('cart',{'message':"Cannot Book Multiple Packages At A Time"})
            return redirect('cart')

