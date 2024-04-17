from django.contrib import admin
from django.urls import path
from .views.home import Index , store,quickView,search_results,profile
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import cart
from .views.checkout import CheckOut
from .views.booking import bookingView

from .middlewares.auth import  auth_middleware



urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('tms', store , name='tms'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),  
    path('logout', logout , name='logout'),
    path('cart/', auth_middleware(cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
   
    path('booking', auth_middleware(bookingView.as_view()), name='booking'),
    # path("quickview/1",quickView,name='quickView'),
    path("quickview/<int:myid>",quickView,name='quickView'),
    path('search/', search_results, name='search_results'),
    path('profile/', auth_middleware(profile), name='profile'),
   

    # Login.as_view() because class based view is used login.py
]

