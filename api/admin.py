from django.contrib import admin
from .models import Job,Trending,User,UserDetail,Application
# Register your models here.
admin.site.register(Job)
admin.site.register(Trending)
admin.site.register(User)
admin.site.register(UserDetail)
admin.site.register(Application)
