from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
class Index(View):

    def post(self , request):  # when add to cart is clicked
        product = request.POST.get('product')#will get product id when add to cart is clicked with name product
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            quantity = cart.get(product)
            if quantity:   # if the product exists in cart 
                if remove:
                    if quantity<=1:
                        cart.pop(product)  # remove item of key product from cart dictionary
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):   #  for showing home page
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories() # it is used to get all category. method id defined in category.py
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID) # defines in products.py modles
    else:
        products = Product.get_all_products();  #defined in product.py view

    data = {}
    data['products'] = products
    data['categories'] = categories

    # print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


def quickView(request, myid):
    # Fetch the product using the id
    if request.method=="POST":
        product = request.POST.get('product')#will get product id when add to cart is clicked with name product
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            quantity = cart.get(product)
            if quantity:   # if the product exists in cart 
                if remove:
                    if quantity<=1:
                        cart.pop(product)  # remove item of key product from cart dictionary
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print('cart' , request.session['cart'])
        # return redirect('homepage')
        product = Product.objects.filter(id=myid)
        
        return render(request, 'quickview.html', {'product':product[0]})
    
    if request.method=="GET":
        
        product = Product.objects.filter(id=myid)
        # print(type(product[0]))
        return render(request, 'quickview.html', {'product':product[0]})


def search_results(request):

    query = request.GET.get('query', '')

    if request.method=="POST":
        product = request.POST.get('product')#will get product id when add to cart is clicked with name product
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            quantity = cart.get(product)
            if quantity:   # if the product exists in cart 
                if remove:
                    if quantity<=1:
                        cart.pop(product)  # remove item of key product from cart dictionary
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

    if query and len(query) >= 3:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
        error_message=None
        return render(request, 'search_results.html', {'products': products,'error_message':error_message,'query':query})
    else:
        # products = []
        error_message="Please make Sure To Enter Relevent Search!"
        # messages.error(request,"Wrong credentials!!!")
        # return redirect('homepage')

        return render(request, 'search_results.html', {'error_message':error_message,'query':query})
