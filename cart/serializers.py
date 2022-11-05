from rest_framework import serializers
from cart.models import WishItem

class WishItemSerializer(serializers.ModelSerializer):
    book = serializers.CharField(read_only=True)
    class Meta:
        model = WishItem
        fields = '__all__'
    