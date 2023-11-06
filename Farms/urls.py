from django.conf.urls import url
from Farms import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^farmer$', views.FarmerApi),
    url(r'^farmer/([0-9]+)$', views.FarmerApi),
    url(r'^farm$', views.FarmApi),
    url(r'^farm/([0-9]+)$', views.FarmApi),
    url(r'^farmer-login$', views.FarmerLoginApi),
    url(r'^farmer-login/([0-9]+)$', views.FarmerLoginApi),
    url(r'^farmdata$', views.FarmDataApi),
    url(r'^farmdata/([0-9]+)$', views.FarmDataApi),
    url(r'^wificreds$', views.FarmDataApi),
    url(r'^wificreds/([0-9]+)$', views.FarmDataApi),

]
