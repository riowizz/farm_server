from django.db import models
import os

def upload_to_images(instance, filename):
    # Define the directory where the image will be uploaded
    upload_directory = "static/images"

    # Get the filename extension from the uploaded file
    # extension = os.path.splitext(filename)[1]

    # Construct the final path using the model's primary key and the filename
    # print(f"instance: {instance.pk}")
    # print(f"extension: {extension}")
    final_filename = f"{filename}"
    return os.path.join(upload_directory, final_filename)



class Product(models.Model):
    # product
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    category = models.CharField(max_length=255, null=False)
    units = models.CharField(max_length=255, null=False, default="Kgs")
    price = models.IntegerField(null=False)
    frequent_quantities = models.CharField(max_length=255, null=False, default="1, 2, 3")
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to=upload_to_images, blank=True)



    def __str__(self):
        return "{}. ({})".format(self.name, self.category)




class Inventory(models.Model):
    # inventory
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(null=False)
    units = models.CharField(default='Kgs', max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=False)



    def __str__(self):
        return "{}. ({}{}) @ {}".format(self.product, self.quantity, self.units, self.price)


class MyIngredient(models.Model):
    # ingredient
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}".format(self.name)



