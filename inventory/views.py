import datetime

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


from .models import Inventory, Product
from .serializers import InventorySerializer, ProductSerializer
from .decorators import validate_inventory_data, validate_product_data


# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class ListCreateCheckNameView(generics.ListCreateAPIView):
    """
        GET Chats/
        POST Chats/
        """


    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        # tag_instance = Chats.objects.get()
        # a_pattern = ChatsSerializer.objects.create(
        #     name=request.data["name"]
        # )
        # Test the chatbot
        res=Inventory.objects.filter(inventory=request.data["inventory"])
        inventory = res.first()

        s = InventorySerializer(inventory)
        return Response(
            data=s.data,
            status=status.HTTP_201_CREATED
        )
@method_decorator(csrf_exempt, name='dispatch')
class ListCreateInventoryView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_inventory_data
    def post(self, request, *args, **kwargs):
        a_tag = Inventory.objects.create(
            product=Product.objects.get(id=request.data["product"]),
            quantity=request.data["quantity"],
            units=request.data["units"],
            price=request.data["price"],

        )
        return Response(
            data=InventorySerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class InventoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_inventory = self.queryset.get(pk=kwargs["pk"])
            return Response(InventorySerializer(a_inventory).data)
        except Inventory.DoesNotExist:
            return Response(
                data={
                    "message": "Inventory with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_inventory_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = InventorySerializer()
            updated_inventory = serializer.update(a_tag, request.data)
            return Response(InventorySerializer(updated_inventory).data)
        except Inventory.DoesNotExist:
            return Response(
                data={
                    "message": "Inventory with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_inventory = self.queryset.get(pk=kwargs["pk"])
            a_inventory.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Inventory.DoesNotExist:
            return Response(
                data={
                    "message": "Inventory with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    

@method_decorator(csrf_exempt, name='dispatch')
class ListCreateProductView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_product_data
    def post(self, request, *args, **kwargs):
        a_tag = Product.objects.create(
            name=request.data["name"],
            description=request.data["description"],
            category=request.data["category"],
            price=request.data["price"],
            date=request.data["date"],
            images=request.data["images"],


        )
        return Response(
            data=ProductSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            return Response(ProductSerializer(a_product).data)
        except Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_product_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = ProductSerializer()
            updated_product = serializer.update(a_tag, request.data)
            return Response(ProductSerializer(updated_product).data)
        except Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            a_product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(
                data={
                    "message": "Product with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    



class getInventory(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_inventory_data
    def post(self, request, *args, **kwargs):
        obj = request.data["obj"]

        if str(obj)=="today":
            inventory_today = Inventory.objects.filter(date__date=datetime.date.today())
        elif str(obj)=="history":
            inventory_today = Inventory.objects.all()

        return Response(
            data=[{
                "product_obj": ProductSerializer(Product.objects.get(id=item["product"])).data,
                **item,
            } for item in InventorySerializer(inventory_today, many=True).data],
                status=status.HTTP_201_CREATED
        )

