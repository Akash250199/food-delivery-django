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
    path('bookings/',views.bookings,name='bookings'),
    path('blog/',views.blog,name='blog'),
    path('blogs/',views.blogs,name='blogs'),
    path('contact/',views.contact,name='contactus'),
    path('developer/',views.developer,name='developedby'),
    path('signup/',views.handlesignup,name='signup'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
]
