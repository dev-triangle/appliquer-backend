from dataclasses import fields
from pyexpat import model
from statistics import mode
from .models import Job,Trending
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Job
        fields='__all__'

class TrendingSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=Trending
        fields='__all__'
