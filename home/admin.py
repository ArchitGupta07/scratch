from django.contrib import admin
from .models import Profiles,Projects,Gallery,Pcomments,Tags_projects

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Projects)
admin.site.register(Gallery)
admin.site.register(Pcomments)
admin.site.register(Tags_projects)