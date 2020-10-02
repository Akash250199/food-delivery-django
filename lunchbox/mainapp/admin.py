from django.contrib import admin
from .models import Contact,Reservation,Blog,Breakfast_Menu,Lunch_Menu,Dinner_Menu,Dessert_Menu,Wine_Menu,Drink_Menu

# Register your models here.
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Blog)
admin.site.register(Breakfast_Menu)
admin.site.register(Lunch_Menu)
admin.site.register(Dinner_Menu)
admin.site.register(Dessert_Menu)
admin.site.register(Wine_Menu)
admin.site.register(Drink_Menu)