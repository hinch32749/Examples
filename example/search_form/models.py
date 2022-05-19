from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название рубрики')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True,
                               verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'

    def __str__(self):
        return self.title

