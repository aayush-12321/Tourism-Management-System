from django.db import models
from .package import Package
from .customer import Customer
from django.utils import timezone
import datetime


class Booking(models.Model):
    package = models.ForeignKey(Package,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    no_of_people = models.IntegerField(default=1)
    price = models.IntegerField()
    remarks = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    traveldate = models.DateField(default=datetime.datetime.today)
    Verification = models.BooleanField(default=False)
    # duration=package.duration
    # duration = models.IntegerField(default=1)  # Duration of the booked package

    def set_travel_date(self):
        self.travel_date = timezone.now().date()

    # def set_duration(self):
    #     self.duration = self.package.duration

    def placebooking(self):
        self.set_travel_date()
        # self.set_duration()
        self.save()

    @staticmethod
    def get_bookings_by_customer(customer_id): # it is used in booking.py view
        return Booking.objects.filter(customer=customer_id).order_by('-date')
        # return Booking.objects.filter(customer=customer_id)

    def __str__(self):
        return f"{self.package.name} - {self.customer.first_name}"