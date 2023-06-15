from django.shortcuts import render, redirect, reverse
from django.db.models.functions import Random
from django.contrib.auth import authenticate
from .models import Profiles,Projects,Gallery,Pcomments,Tags_projects,Favourites,Featured
from .models import Lovers,Viewers,Downloaders, Friends,Gcomments,Activities

from django.contrib import messages
from home.templatetags import extras 
from django.db.models import Count

from django.contrib.auth.models import User
from django.db.models import F
from django.contrib.auth import logout, login
import datetime

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    # profile = Profiles.objects.get(username = request.user) 
    # project = Projects.objects.filter(p_creator = request.user)

    # context ={
    #     'profile':profile,
    #     'project':project
    #     }    
    # if 'view' in request.POST: 

    #     p = request.POST.get('proj_name')
    #     a = Projects.objects.get(project_name=p)
    #     print(p, 'check')
    #     user = request.user
        
        
    #     if user not in a.viewed.all():
    #         a.viewed.add(user)
    #         new_view = Viewers(pv_name = a, viewer = request.user)
    #         new_view.save()
    #         return redirect(reverse('project_page', args=[p]))
    #     else:            
    #         return redirect(reverse('project_page', args=[p]))
    s = Featured.objects.all()[:3]

    project_names = [entry.project_n for entry in s]

    d = Projects.objects.filter(project_name__in=project_names)

    random_row = Projects.objects.annotate(random_number=Random()).order_by('random_number').first()
    
    random_proj = Projects.objects.filter(p_creator = random_row.p_creator)
    context={
        'd':d,
        'random_row':random_row,
        'random_proj':random_proj
        
    }  
    if 'view' in request.POST: 

        p = request.POST.get('proj_name')
        a = Projects.objects.get(project_name=p)
        print(p, 'check')
        user = request.user
        
        
        if user not in a.viewed.all():
            a.viewed.add(user)
            new_view = Viewers(pv_name = a, viewer = request.user)
            new_view.save()
            return redirect(reverse('project_page', args=[p]))
        else:            
            return redirect(reverse('project_page', args=[p]))
    return render(request,'home.html', context)
    




def loginUser(request):

    if 'in' in request.POST:
        
            username = request.POST.get('username')
            password = request.POST.get('password')
            #check if user is using correct credentials

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
            else:
                return render(request,'login.html')
    if 'up' in request.POST:
        return redirect('/register')   

    return render(request,'login.html')





def logoutUser(request):
   logout(request)
   return redirect("/login")




def home(request):

    user1 = request.user
    your_projects = Projects.objects.filter(p_creator=user1)[:3]
   
    s = Featured.objects.all()[:4]

    project_names = [entry.project_n for entry in s]

    d = Projects.objects.filter(project_name__in=project_names)    
    
    random_row = Projects.objects.annotate(random_number=Random()).order_by('random_number').first()

    if random_row is not None:    
        random_proj = Projects.objects.filter(p_creator = random_row.p_creator)


    # ---------Activity-------------
    trending_proj = Projects.objects.annotate(num_like=Count('liked')).order_by('-num_like').first()


    all_active = Activities.objects.filter(status = True)[:3]
    personal = Activities.objects.all()[:3]   
    profile = Profiles.objects.get(username=request.user)

    # ---------Activity end-------------


    
    context={
        'd':d,
        'random_row':random_row,
        'random_proj':random_proj,
        'your_projects':your_projects,
        "all_active": all_active,
        "personal": personal,
        "profile": profile,
        "trending_proj": trending_proj
        
    }  
    if 'view' in request.POST: 

        p = request.POST.get('proj_name')
        a = Projects.objects.get(project_name=p)
        print(p, 'check')
        user = request.user
        
        
        if user not in a.viewed.all():
            a.viewed.add(user)
            new_view = Viewers(pv_name = a, viewer = request.user)
            new_view.save()
            return redirect(reverse('project_page', args=[p]))
        else:            
            return redirect(reverse('project_page', args=[p]))
    return render(request,'home.html', context)




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
    # proj_gal = Projects.objects.all()
    proj_gal = Projects.objects.all().exclude(p_creator = request.user)
    profile = Profiles.objects.get(username = request.user)
    gcomm = Gcomments.objects.all() 
    context={
        'proj_gal':proj_gal,
        'profile':profile,
        'gcomm':gcomm
    }
    if 'view' in request.POST: 

        p = request.POST.get('proj_name')
        a = Projects.objects.get(project_name=p)
        print(p, 'check')
        user = request.user
        
        
        if user not in a.viewed.all():
            a.viewed.add(user)
            new_view = Viewers(pv_name = a, viewer = request.user)
            new_view.save()
            return redirect(reverse('project_page', args=[p]))
        else:    
        
            return redirect(reverse('project_page', args=[p]))
    elif 'com' in request.POST:       
        comment = request.POST.get('comment')
        # print(comment)

        
        user_comment = request.user
        new_comment = Gcomments(username=user_comment,gcomment=comment,date = datetime.date.today())
        new_comment.save()
        return redirect('/gallery')
    


    return render(request,'gallery.html', context)





def support(request):
    return render(request,'support.html')



def about(request):
    return render(request,'about.html')


def activity(request):
    all_active = Activities.objects.filter(status = True)
    personal = Activities.objects.all()    
    profile = Profiles.objects.get(username=request.user)

    context = {
       "all_active": all_active,
       "personal": personal,
       "profile": profile
    }


    return render(request,'activity.html',context)





def create_project(request):
    if request.method=='POST':        

        project_name = request.POST.get('project_name')
        project_notes = request.POST.get('project_notes')
        project_link = request.POST.get('project_link')
        p_image = request.FILES.get('image')

        creator = request.user

        new_project = Projects(project_name=project_name,project_notes=project_notes,p_image=p_image,p_creator = request.user, project_link=project_link)
        new_project.save()

        print(new_project.project_name)

        proj_created = Projects.objects.get(project_name = new_project.project_name)

        # above proj_created is written because below new activity was gven error : - Activities.project_involved must be a Projects instance


        act = str(creator) + " " + "created a project called "+ str(project_name)
        new_activity = Activities(activity=act,project_involved = proj_created,user_involved = request.user,status = False)
        new_activity.save()






        return redirect('/')
    else:
        return render(request,'create_project.html')





def project_page(request,project_name):

    proj = Projects.objects.get(project_name=project_name)
    print('Archit')
    comm = Pcomments.objects.filter(pname__project_name=project_name, parent = None)   #Doubt Field ‘id’ expected a number but got ‘Free’  link - In this updated code, pname__project_name represents the lookup condition where project_name matches the project_name field in the related Projects object.Please make sure that the Pcomments model has a field named pname that refers to the Projects model using a ForeignKey or similar relationship. Additionally, ensure that project_name contains the desired project name value for the lookup.
    # print(comm)
    # print('Archit2')
    # prof = Profiles.objects.filter(username=request.user).first()

    replies = Pcomments.objects.filter(pname__project_name=project_name).exclude(parent=None)  

    replydict = {}
    for reply in replies:
        if reply.parent.id  not in replydict.keys():
            replydict[reply.parent.id] = [reply]
        else:
            replydict[reply.parent.id].append(reply)
    
    print(replydict)


    tagg = Tags_projects.objects.filter(p_tag_name__project_name = project_name)


    profile = Profiles.objects.get(username=proj.p_creator)
    current_user = request.user




    context = {
        'proj':proj,
        # 'prof':prof,
        'comm':comm,
        'tagg':tagg,
        'replies':replies,
        'replydict':replydict,
        'profile':profile,
        'current_user':current_user
    }


   
    if 'com' in request.POST:       
        comment = request.POST.get('comment')
        # print(comment)

        p = Projects.objects.get(project_name=proj.project_name)
        print(p,' Archit')
        user_comment = request.user
        

        parentSno = request.POST.get('parent_id')

        if parentSno == "":
            new_comment = Pcomments(username=user_comment,comment=comment, pname = p)
            new_comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else :
            parent = Pcomments.objects.get(id = parentSno)
            new_comment = Pcomments(username=user_comment,comment=comment, pname = p, parent = parent)
            new_comment.save()
            messages.success(request, "Your Reply has been posted successfully")


       

        return redirect(reverse('project_page', args=[project_name]))
    
    
    
    elif 'tags' in request.POST:
        tag = request.POST.get('tag')
        t = Projects.objects.get(project_name=proj.project_name)       
        user = request.user
                
        if user not in t.tagged.all():
            t.tagged.add(user)          

        new_tag = Tags_projects(p_tag_name = t, tag=tag)
        new_tag.save()
        return redirect(reverse('project_page', args=[project_name]))        
    # here we finally solve the instance problem. So check it for future reference

    elif 'fav' in request.POST:
        f =  Projects.objects.get(project_name=proj.project_name)
        new_fav = Favourites(project_name = f, favorby = request.user)
        new_fav.save()
        return redirect(reverse('project_page', args=[project_name]))
    
    elif 'like' in request.POST:

        # -----activity----

        act = str(proj.p_creator) + " " + "liked project "+ str(project_name)
        new_activity = Activities(activity=act,project_involved = proj,user_involved = proj.p_creator,status = False)
        new_activity.save()
        # -----activity----





    
        user = request.user
        l =  Projects.objects.get(project_name=proj.project_name)
        
        if user in l.liked.all():
            l.liked.remove(user)
        else:
            l.liked.add(user)

        like, created = Lovers.objects.get_or_create(lover=user,p_name = l)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:like.value = 'Like'         
        return redirect(reverse('project_page', args=[project_name]))
    
    elif 'follow' in request.POST:
        user = request.user

        
        f =  Profiles.objects.get(username=proj.p_creator)
        
        if user in f.follows.all():
            f.follows.remove(user)
        else:
            f.follows.add(user)


        # -----activity----

            act_follow = str(user) + " " + "started following you"
            new_activity = Activities(activity=act_follow,user_involved = user,status = False)
            new_activity.save()
        # -----activity----
            

        # like, created = Lovers.objects.get_or_create(lover=user,p_name = l)

        # if not created:
        #     if like.value == 'Like':
        #         like.value = 'Unlike'
        #     else:like.value = 'Like'         
        return redirect(reverse('project_page', args=[project_name]))
    

    elif 'down' in request.POST:
        
        a = Projects.objects.get(project_name=proj.project_name)
        
        user = request.user
        print('Archit2')
        
        if user not in a.downloaded.all():
            print('t')
            a.downloaded.add(user)
            new_down = Downloaders(pd_name = a, downloader = request.user)
            new_down.save()
            
            return redirect(reverse('project_page', args=[project_name]))
    
    return render(request,'project_page.html', context)