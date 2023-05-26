from products.models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializerForProductList(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "rating", "price"]


class CategorySerializerForProduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializerForProduct(serializers.ModelSerializer):
    categories = CategorySerializerForProduct(many=True)

    class Meta:
        model = Product
        fields = ["categories", "name", "brand", "price", "rating", "description"]
