from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('dev',views.developer,name='developer'),
    path('res',views.reservation,name='reservation'),
    path('abt',views.about,name='aboutus'),
    path('men',views.menu,name='menu'),
    path('blg',views.blog,name='blog'),
    path('con',views.contact,name='contact'),
]