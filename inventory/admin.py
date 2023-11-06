from django.contrib import admin


from .models import Inventory, Product, MyIngredient
# Register your models here.
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(MyIngredient)
