from django.urls import path, include
from products.api.views import *

urlpatterns = [
    path("products/", ProductList.as_view(), name="products"),
    path("product/<int:id>/", ProductDetail.as_view(), name="product"),
    path('categories/', CategoryList.as_view(), name='categories'),
]
