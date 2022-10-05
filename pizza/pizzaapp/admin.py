from django.contrib import admin
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']


class SizesAdmin(admin.ModelAdmin):
    list_display = ['title']


class DoughAdmin(admin.ModelAdmin):
    list_display = ['title']


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'size', 'dough', 'price']
    list_display_links = ['title', 'category', 'size', 'dough', 'price']
    search_fields = ('title', 'category', 'size', 'dough')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Sizes, SizesAdmin)
admin.site.register(Dough, DoughAdmin)
admin.site.register(Pizza, PizzaAdmin)
