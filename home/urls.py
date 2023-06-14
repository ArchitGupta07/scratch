from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('projects', views.projects, name="projects"),
    path('gallery', views.gallery, name="gallery"),
    path('support', views.support, name="support"),
    path('about', views.about, name="about"),
    path('register', views.register, name="register"),
    path('activity', views.activity, name="activity"),
    path('create_project', views.create_project, name="create_project"),
    path('project_page/<str:project_name>', views.project_page, name="project_page"),

]
