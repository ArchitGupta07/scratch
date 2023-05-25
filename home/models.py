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
    p_creator = models.ForeignKey(User,max_length=100,null=True,on_delete=models.CASCADE)
    
    # comments = models.CharField(max_length=100,default='None')
    # tags = models.CharField(max_length=100,default='None')
    def __str__(self):
        return self.project_name

class Gallery(models.Model):
    project_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

class Pcomments(models.Model):
    username = models.ForeignKey(User,max_length=100,null=False,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000,default='None')
    date = models.DateField()
    
    def __str__(self):
        return str(self.username)
     

class Tags_projects(models.Model):
     project_name = models.ForeignKey(Projects,null=True,on_delete=models.CASCADE)

     tag = models.CharField(max_length=100,null=False,default='None')
     def __str__(self):
            return self.project_name
     










class Tags_projects(models.Model):
     def __str__(self):
            return self.first_name+" "+self.last_name
     
class Tags_projects(models.Model):
     def __str__(self):
            return self.first_name+" "+self.last_name
     
class Tags_projects(models.Model):
     def __str__(self):
            return self.first_name+" "+self.last_name
     
class Tags_projects(models.Model):
     def __str__(self):
            return self.first_name+" "+self.last_name
     
class Tags_projects(models.Model):
     def __str__(self):
            return self.first_name+" "+self.last_name
     

