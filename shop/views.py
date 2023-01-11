from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from shop.models import Product
from shop.serializers import ShopSerializer


# Create your views here.


def index(request):

    return render(request, "shop/index.html", {'product': Product.objects.all()})


class ShopView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ShopSerializer
