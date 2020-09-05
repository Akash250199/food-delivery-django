from django.db import models

# Create your models here.

class booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.IntegerField()
    guest = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()


"""class Reservation(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phno = models.CharField(max_length=13)
    guest = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()"""