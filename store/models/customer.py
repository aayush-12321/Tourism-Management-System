from django.db import  models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod # it does not require an instance of class to be called
    def get_customer_by_email(email): # it is used in login.py to get customer
        try:  # get throws error if email is not present in db 
            return Customer.objects.get(email=email)  # get will give single record but filter will give list
        except:
            return False


    def isExists(self): # it is used in signup.py to check if email already exists or not
        if Customer.objects.filter(email = self.email) or Customer.objects.filter(phone=self.phone):
            return True

        return  False
    
    def __str__(self):
        return self.first_name


