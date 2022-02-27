from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from \
    .models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['id']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['products']
    search_fields = ['positions__product__id']
