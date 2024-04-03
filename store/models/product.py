from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    # price = models.IntegerField(default=0)
    price = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod # it does not require an instance of class to be called
    def get_products_by_id(ids): # it is used in cart.py views
        return Product.objects.filter(id__in =ids)  # here ids is a list so id__in is used

    @staticmethod
    def get_all_products(): #used in home.py
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id): #used in checkout.py
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()