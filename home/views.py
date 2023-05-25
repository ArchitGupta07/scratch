from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Profiles,Projects,Gallery,Pcomments

from django.contrib.auth.models import User
from django.contrib.auth import logout, login
import datetime

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    

   

    profile = Profiles.objects.get(username = request.user)
    return render(request,'index.html',{'profile':profile})

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

    if request.method=='POST':
        username = request.user
        comment = request.POST.get('comment')
        print(comment)

        new_comment = Pcomments(username=username,comment=comment,date = datetime.date.today())
        new_comment.save()

    
    return render(request,'projects.html')




def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        location = request.POST.get('location')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        # description = request.POST.get('description')
        # username = request.POST.get('username')
        new_user = Profiles(first_name=first_name,last_name=last_name,username=username,location=location,password=password,email=email,image=image)
        new_user.save()
        user = User.objects.create_user(username=username,email=email, password=password)
        user.save()
       
        return redirect("/login")

    else:
         return render(request,'register.html')
def gallery(request):
    return render(request,'gallery.html')
def support(request):
    return render(request,'support.html')
def about(request):
    return render(request,'about.html')
def create_project(request):
    return render(request,'create_project.html')