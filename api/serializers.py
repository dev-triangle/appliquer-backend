from dataclasses import fields
import email
from statistics import mode
from rest_framework import serializers
from .models import Job,Trending
from rest_framework.permissions import IsAuthenticated
from .models import User,UserDetail,Application
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)

    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']
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

class UserDetailSerializer(serializers.ModelSerializer):
    # profile_photo=serializers.ImageField(max_length=None,allow_empty_file=True,use_url=True,required=False)
    class Meta:
        model=UserDetail
        fields='__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=['user_foreign','job_foreign','date_of_application','username']

