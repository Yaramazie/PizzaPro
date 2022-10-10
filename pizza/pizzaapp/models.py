from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Category name')
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_category', kwargs={'slug': self.slug})


class Sizes(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Size')
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sizes', kwargs={'slug': self.slug})


class Dough(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Dough')
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dough', kwargs={'slug': self.slug})


class Pizza(models.Model):
    title = models.CharField(max_length=80, unique=True, verbose_name='Name')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Category')
    price_22sm = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Price_22sm')
    price_26sm = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Price_26sm')
    price_32sm = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Price_32sm')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    slug = models.SlugField(max_length=120, verbose_name='URL', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_pizza', kwargs={'slug': self.slug})
