from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.timezone import now
# Create your models here.   




    


class Projects(models.Model):
    
    project_name = models.CharField(max_length=100, null=False)
    project_notes = models.CharField(max_length=500,default='None')
   
    p_image = CloudinaryField('image')
    p_creator = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE,related_name='p_creator')
    date = models.DateField(null=True,default=None)
    project_link = models.URLField(null = True)
    liked = models.ManyToManyField(User, default = None, blank=True, related_name='liked')
    viewed = models.ManyToManyField(User, default = None, blank=True, related_name='viewed')
    downloaded = models.ManyToManyField(User, default = None, blank=True, related_name='downloaded')
    tagged = models.ManyToManyField(User, default = None, blank=True, related_name='tagged')
    # likes = models.IntegerField(default=0)


    # Tip:- use USER in foreign key if you wanted use the current user of a particular page. This will save you from errors like " Field 'id' expected a number "
    
    def __str__(self):
        return self.project_name
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    @property
    def num_down(self):
        return self.downloaded.all().count()
    
    @property
    def num_tags(self):
        return self.tagged.all().count()
    
    @property
    def num_views(self):
        return self.viewed.all().count()

    # comments = models.CharField(max_length=100,default='None')
    # tags = models.CharField(max_length=100,default='None')

    
class Profiles(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False,default='None')
    father = models.CharField(max_length=100,null=False,default='None')
    username = models.CharField(max_length=100,null=False)    
    password = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100, default='None')
   
    image = CloudinaryField('image')

    # friends = models.CharField(max_length=100,null=False,default='None')
    email = models.EmailField(default='None')
    friend = models.ManyToManyField(User, default = None, blank=True, related_name='friend')
    proj_created = models.ManyToManyField(Projects, default = None, blank=True, related_name='proj_created')
    

    def __str__(self):
        return self.first_name+" "+self.last_name
    

class Gallery(models.Model):
    project_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.project_name

class Pcomments(models.Model):
    
    id = models.AutoField(primary_key=True)    
    username = models.ForeignKey(User,max_length=100,null=False,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000,default='None')
    
    pname = models.ForeignKey(Projects,on_delete=models.CASCADE,default=None)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)    
    #   in above line we used 'self' as we wanted to make itself the foreign key
    date = models.DateTimeField(default=now)

    
    def __str__(self):
        return str(self.username) + " " + str(self.comment)
    
class Gcomments(models.Model):
    
    username = models.ForeignKey(User,max_length=100,null=False,on_delete=models.CASCADE)
    gcomment = models.CharField(max_length=1000,default='None')
    date = models.DateField()
    # pname = models.ForeignKey(Projects,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return str(self.username)
     
class Tags_projects(models.Model):
    
    p_tag_name = models.ForeignKey(Projects,null=True,on_delete=models.CASCADE)
    tag = models.CharField(max_length=100,null=False,default='None')
    tagger = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE, default=None)
    
    
    def __str__(self):
        return str(self.p_tag_name)

 
class Favourites(models.Model):
    project_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    # project_creator = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    favorby = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.project_name)



LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')

)
class Lovers(models.Model):
    p_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    lover = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)
     
    def __str__(self):
            return str(self.lover)+ " " + str(self.p_name)
    

     
class Viewers(models.Model):
    pv_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    viewer =  models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE)
    def __str__(self):
            return str(self.pv_name)+ " " + str(self.viewer)
     

class Featured(models.Model):
    project_n = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE, related_name = 'project_n')
    # creator = models.ForeignKey(Profiles,max_length=100, null=True,on_delete=models.CASCADE, related_name='creator')

    def __str__(self):
            return str(self.project_n)

class Projects_text(models.Model):
     def __str__(self):
            return self.first_name+" "+self.last_name
     

class Downloaders(models.Model):
    pd_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    downloader =  models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE)     

    def __str__(self):
            return str(self.pd_name)+ " " + str(self.downloader)
    

class Friends(models.Model):
     
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="user", default=None )    
    friends = models.ManyToManyField(User, blank=True, related_name="friends")



    def __str__(self):
        return self.user.username
    
    def add_friend(self,account):
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()
    

    def remove_friend(self,account):
         

         if account in self.friends.all():
              self.friends.remove(account)
     
    def unfriend(self,removee):
         

         #person terminating the friendship

         remover_friend_list = self        

         remover_friend_list.remove_friend(removee)

         friends_list = Friends.objects.get(user = removee)

         friends_list.remove_friend(self.user)
    

    def is_mutual_friend(self,friend):
         

         if friend in self.friends.all():
              return True
         return False

class FriendRequest(models.Model):
     
     sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name="sender")
     reciever = models.ForeignKey(User,on_delete=models.CASCADE, related_name="reciever")

     is_active = models.BooleanField(blank=True,null=False,default=True)
     timestamp = models.DateTimeField(auto_now_add = True)

     def __str__(self) :
          return self.sender.username
     

     def accept(self):
          
          reciever_friend_list = Friends.objects.get(user= self.reciever)

          if reciever_friend_list:
               reciever_friend_list.add_friend(self.sender)
               sender_friend_list = Friends.objects.get(user = self.sender)

               if sender_friend_list:
                    sender_friend_list.add_friend(self.reciever)
                    self.is_active = False
                    self.save()

     def decline(self):
          
          self.is_active = False
          self.save()
     
     def cancel(self):
          

          self.is_active = False
          self.save()
               
     
class Followers(models.Model):
    def __str__(self):
        return self.first_name+" "+self.last_name
     




         



# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
     
# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
     
# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
     

