"""Импорт моделей"""
from django.contrib import admin

from models import Category
from models import TypeProduct
from models import Product
from models import ImageProduct


# Register your models here.

"""Регистрируем модели"""
admin.site.register(Category)
admin.site.register(TypeProduct)
admin.site.register(Product)
admin.site.register(ImageProduct)