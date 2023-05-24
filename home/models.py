from django.db import models

# Create your models here.


    

class Projects(models.Model):
    project_name = models.CharField(max_length=100, null=False)
    project_notes = models.CharField(max_length=500,default='None')
    comments = models.CharField(max_length=100,default='None')
    tags = models.CharField(max_length=100,default='None')
    


    def __str__(self):
        return self.project_name
class Gallery(models.Model):
    project_name = models.ForeignKey(Projects,max_length=100, null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name

class Profiles(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False,default='None')
    username = models.CharField(max_length=100,null=False,default='None')
    
    password = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100, default='None')

    # friends = models.CharField(max_length=100,null=False,default='None')
    email = models.EmailField(default='None')
    

    def __str__(self):
        return self.first_name+" "+self.last_name
