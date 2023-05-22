from django.db import models

# Create your models here.

class Profiles(models.Model):
    name = name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Projects(models.Model):
    project_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
class Gallery(models.Model):
    project_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
