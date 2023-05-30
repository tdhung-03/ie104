from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import generics, status
from rest_framework.response import Response
from purchase.models import *
from users.models import *
from products.models import *
from purchase.api.serializers import *
from django.db.models import Sum


class AddToCartAPIView(generics.CreateAPIView):
    queryset = CartDetail.objects.all()
    serializer_class = CartDetailSerializer

    @method_decorator(login_required)
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        cart, _ = Cart.objects.get_or_create(owner=request.user.profile)
        product = Product.objects.get(pk=product_id)

        # Check if the product already exists in the cart
        cart_item, created = CartDetail.objects.get_or_create(cart=cart, product=product)

        if not created:
            # If the product already exists, update the quantity by adding the new quantity
            cart_item.quantity += quantity
        else:
            # If it's a new product, create a new cart item
            cart_item.quantity = quantity

        cart_item.sub_price = cart_item.quantity * cart_item.product.price
        cart_item.save()

        cart.total_price = cart.CartDetails.aggregate(total=Sum('sub_price'))['total']
        cart.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)


class ConvertCartToOrderAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer

    @method_decorator(login_required)
    @method_decorator(ensure_csrf_cookie)
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner=request.user.profile)
        order = Order.objects.create(owner=request.user.profile, total_price=0)

        for cart_detail in cart.CartDetails.all():
            OrderDetail.objects.create(
                order=order,
                product=cart_detail.product,
                quantity=cart_detail.quantity,
                sub_price=cart_detail.sub_price
            )

        order.total_price = cart.total_price
        order.save()

        cart.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
