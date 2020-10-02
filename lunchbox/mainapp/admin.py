from django.contrib import admin
from .models import Contact,Reservation,Blog

# Register your models here.
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Blog)
