from django.db import models


class Farmer(models.Model):
    # farmer
    name = models.CharField(max_length=255, null=False)
    age = models.CharField(max_length=255, null=False)
    national_id = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} ({})".format(self.name, self.national_id)



class Farm(models.Model):
    # course
    name = models.CharField(max_length=255, null=False)
    size = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} ({})".format(self.name, self.location)



class FarmData(models.Model):
    # farm data
    temperature = models.CharField(max_length=255, null=True)
    humidity = models.CharField(max_length=255, null=True)
    moisture = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "H({}) M({}) T({})".format(self.humidity, self.moisture, self.temperature)


class WifiCredential(models.Model):
    # farm data
    sensor_id = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)



    def __str__(self):
        return "({}) User-({}) pass-({}) ".format(self.sensor_id, self.username, self.password)


