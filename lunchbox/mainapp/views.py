from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from mainapp.models import Contact,Reservation,Blog,Breakfast_Menu,Lunch_Menu,Dinner_Menu,Dessert_Menu,Wine_Menu,Drink_Menu
import requests
import json
import secrets
from django.conf import settings 
from django.core.mail import send_mail


# Create your views here.

def index(request):
    # Breakfast Object
    item1=Breakfast_Menu.objects.get(item ="Italian Noodles")
    item2=Breakfast_Menu.objects.get(item ="Chole Bhature")
    item3=Breakfast_Menu.objects.get(item ="Egg Soup") 
    some_breakfast=[item1,item2,item3]

    # Lunch Object
    item1=Lunch_Menu.objects.get(item ="Baked Italian Bread")
    item2=Lunch_Menu.objects.get(item ="Roasted Mixed Meat")
    item3=Lunch_Menu.objects.get(item ="Roasted Pork") 
    some_lunch=[item1,item2,item3]

    # Dinner Object
    item1=Dinner_Menu.objects.get(item ="Murgh Biryani")
    item2=Dinner_Menu.objects.get(item ="Sweet Salad")
    item3=Dinner_Menu.objects.get(item ="Mexican Pizza") 
    some_dinner=[item1,item2,item3]

    # Dessert Object
    item1=Dessert_Menu.objects.get(item ="Ice Cream" )
    item2=Dessert_Menu.objects.get(item ="Choco Cake")
    item3=Dessert_Menu.objects.get(item ="Swedish Ice Cream") 
    some_dessert=[item1,item2,item3]

    # Wine Object
    item1=Wine_Menu.objects.get(item ="Turkish Wine")
    item2=Wine_Menu.objects.get(item ="Cranberry")
    item3=Wine_Menu.objects.get(item ="Blue Velvet") 
    some_wine=[item1,item2,item3]

    # Drink object
    item1=Drink_Menu.objects.get(item ="Orange Juice")
    item2=Drink_Menu.objects.get(item ="Orange Velvet")
    item3=Drink_Menu.objects.get(item ="Lemon Squadr") 
    some_drink=[item1,item2,item3]

    # Blog Object
    item1=Blog.objects.get(date="2020-08-13")
    item2=Blog.objects.get(date="2020-07-31")
    item3=Blog.objects.get(date="2020-09-10") 
    some_blog=[item1,item2,item3]


    return render(request, 'mainapp/index.html',
                                                {"Some_breakfast_Menus":some_breakfast,"Some_lunch_Menus":some_lunch,
                                                "Some_dinner_Menus":some_dinner,"Some_dessert_Menus":some_dessert,
                                                "Some_wine_Menus":some_wine,"Some_drink_Menus":some_drink,
                                                "Some_blogs":some_blog})
def about(request):
    return render(request,'mainapp/about.html')
def chef(request):
    return render(request,'mainapp/chef.html')
def menu(request):
    all_breakfast_menu=Breakfast_Menu.objects.all()
    all_lunch_menu=Lunch_Menu.objects.all()
    all_dinner_menu=Dinner_Menu.objects.all()
    all_dessert_menu=Dessert_Menu.objects.all()
    all_wine_menu=Wine_Menu.objects.all()
    all_drink_menu=Drink_Menu.objects.all()
    return render(request,'mainapp/menu.html',
                                            {"breakfast_Menus":all_breakfast_menu,"lunch_Menus":all_lunch_menu,
                                            "dinner_Menus":all_dinner_menu,"dessert_Menus":all_dessert_menu,
                                            "wine_Menus":all_wine_menu,"drink_Menus":all_drink_menu})
def reservation(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email'].lower()   # if the user enter upper case email then lower() automatically turned into in lower case
        phone=request.POST['phone']
        date=request.POST['date']
        time=request.POST['time']
        guest=request.POST['guest']


        if len(name)<3 or len(email)<3 or len(phone)<10 or len(guest)<1:
            messages.error(request,"Make sure the information is complete and valid!")
            return redirect('reservation')
        
        if any(not name.isalpha() and not name.isspace() for name in name): 
            messages.error(request,"Please type Valid Name!")
            return redirect('reservation')

        if not phone.isdigit():
            messages.error(request,"Please type Phone Number!")
            return redirect('reservation')
        else:
            reservation=Reservation(name=name,email=email,phone=phone,date=date,time=time,guest=guest)
            reservation.save()
            subject = 'Booking Confirmed !! LunchBox'
            message = f'Hi {name}, Your Table Booking for {guest} persons is Confirmed at {time} on {date} .\n\nThank you for Choosing Us. '
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list )

            messages.success(request,"Booking Confirmed and Your Details has been Sent Via Email Successfully")
            return redirect('reservation')

    return render(request,'mainapp/reservation.html')
def bookings(request):
    all_bookings=Reservation.objects.all()
    return render(request,'mainapp/bookings.html',{"Details":all_bookings})
def blog(request):
    all_blog=Blog.objects.all()
    return render(request,'mainapp/blog.html',{"Blogs":all_blog})
def blogs(request):
    return render(request,'mainapp/blog-single.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email'].lower()
        phone=request.POST['phone']
        subject=request.POST['subject']
        desc=request.POST['desc']

        #captcha
        clientkey=request.POST['g-recaptcha-response']
        secretkey='6LdunscZAAAAAJ_PFLDKtmlY-Dnx4V4CuA0IBoDj'
        capthchaData={
            'secret': secretkey,
            'response': clientkey
        }
        r= requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
        response=json.loads(r.text)
        verify= response['success']
        if verify:
            if any(not name.isalpha() and not name.isspace() for name in name):
                messages.error(request,"Please type Valid Name!")               
                return redirect('contactus')

            if not phone.isdigit():
                messages.error(request,"Please type Phone Number!")
                return redirect('contactus')

            if len(name)<3 or len(email)<3 or len(phone)<10 or len(subject)<4 or len(desc)<5:
                messages.error(request,"Make sure the information is complete and valid!")
                return redirect('contactus')

            else:
                contact=Contact(name=name,email=email,phone=phone,subject=subject,desc=desc)
                contact.save()
                subject = 'Message Sent Successfully !! LunchBox'
                message = f'Hi {name}, We have received Your message and will get back to you Soon.'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [email] 
                send_mail( subject, message, email_from, recipient_list )

                messages.success(request,"Your Message has been Successfully sent")
                return redirect('contactus')
        else:
            messages.error(request,"Error sending message, Invalid Credentials/captcha")
            return redirect('contactus') 
    all_messages=Contact.objects.all()
    return render(request, 'mainapp/contact.html',{"Messages":all_messages})

def developer(request):
    return render(request,'mainapp/developer.html')
def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email'].lower()   
        otp=request.POST['otp'] 
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        """secretsgen=secrets.SystemRandom()
        opt=secretsgen.randrange(100000,999999)
        subject = 'Otp for signup !! LunchBox'
        message = f'Hi {fname}  Your Otp is {opt} .\n\nThank you for Choosing Us. '
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email] 
        send_mail( subject, message, email_from, recipient_list )"""

        if len(username)>10:
            messages.error(request,"username mustbe under 10 characters")
            return redirect('home')
        
        if len(pass1)<6:
            messages.error(request,"Password mustbe atleast 6 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"username should only contains letter & number")
            return redirect('home')
        if not otp==opt:
            messages.error(request,"Otp does not Match")
            return redirect('home')



        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already Taken")
                return redirect('home')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already Taken")
                return redirect('home')  
            else:
                # captcha
                clientkey=request.POST['g-recaptcha-response']
                secretkey='6LdunscZAAAAAJ_PFLDKtmlY-Dnx4V4CuA0IBoDj'
                capthchaData={
                    'secret': secretkey,
                    'response': clientkey
                }
                r= requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
                response=json.loads(r.text)
                verify= response['success']
                if verify:
                    myuser=User.objects.create_user(username=username,email=email,otp=otp,password=pass1,first_name=fname,last_name=lname)
                    myuser.save()

                    #email
                    subject = 'Sign Up Successful !! LunchBox'
                    message = f'Hi {fname}, Thank you for registering in LunchBox.\n\nNow Login using this Username:- {username} and Password:- {pass1}'
                    email_from = settings.EMAIL_HOST_USER 
                    recipient_list = [email] 
                    send_mail( subject, message, email_from, recipient_list )
                    messages.success(request,"Your Credentials sent via Email and Account Succesfully Created")
                    return redirect('home')
                else:
                    messages.error(request,"Error creating account! Make sure that you have entered correct information")
                    return redirect('home')        
        else:
            messages.error(request,"Passwords does not Match")
            return redirect('home')

    else:
        messages.error(request,"Login First")
        return redirect('home')

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            if not user.is_staff:   
                login(request,user)
                messages.success(request,"Successfully Logged In")
                return redirect('home')   
            else:
                messages.error(request,"This is not for Restaurant User")
                return redirect('home')
        else:
            messages.error(request,"Invalid Credentials,Try Again")
            return redirect('home')

    else:
        return HttpResponse('404-not found')

def handleadminlogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            if user.is_staff: 
                login(request,user)
                messages.success(request,"Successfully Logged In")
                return redirect('home')
            else:
                messages.error(request,"This is not for Normal User ")
                return redirect('home')

        else:
            messages.error(request,"Invalid Credentials,Try Again")
            return redirect('home')

    else:
        return HttpResponse('404-not found')



def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('home')

    

