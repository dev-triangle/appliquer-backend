from dataclasses import fields
import email
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
    class Meta:
        model=UserDetail
        fields='__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'

class LogoutSerializer(serializers.ModelSerializer):
    refresh=serializers.CharField()

    def validate(self,attrs):
        self.token=attrs['refresh']
        return attrs

    def save(self,**kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')