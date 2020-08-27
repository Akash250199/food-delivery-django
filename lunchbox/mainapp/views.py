from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return render(request, 'mainapp/contact.html')
def developer(request):
    return render(request,'mainapp/developer.html')
def reservation(request):
    return render(request,'mainapp/reservation.html')