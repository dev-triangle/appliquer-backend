from django.shortcuts import render
from .serializers import JobSerializer,TrendingSerializer
from .models import Job,Trending,User
from rest_framework import generics,mixins,viewsets,status
from .serializers import RegisterSerializer
from rest_framework.response import Response
# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self,request):
        user=request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data=serializer.data
        return Response(user_data,status=status.HTTP_201_CREATED)

class JobViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class=JobSerializer
    queryset=Job.objects.all()

class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()
