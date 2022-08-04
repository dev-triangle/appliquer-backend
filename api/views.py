from django.shortcuts import render
from .serializers import JobSerializer,TrendingSerializer
from .models import Job,Trending
from rest_framework import generics,mixins,viewsets
# Create your views here.
class JobViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=JobSerializer
    queryset=Job.objects.all()

class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()
