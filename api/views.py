from django.shortcuts import render
from .serializers import JobSerializer,TrendingSerializer
from .models import Job,Trending,User
from rest_framework import generics,mixins,viewsets,status
from .serializers import RegisterSerializer
from rest_framework.response import Response
# Create your views here.

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()
    
class JobViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=JobSerializer
    queryset=Job.objects.all()

class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()
