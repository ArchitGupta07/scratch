from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from .models import Profiles,Projects,Gallery,Pcomments,Tags_projects,Favourites
from .models import Lovers

from django.contrib.auth.models import User
from django.db.models import F
from django.contrib.auth import logout, login
import datetime

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    profile = Profiles.objects.get(username = request.user) 
    project = Projects.objects.all()

    context ={
        'profile':profile,
        'project':project
        }    
    return render(request,'index.html',context)

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

def home(request):
   return render(request,'home.html')


def projects(request):  

    if request.method=='POST':
        
        comment = request.POST.get('comment')
        # print(comment)

        user_comment = request.user

        new_comment = Pcomments(username=user_comment,comment=comment,date = datetime.date.today())
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
    proj_gal = Projects.objects.all()
    context={
        'proj_gal':proj_gal
    }
    if 'fav' in request.POST: 
        # new_fav = Favourites(project_name = proj_ga;)

        
        return redirect("/gallery")
    


    return render(request,'gallery.html', context)


def support(request):
    return render(request,'support.html')
def about(request):
    return render(request,'about.html')



def create_project(request):
    if request.method=='POST':        

        project_name = request.POST.get('project_name')
        project_notes = request.POST.get('project_notes')
        project_link = request.POST.get('project_link')
        p_image = request.FILES.get('p_image')

        new_project = Projects(project_name=project_name,project_notes=project_notes,p_image=p_image,p_creator = request.user, project_link=project_link)
        new_project.save()
        return redirect('/')
    else:
        return render(request,'create_project.html')


def project_page(request,project_name):

    proj = Projects.objects.filter(project_name=project_name).first()
    print('Archit')
    comm = Pcomments.objects.filter(pname__project_name=project_name)   #Doubt Field ‘id’ expected a number but got ‘Free’  link - In this updated code, pname__project_name represents the lookup condition where project_name matches the project_name field in the related Projects object.Please make sure that the Pcomments model has a field named pname that refers to the Projects model using a ForeignKey or similar relationship. Additionally, ensure that project_name contains the desired project name value for the lookup.
    # print(comm)
    # print('Archit2')

    tagg = Tags_projects.objects.filter(p_tag_name__project_name = project_name)
    context = {
        'proj':proj,
        'comm':comm,
        'tagg':tagg
    }


   
    if 'com' in request.POST:       
        comment = request.POST.get('comment')
        # print(comment)

        p = Projects.objects.get(project_name=proj.project_name)
        print(p,' Archit')
        user_comment = request.user
        new_comment = Pcomments(username=user_comment,comment=comment,date = datetime.date.today(), pname = p)
        new_comment.save()

        return redirect(reverse('project_page', args=[project_name]))
    elif 'tags' in request.POST:
        tag = request.POST.get('tag')
        t = Projects.objects.get(project_name=proj.project_name)

        new_tag = Tags_projects(p_tag_name = t, tag=tag)
        new_tag.save()
        return redirect(reverse('project_page', args=[project_name]))        
    # here we finally solve the instance problem. So check it for future reference

    elif 'fav' in request.POST:
        f =  Projects.objects.get(project_name=proj.project_name)
        new_fav = Favourites(project_name = f, curator = request.user)
        new_fav.save()
        return redirect(reverse('project_page', args=[project_name]))
    
    elif 'like' in request.POST:
        l =  Projects.objects.get(project_name=proj.project_name)
        new_like = Lovers(p_name = l,lover = request.user )
        new_like.save()
        Projects.objects.filter(project_name=project_name).update(likes = F('likes')+1)
        return redirect(reverse('project_page', args=[project_name]))
    
    return render(request,'project_page.html', context)