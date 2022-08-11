import stat
from django.shortcuts import render
from .serializers import JobSerializer,LogoutSerializer,TrendingSerializer,UserDetailSerializer,ApplicationSerializer
from .models import Job,Trending,User,UserDetail,Application
from rest_framework import generics,mixins,viewsets,status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()
    
class JobViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,):
    serializer_class=JobSerializer
    queryset=Job.objects.all() 
    
class TrendingViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=TrendingSerializer
    queryset=Trending.objects.all()

class UserDetailViewset(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=UserDetailSerializer
    queryset=UserDetail.objects.all()

class ApplicationViewset(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=ApplicationSerializer
    queryset=Application.objects.all()

class LogoutAuth(generics.GenericAPIView):
    serializer_class=LogoutSerializer
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

