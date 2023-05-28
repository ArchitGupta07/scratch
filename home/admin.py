from django.contrib import admin
from .models import Profiles,Projects,Gallery,Pcomments,Tags_projects,Favourites,Lovers,Viewers,Featured
from .models import Projects_text,Downloaders,Friends

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Projects)
admin.site.register(Gallery)
admin.site.register(Pcomments)
admin.site.register(Tags_projects)
admin.site.register(Favourites)
admin.site.register(Lovers)
admin.site.register(Viewers)
admin.site.register(Featured)
admin.site.register(Projects_text)
admin.site.register(Downloaders)
admin.site.register(Friends)