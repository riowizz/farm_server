from django.urls import path
from .views import ListCreateRecommendationView, RecommendationDetailView

urlpatterns = [
    path('recommendation/', ListCreateRecommendationView.as_view(), name="Recommendation-list-create"),
    path('recommendation/<int:pk>/', RecommendationDetailView.as_view(), name="Recommendation-detail"),
    
]
