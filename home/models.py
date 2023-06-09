from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
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
    
    username = models.ForeignKey(User,max_length=100,null=False,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000,default='None')
    date = models.DateField()
    pname = models.ForeignKey(Projects,on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return str(self.username)
    
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
     friend = models.ForeignKey(Profiles,max_length=100, null=True,on_delete=models.CASCADE)
     friend_s = models.ForeignKey(User,max_length=100, null=True,on_delete=models.CASCADE)
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
     

