from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    subject=models.TextField()
    desc=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return 'Message from: ' + self.name

class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    date=models.DateField() 
    time=models.TimeField()
    guest=models.PositiveIntegerField()

    def __str__(self):
        return 'Message from: ' + self.name

