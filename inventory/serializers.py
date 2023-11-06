from django.forms import model_to_dict
from rest_framework import serializers

from .models import Inventory, Product, MyIngredient


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
        # image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
        # fields = ["id", "name", "description", "category", "quantity", "date", "price", "images"]

    def update(self, instance, validated_data):
        instance.product = validated_data.get("product", instance.product)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.units = validated_data.get("units", instance.units)
        instance.date = validated_data.get("date", instance.date)
        instance.price = validated_data.get("price", instance.price)

    #
        instance.save()
        return instance


class MyIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyIngredient
        fields = "__all__"
        # image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
        # fields = ["id", "name"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)

    #
        instance.save()
        return instance





class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        images = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
        # fields = ["id", "name", "description", "price", "category", "date", "images"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.category = validated_data.get("category", instance.category)
        instance.price = validated_data.get("price", instance.price)
        instance.date = validated_data.get("date", instance.date)
        instance.images = validated_data.get("images", instance.images)

    #
        instance.save()
        return instance





