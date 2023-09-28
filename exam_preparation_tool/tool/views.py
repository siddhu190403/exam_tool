from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Testing,sample,History
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages
from django.template import loader
from googlesearch import search
from .summarize import summarize_text,summarize
from .searchresults import searchresults,recomendvideos,extractlink
from .scrapecontent import generatequestion


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

def result(request):
    req = request.POST["search"]
    marks = int(request.POST["mark"])
    if marks > 2:
        marks = marks*2
    
    question = generatequestion(req)

    #get links
    #link = searchresults(req)
    search_url=""

    url = 'https://en.wikipedia.org/wiki/'+req

    #add record in history
    name = User.objects.values_list('username').get(id = request.user.id)
    hist = History(uid=request.user.id,name=name,history=req)
    hist.save()
    # Parsing the HTML

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    res=""
    for para in soup.find_all("p"):
        res = res+para.get_text()
    
    for r in res:
        if r.isnumeric() or r is '[' or r is ']':\
            res = res.replace(r,' ')

    final_result = summarize_text(res,marks)
    print("final_result : \n"+final_result)

    return render(request,'result.html',{'result':final_result,'questions':question,'topic':req})

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

def ViewHistory(request):
    history = []
    histories = History.objects.all()
    for his in histories:
        if his.uid == request.user.id:
            history.append(his.history)
    print(history)
    return render(request,'history.html',{'hist':history})

def GetLinks(request):

    if request.method == 'POST':
        # Define the search query
        query = request.POST["query"]

        link = searchresults(query)

        return render(request,'links.html',{'links':link,'query':query,'videos':recomendvideos(query),'video_link':extractlink(recomendvideos(query))})
    else:
        return render(request,'links.html')