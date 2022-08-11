from distutils.command.upload import upload
import email
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
# Create your models here.
TYPE_CHOICES = (
   ('Intern', 'Intern'),
   ('Full-Time', 'Full-time'),
   ('Part-Time','Part-time')
)
class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        # user=self.create_user(username,email,password)
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''

class Job(models.Model):
    company_name=models.CharField(max_length=100)
    job_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    type=models.CharField(choices=TYPE_CHOICES, max_length=128)
    salary=models.FloatField()
    duration=models.IntegerField(null=True,blank=True)
    last_date=models.DateField()
    image=models.ImageField(upload_to='job_images',blank=True,null=True)
    reqs=models.CharField(max_length=200,blank=True,null=True)
    desc=models.TextField(max_length=300,blank=True,null=True)
    

    def __str__(self):
        return (self.company_name)

class Trending(models.Model):
    company_name=models.CharField(max_length=100)
    job_name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images',blank=True,null=True)

    def __str__(self):
        return (self.company_name)

class UserDetail(models.Model):
    skillset= models.CharField(max_length=250)
    experience=models.CharField(max_length=250)
    name=models.CharField(max_length=100)
    projects=models.CharField(max_length=250)
    description=models.CharField(max_length=500)
    user_foreign=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return(self.name)
        




