from django.shortcuts import render
from .serializers import JobSerializer,TrendingSerializer
from .models import Job,Trending,User
from rest_framework import generics,mixins,viewsets,status
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()
    
class JobViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,):
    permission_classes=[IsAuthenticated]
    serializer_class=JobSerializer
    queryset=Job.objects.all()
    
    
class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()
