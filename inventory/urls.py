from django.urls import path
from .views import ListCreateInventoryView, InventoryDetailView, ListCreateCheckNameView, ListCreateProductView, \
    ProductDetailView, getInventory

urlpatterns = [
    path('get-inventory/', getInventory.as_view(), name="getInventory-list-create"),
    path('inventory/', ListCreateInventoryView.as_view(), name="Inventory-list-create"),
    path('product/', ListCreateProductView.as_view(), name="Product-list-create"),

    path('check_name/', ListCreateCheckNameView.as_view(), name="checkname-list-view"),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name="Inventory-detail"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="Product-detail"),
]
