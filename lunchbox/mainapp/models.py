from django.db import models

# Create your models here.

class booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phno = models.IntegerField()
    guest = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()