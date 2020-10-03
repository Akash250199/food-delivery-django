from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    subject=models.TextField()
    desc=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    class Meta:
        verbose_name_plural = "1. Contacts"  # This is used to Modify Order in django admin

    def __str__(self):
        return 'Message from: ' + self.name  # This is used to see the name after saving anything in database table
    

class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    date=models.DateField() 
    time=models.TimeField()
    guest=models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "2. Reservations"

    def __str__(self):
        return 'Booking from: ' + self.name

class Blog(models.Model):
    
    img=models.ImageField(upload_to='images')
    date=models.DateField()
    uploadby=models.CharField(max_length=100) 
    subject=models.TextField()
    
    class Meta:
        verbose_name_plural = "3. Blogs"

    def __str__(self):
        return 'Blogs: ' + self.subject

class Breakfast_Menu(models.Model):
    item=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    img=models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "4. Breakfast_Menus"

    def __str__(self):
        return 'Breakfast_Menu: ' + self.item
        
class Lunch_Menu(models.Model):
    item=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    img=models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "5. Lunch_Menus"

    def __str__(self):
        return 'Lunch_Menu: ' + self.item

class Dinner_Menu(models.Model):
    item=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    img=models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "6. Dinner_Menus"

    def __str__(self):
        return 'Dinner_Menu: ' + self.item

class Dessert_Menu(models.Model):
    item=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    img=models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "7. Dessert_Menus"

    def __str__(self):
        return 'Dessert_Menu: ' + self.item

class Wine_Menu(models.Model):
    item=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    img=models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "8. Wine_Menus"

    def __str__(self):
        return 'Wine_Menu: ' + self.item

class Drink_Menu(models.Model):
    item=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    img=models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "9. Drink_Menus"

    def __str__(self):
        return 'Drink_Menu: ' + self.item

