from Farms import views
from django.urls import path
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('farmer/', views.FarmerApi),
    path('farmer/<int:pk>/', views.FarmerApi),
    path('farm/', views.FarmApi),
    path('farm/<int:pk>/', views.FarmApi),
    path('farmer-login/', views.FarmerLoginApi),
    path('farmer-login/<int:pk>/', views.FarmerLoginApi),
    path('farmdata/', views.FarmDataApi),
    path('farmdata/<int:pk>/', views.FarmDataApi),
    path('wificreds/', views.FarmDataApi),
    path('wificreds/<int:pk>/', views.FarmDataApi),

]
