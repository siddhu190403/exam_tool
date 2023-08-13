from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Testing,sample
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def helloDjango(request):
    samp = sample.objects.values_list('name').get(age=20)
    #Book.objects.values_list('title', flat=True).get(id=3)
    return render(request,'homepage.html',{'name':samp})

def searchpage(request):
    return render(request,'searchpage.html')

def LoginPage(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        password = request.POST.get("password")
        print(uname)
        print(password)
        a = auth.authenticate(username=uname,password=password)
        print(a)
        if a is not None:
            auth.login(request,a)
            return redirect('search/')
        else:
            messages.error(request,'Invalid username and password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def SignupPage(request):
    return render(request,'register.html')

def practicePage(request):
    test = Testing()
    test.price = 500
    test.desc = 'Just to check dynamic rendering'
    return render(request,'practice.html',{'price':test.price,'desc':test.desc})

def result(request):
    req = request.POST["search"]
    url = 'https://en.wikipedia.org/wiki/'+req
    r = requests.get(url)
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    res=""
    for para in soup.find_all("p"):
        res = res+para.get_text()

    return render(request,'result.html',{'result':res})

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        print(username)
        
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/login')
    else:
        return redirect('sign-up.html')

def Logout(request):
    auth.logout(request)
    return redirect('/login')