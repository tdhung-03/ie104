from products.models import *
from rest_framework import serializers


class ProductSerializerForProductList(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "rating", "price", "image_public_id"]


class CategorySerializerForProductDetail(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializerForProductDetail(serializers.ModelSerializer):
    categories = CategorySerializerForProductDetail(many=True)

    class Meta:
        model = Product
        fields = ["categories", "name", "brand", "price", "rating", "description", "image_public_id"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductBasedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'rating', 'price', "image_public_id"]


class CategoryForQuerySerializer(serializers.ModelSerializer):
    products = ProductBasedCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'products']
