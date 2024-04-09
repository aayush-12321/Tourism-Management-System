from django.contrib import admin
from .models.package import Package
from .models.category import Category
from .models.customer import Customer
from .models.booking import Booking


class Adminpackage(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Package, Adminpackage)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer )
admin.site.register(Booking )
