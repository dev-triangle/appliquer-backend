from dataclasses import fields
from pyexpat import model
from statistics import mode
from .models import Job,Trending
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields=['id','company_name','job_name','location','type','salary','duration','last_date']

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trending
        fields='__all__'
