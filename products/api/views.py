from products.api.serializers import *
from products.models import *
from rest_framework import generics
from django.db.models.functions import Lower
from django.contrib.postgres.search import TrigramSimilarity


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializerForProductList

    def get_queryset(self):
        search_query = self.request.query_params.get('name', None)
        queryset = Product.objects.all()

        if search_query:
            # Perform Levenshtein search using trigram similarity
            queryset = queryset.annotate(
                similarity=TrigramSimilarity(Lower('name'), search_query),
            ).filter(similarity__gt=0.3).order_by('-similarity')

        return queryset


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerForProductDetail
    lookup_field = 'id'


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryForQuery(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForQuerySerializer
    lookup_field = 'name'
