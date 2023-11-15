from Farms import views
from django.urls import path
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path(r'^farmer$', views.FarmerApi),
    path(r'^farmer/([0-9]+)$', views.FarmerApi),
    path(r'^farm$', views.FarmApi),
    path(r'^farm/([0-9]+)$', views.FarmApi),
    path(r'^farmer-login$', views.FarmerLoginApi),
    path(r'^farmer-login/([0-9]+)$', views.FarmerLoginApi),
    path(r'^farmdata$', views.FarmDataApi),
    path(r'^farmdata/([0-9]+)$', views.FarmDataApi),
    path(r'^wificreds$', views.FarmDataApi),
    path(r'^wificreds/([0-9]+)$', views.FarmDataApi),

]
