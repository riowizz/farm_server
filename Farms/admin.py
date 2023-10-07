from django.contrib import admin
from .models import Farmer, Farm, FarmData

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Farm)
admin.site.register(FarmData)
