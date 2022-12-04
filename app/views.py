from sre_constants import SUCCESS
from django.core.mail import send_mail
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings



def index(request):
    return render(request,'index.html')
def About(request):
    return render(request,'About.html')
def Home(request):
    return render(request,'Home.html')
def contact(request):
    return render(request,'contact.html')
def base(request):
    return render(request,'base.html')
def loan(request):
    return render(request,'loan.html')
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            return render(request, "success.html")
        else:
            return HttpResponse("<h1>Wrong credentials check again!</h1>")
    return render(request,'signin.html')
def Register(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(email=request.POST['email'])
                return HttpResponse("Email already taken")                
            except User.DoesNotExist:
                myuser=User.objects.create_user(username,email,password)
                myuser.save()
                send_mail(
                'From SAM Banking Systems',
                'Hello Sir/Mam Thanks for choosing our bank and we aim to provide you the best services ',
                'ananya.vijju@gmail.com',
                [email],
                fail_silently = False,)
                return render(request,'success.html')

    return render(request,'Register.html')

def next(request):
    return render(request,'next.html')
def next2(request):
    return render(request,'next2.html')
def next3(request):
    return render(request,'next3.html')
def next4(request):
    return render(request,'next4.html')
def next5(request):
    return render(request,'next5.html')
def next6(request):
    return render(request,'next6.html')

def feedback(request):
    return render(request,'feedback.html')

def handelLogout(request):
    messages.success(request, "Successfully logged out")
    return render(request,'index.html')
