from urllib import request
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse,redirect
from .models import Contact,Login,Register,Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages
import json
import requests
#template rendering
def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"home.html")

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"about.html")

def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    elif request.method== "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        orderNumber=request.POST.get('orderNumber')
        customerNote=request.POST.get('customerNote')
        data={
            'name':name,
            'email':email,
            'phone':phone,
            'customerNote':customerNote
        }
        customerNote='''
        New customerNote:{}
        From:{}
        '''.format(data['customerNote'],data['email'])
        send_mail(data['phone'],customerNote,'',['oggy21176940@gmail.com'])
        contact=Contact(name=name,email=email,phone=phone,ordernum=orderNumber,msg=customerNote)
        contact.save()
        messages.success(request, 'Your response has been saved!!')
        return redirect("/home")
    return render(request,"contact.html")


def rentalsavailable(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"rentalsavailable.html")

def loginUser(request):
    if request.method== "POST":
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have successfully logged in!!')
            return redirect("/home")
        else:
            return render(request, "login.html")
            messages.error(request, 'Document deleted.')

        log=Login(username=username,password=password)
        log.save()
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        fname = request.POST.get('firstName')
        lname = request.POST.get('lastName')
        phoneNo = request.POST.get('phoneNo')
        username = request.POST.get('username')
        password=request.POST.get('password')
        user = User(first_name=fname, last_name=lname, username=username)
        user.set_password(password)
        user.save()
        messages.success(request, 'You have successfully Registered!!')
        return redirect("/login")
    return render(request,"register.html")

def bill(request):
    return render(request,'bill.html')

def payment(request):
    return render(request,'payment.html')

def logoutuser(request):
    logout(request)
    return render(request,'landing.html')



def afterlogin(request):
    return render(request,'afterlogin.html')


def landing(request):
    return render(request,'landing.html')


def feedback(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        feedback = Feedback(user=request.user, rating=rating, comment=comment)
        feedback.save()
        return redirect('home')
    return render(request, 'feedback.html')




