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


from .models import Calender
from .serializers import CalenderSerializer
from .decorators import validate_calender_data


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateCalenderView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_calender_data
    def post(self, request, *args, **kwargs):
        a_tag = Calender.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            images=request.data["images"],


        )
        return Response(
            data=CalenderSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class CalenderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_calender = self.queryset.get(pk=kwargs["pk"])
            return Response(CalenderSerializer(a_calender).data)
        except Calender.DoesNotExist:
            return Response(
                data={
                    "message": "Calender with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_calender_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = CalenderSerializer()
            updated_calender = serializer.update(a_tag, request.data)
            return Response(CalenderSerializer(updated_calender).data)
        except Calender.DoesNotExist:
            return Response(
                data={
                    "message": "Calender with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_calender = self.queryset.get(pk=kwargs["pk"])
            a_calender.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Calender.DoesNotExist:
            return Response(
                data={
                    "message": "Calender with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
