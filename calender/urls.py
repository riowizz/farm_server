from django.urls import path
from .views import ListCreateCalenderView, CalenderDetailView

urlpatterns = [
    path('calender/', ListCreateCalenderView.as_view(), name="Calender-list-create"),
    path('calender/<int:pk>/', CalenderDetailView.as_view(), name="Calender-detail"),
    
]
