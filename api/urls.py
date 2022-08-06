from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet,TrendingViewSet,RegisterView
router=DefaultRouter()
router.register('jobs',JobViewSet, basename='jobs')
router.register('trending',TrendingViewSet,basename='trending')
router.register('register',RegisterView,basename='register')
urlpatterns = [
    path('',include(router.urls)),
]