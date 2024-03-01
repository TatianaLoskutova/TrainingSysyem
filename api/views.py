from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer, ProductStatisticSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Представление продукта.
    """

    queryset = Product.objects.prefetch_related('lessons').all()
    serializer_class = ProductSerializer


class ProductStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Представление статистки по продукту.
    """

    queryset = Product.objects.prefetch_related('group_set').all()
    serializer_class = ProductStatisticSerializer
