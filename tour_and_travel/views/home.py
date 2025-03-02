from django.shortcuts import render , redirect , HttpResponseRedirect
from tour_and_travel.models.package import Package
from tour_and_travel.models.customer import Customer
from tour_and_travel.models.category import Category
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
class Index(View):

    def post(self , request):  # when add to cart is clicked
        package = request.POST.get('package')#will get package id when add to cart is clicked with name package
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            no_of_people = cart.get(package)
            if no_of_people:   # if the package exists in cart 
                if remove:
                    if no_of_people<=1:
                        cart.pop(package)  # remove item of key package from cart dictionary
                    else:
                        cart[package]  = no_of_people-1
                else:
                    cart[package]  = no_of_people+1

            else:
                cart[package] = 1
        else:
            cart = {}
            cart[package] = 1

        request.session['cart'] = cart
        # print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):   #  for showing home page
        # print()
        return HttpResponseRedirect(f'/tms{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    packages = None
    categories = Category.get_all_categories() # it is used to get all category. method id defined in category.py
    categoryID = request.GET.get('category')
    if categoryID:
        packages = Package.get_all_packages_by_categoryid(categoryID) # defines in packages.py modles
    else:
        packages = Package.get_all_packages();  #defined in package.py view

    data = {}
    data['packages'] = packages
    data['categories'] = categories

    # print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


def quickView(request, myid):
    # Fetch the package using the id
    if request.method=="POST":
        package = request.POST.get('package')#will get package id when add to cart is clicked with name package
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            no_of_people = cart.get(package)
            if no_of_people:   # if the package exists in cart 
                if remove:
                    if no_of_people<=1:
                        cart.pop(package)  # remove item of key package from cart dictionary
                    else:
                        cart[package]  = no_of_people-1
                else:
                    cart[package]  = no_of_people+1

            else:
                cart[package] = 1
        else:
            cart = {}
            cart[package] = 1

        request.session['cart'] = cart
        # print('cart' , request.session['cart'])
        # return redirect('homepage')
        package = Package.objects.filter(id=myid)
        
        return render(request, 'quickview.html', {'package':package[0]})
    
    if request.method=="GET":
        
        package = Package.objects.filter(id=myid)
        # print(type(package[0]))
        return render(request, 'quickview.html', {'package':package[0]})


def search_results(request):

    query = request.GET.get('query', '')

    if request.method=="POST":
        package = request.POST.get('package')#will get package id when add to cart is clicked with name package
        remove = request.POST.get('remove') #remove is a name for - in home
        cart = request.session.get('cart')

        if cart:  # checking if cart already exists or not
            no_of_people = cart.get(package)
            if no_of_people:   # if the package exists in cart 
                if remove:
                    if no_of_people<=1:
                        cart.pop(package)  # remove item of key package from cart dictionary
                    else:
                        cart[package]  = no_of_people-1
                else:
                    cart[package]  = no_of_people+1

            else:
                cart[package] = 1
        else:
            cart = {}
            cart[package] = 1

        request.session['cart'] = cart

    if query and len(query) >= 3:
        packages = Package.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
        if len(packages)==0:
            error_message="Please make Sure To Enter Relevent Search!"

            # messages.success(request,"Congratulations! User Registered Successfully.")
            # redirect('homepage')
            return render(request, 'search_results.html', {'packages': packages,'query':query,'error_message':error_message})
        else:
            error_message=None
            return render(request, 'search_results.html', {'packages': packages,'error_message':error_message,'query':query})


def profile(request):
    # Assuming you have authenticated users and you're using Django's built-in User model
    # user = request.user
    customer_id = request.session.get('customer')
    customer=Customer.get_customer_by_id(customer_id)
    # print(customer)
    # print(customer)
    


    return render(request, 'profile.html', {'user': customer})