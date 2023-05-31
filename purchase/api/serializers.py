from rest_framework import serializers
from products.models import *
from purchase.models import *
from users.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartDetail
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    CartDetails = CartDetailSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'created_at', 'CartDetails']


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity', 'sub_price']


class OrderSerializer(serializers.ModelSerializer):
    OrderDetails = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'owner', 'created_at', 'total_price', 'OrderDetails']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProductForCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "image_public_id"]


class CartDetailForCartSerializer(serializers.ModelSerializer):
    product = ProductForCartSerializer()

    class Meta:
        model = CartDetail
        fields = ["pk", "product", "quantity", "sub_price"]


class CartFullSerializer(serializers.ModelSerializer):
    CartDetails = CartDetailForCartSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["CartDetails", "total_price"]
