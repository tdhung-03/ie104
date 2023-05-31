from django.urls import path, include
from purchase.api.views import *

urlpatterns = [
    path('cart/add/', AddToCartAPIView.as_view(), name='add-to-cart'),
    path('cart/convert-to-order/', ConvertCartToOrderAPIView.as_view(), name='convert-cart-to-order'),
    path('cart/', CartFullView.as_view(), name='cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartAPIView.as_view(), name='remove-from-cart'),
    path('orders/', OrderFullView.as_view(), name='orders')
]
