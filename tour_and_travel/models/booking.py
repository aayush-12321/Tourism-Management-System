from django.db import models
from .package import Package
from .customer import Customer
import datetime


class Booking(models.Model):
    package = models.ForeignKey(Package,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placebooking(self):
        self.save()

    @staticmethod
    def get_bookings_by_customer(customer_id): # it is used in booking.py view
        return Booking.objects.filter(customer=customer_id).order_by('-date')

    def __str__(self):
        return f"{self.package.name} - {self.customer.first_name}"