from django.shortcuts import render

from cart.models import WishItem
from cart.serializers import WishItemSerializer
from rest_framework import  generics
# Create your views here.
class CartViewSet(generics.ListCreateAPIView):
    queryset = WishItem.objects.all()
    serializer_class = WishItemSerializer