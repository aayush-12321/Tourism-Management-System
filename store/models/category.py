from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod  # it does not require an instance of class to be called
    def get_all_categories():  # to get all category. it is used in home.py
        return Category.objects.all()


    def __str__(self):
        return self.name
