from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet,TrendingViewSet
router=DefaultRouter()
router.register('jobs',JobViewSet, basename='jobs')
router.register('trending',TrendingViewSet,basename='trending')
urlpatterns = [
    path('',include(router.urls)),
]