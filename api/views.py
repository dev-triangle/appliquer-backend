import stat
from django.shortcuts import render
from .serializers import JobSerializer,RegisterSerializer,TrendingSerializer,UserDetailSerializer,ApplicationSerializer
from .models import Job,Trending,User,UserDetail,Application
from rest_framework import generics,mixins,viewsets,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
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

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

