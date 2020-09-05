from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainapp.models import booking
from mainapp.forms import reserv
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')
def about(request):
    return render(request,'mainapp/about.html')
def chef(request):
    return render(request,'mainapp/chef.html')
def menu(request):
    return render(request,'mainapp/menu.html')
def reservation(request):
    if request.method == 'POST':
        a=reserv(request.POST)
        if a.is_valid():
            try:
                a.save()
                print('Booking conirmed')
                return redirect('/')
            except:
                pass
		
        
    else:
        return render(request,'mainapp/reservation.html')
def blog(request):
    return render(request,'mainapp/blog.html')
def blogs(request):
    return render(request,'mainapp/blog-single.html')
def contact(request):
    return render(request, 'mainapp/contact.html')
def developer(request):
    return render(request,'mainapp/developer.html')


