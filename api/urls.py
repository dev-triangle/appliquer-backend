from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import JobViewSet,TrendingViewSet,RegisterView,UserDetailViewset,BlacklistTokenView,ApplicationViewset,LoggedInUserView
router=DefaultRouter()
router.register('jobs',JobViewSet, basename='jobs')
router.register('trending',TrendingViewSet,basename='trending')
router.register('register',RegisterView,basename='register')
router.register('user-detail',UserDetailViewset,basename='user-detail')
router.register('application',ApplicationViewset,basename='application')
# router.register('current-user',LoggedInUserView,basename='current-user')
urlpatterns = [
    path('',include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),

]