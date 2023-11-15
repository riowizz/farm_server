from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect


from .models import Recommendation
from .serializers import RecommendationSerializer
from .decorators import validate_recommendation_data


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateRecommendationView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_recommendation_data
    def post(self, request, *args, **kwargs):
        a_tag = Recommendation.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            images=request.data["images"],


        )
        return Response(
            data=RecommendationSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class RecommendationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_recommendation = self.queryset.get(pk=kwargs["pk"])
            return Response(RecommendationSerializer(a_recommendation).data)
        except Recommendation.DoesNotExist:
            return Response(
                data={
                    "message": "Recommendation with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_recommendation_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = RecommendationSerializer()
            updated_recommendation = serializer.update(a_tag, request.data)
            return Response(RecommendationSerializer(updated_recommendation).data)
        except Recommendation.DoesNotExist:
            return Response(
                data={
                    "message": "Recommendation with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_recommendation = self.queryset.get(pk=kwargs["pk"])
            a_recommendation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Recommendation.DoesNotExist:
            return Response(
                data={
                    "message": "Recommendation with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
