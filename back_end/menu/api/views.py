from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from ..models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemListView(ListAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.exclude(price=None)
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name", "price"]
