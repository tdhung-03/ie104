from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    categories = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.name
