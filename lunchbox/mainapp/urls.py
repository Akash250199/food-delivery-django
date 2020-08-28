from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact,name='contact'),
    path('dev',views.developer,name='developer'),
    path('res',views.reservation,name='reservation')
]