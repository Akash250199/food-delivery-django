# creating urls
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/',views.about,name='aboutus'),
    path('chef/',views.chef,name='chef'),
    path('menu/',views.menu,name='menu'),
    path('reserve/',views.reservation,name='reservation'),
    path('blog/',views.blog,name='blog'),
    path('blogs/',views.blogs,name='blogs'),
    path('contact/',views.contact,name='contactus'),
    path('developer/',views.developer,name='developedby'),
    
 
   
]