from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Category name')

    def __str__(self):
        return self.title


class Sizes(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Size')

    def __str__(self):
        return self.title


class Dough(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Dough')

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=80, unique=True, verbose_name='Name')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Category')
    size = models.ForeignKey(Sizes, on_delete=models.PROTECT, verbose_name='Size', null=True, blank=True)
    dough = models.ForeignKey(Dough, on_delete=models.PROTECT, verbose_name='Dough')
    price = models.IntegerField(default=0, verbose_name='Price')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo', blank=True)

    def __str__(self):
        return self.title
