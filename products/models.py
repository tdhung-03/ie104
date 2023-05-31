from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    categories = models.ManyToManyField(Category, blank=True, related_name="products")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    price = models.IntegerField()
    brand = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/images')
    image_public_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
