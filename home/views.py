from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.contrib.auth import logout, login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):

    if 'in' in request.POST:
        
            username = request.POST.get('username')
            password = request.POST.get('password')
            #check if user is using correct credentials

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request,'login.html')
    if 'up' in request.POST:
        return redirect('/register')

        

    return render(request,'login.html')

def logoutUser(request):
   logout(request)
   return redirect("/login")


def projects(request):
    return render(request,'projects.html')
def register(request):
    return render(request,'register.html')
def gallery(request):
    return render(request,'gallery.html')
def support(request):
    return render(request,'support.html')
def about(request):
    return render(request,'about.html')