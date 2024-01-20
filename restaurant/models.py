from django.db import models

# Create your models here.
class Booking(models.Model):
    # id = models.SmallIntegerField(default =5)
    name = models.CharField(max_length=200)
    no_of_guests = models.SmallIntegerField
    booking_date = models.DateTimeField()
    
    


class Menu(models.Model):
    # id = models.SmallIntegerField(default =5)
    title = models.CharField(max_length= 255)
    price = models.DecimalField(max_digits =10, decimal_places= 2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    
class User(models.Model):
   url = models.CharField(max_length=200)
   username = models.CharField(max_length= 200)
   email =models.CharField(max_length= 200)
   groups = models.CharField(max_length= 200)