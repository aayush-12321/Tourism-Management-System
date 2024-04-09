from django.db import models
from .category import Category


class Package(models.Model):
    name = models.CharField(max_length=50)
    # price = models.IntegerField(default=0)
    price = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/packages/')

    @staticmethod # it does not require an instance of class to be called
    def get_packages_by_id(ids): # it is used in cart.py views
        return Package.objects.filter(id__in =ids)  # here ids is a list so id__in is used

    @staticmethod
    def get_all_packages(): #used in home.py
        return Package.objects.all()

    @staticmethod
    def get_all_packages_by_categoryid(category_id): #used in checkout.py
        if category_id:
            return Package.objects.filter(category = category_id)
        else:
            return Package.get_all_packages()