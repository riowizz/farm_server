from django.forms import model_to_dict
from rest_framework import serializers

from .models import Farmer, Farm, FarmData, WifiCredential


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = "__all__"
        # fields = ["id", "name", "age", "national_id", "address", "email"]

    # def update(self, instance, validated_data):
    #     instance.course_code = validated_data.get("course_code", instance.course_code)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.years = validated_data.get("years", instance.years)
    #     instance.sem_count = validated_data.get("sem_count", instance.sem_count)
    #
    #     instance.save()
    #     return instance



class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        farmer = FarmerSerializer
        fields = "__all__"
        # fields = ["id", "name", "size", "location", "farmer"]

    # def update(self, instance, validated_data):
    #     instance.course_code = validated_data.get("course_code", instance.course_code)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.years = validated_data.get("years", instance.years)
    #     instance.sem_count = validated_data.get("sem_count", instance.sem_count)
    #
    #     instance.save()
    #     return instance


class FarmDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmData
        fields = "__all__"
        # fields = ["id", "name", "size", "location", "farmer"]

    # def update(self, instance, validated_data):
    #     instance.course_code = validated_data.get("course_code", instance.course_code)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.years = validated_data.get("years", instance.years)
    #     instance.sem_count = validated_data.get("sem_count", instance.sem_count)
    #
    #     instance.save()
    #     return instance


class WifiCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = WifiCredential
        fields = "__all__"
        # fields = ["id", "name", "size", "location", "farmer"]

    # def update(self, instance, validated_data):
    #     instance.course_code = validated_data.get("course_code", instance.course_code)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.years = validated_data.get("years", instance.years)
    #     instance.sem_count = validated_data.get("sem_count", instance.sem_count)
    #
    #     instance.save()
    #     return instance



