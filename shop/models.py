from django.db import models

# Create your models here.


class Category(models.Model):
    """Категория"""
    name = models.CharField('категории', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TypeProduct(models.Model):
    """Тип продукта"""
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Тип продуктов'


class Product(models.Model):
    """Описание продукта """
    name = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Постер', upload_to='shop/')
    release_year = models.PositiveIntegerField('Дата выхода', default=2022)
    country = models.CharField('Страна производитель', max_length=30)
    type_product = models.ManyToManyField(TypeProduct, verbose_name='Тип продуктов', related_name="type_product")
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'фильмы'


class ImageProduct(models.Model):
    """Подробные фото продукта"""
    name = models.CharField('Заголовок', max_length=100)
    descriptions = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey(Product, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подробные фото'
        verbose_name_plural = 'Подробные фотографии'
