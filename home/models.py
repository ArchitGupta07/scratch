from django.db import models
from django.contrib.auth.models import User
# Create your models here.   



class Profiles(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False,default='None')
    username = models.CharField(max_length=100,null=False)    
    password = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100, default='None')
    image = models.ImageField(upload_to="static/images",default='None')

    # friends = models.CharField(max_length=100,null=False,default='None')
    email = models.EmailField(default='None')
    
    

    def __str__(self):
        return self.first_name+" "+self.last_name
    


class Projects(models.Model):
    
    project_name = models.CharField(max_length=100, null=False)
    project_notes = models.CharField(max_length=500,default='None')
    p_image = models.ImageField(upload_to="images/",default='None')
    p_creator = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE,related_name='p_creator')

    project_link = models.URLField(null = True)
    liked = models.ManyToManyField(User, default = None, blank=True, related_name='liked')
    # likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.project_name
    
    @property
    def num_likes(self):
        return self.liked.all().count()

    # comments = models.CharField(max_length=100,default='None')
    # tags = models.CharField(max_length=100,default='None')
    

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
     
class Tags_projects(models.Model):
    
    p_tag_name = models.ForeignKey(Projects,null=True,on_delete=models.CASCADE)
    tag = models.CharField(max_length=100,null=False,default='None')
    
    
    def __str__(self):
        return str(self.p_tag_name)

 
class Favourites(models.Model):
    project_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    # project_creator = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)
    curator = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE)
    

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
     


# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
     
# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
     
# class Tags_projects(models.Model):
#      def __str__(self):
#             return self.first_name+" "+self.last_name
     

