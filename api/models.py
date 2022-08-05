from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
# Create your models here.
TYPE_CHOICES = (
   ('I', 'Intern'),
   ('F', 'Full-time'),
   ('P','Part-time')
)


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






