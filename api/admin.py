from django.contrib import admin
from .models import Job,Trending
from .models import User
# Register your models here.
admin.site.register(Job)
admin.site.register(Trending)
admin.site.register(User)