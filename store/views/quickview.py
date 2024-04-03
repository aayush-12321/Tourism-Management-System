from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View


class ProductView(View):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)




    return render(request, 'shop/prodView.html', {'product':product[0]})