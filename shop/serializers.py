from rest_framework.serializers import ModelSerializer
from shop.models import Product


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description']
