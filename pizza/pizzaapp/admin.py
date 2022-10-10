from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget

from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}




class DoughAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}


class PizzaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'category', 'price_22sm', 'price_26sm', 'price_32sm', 'get_photo', 'slug']
    list_display_links = ['title', 'category', 'price_22sm', 'price_26sm', 'price_32sm']
    search_fields = ('title', 'category')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Photo'


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Dough, DoughAdmin)
admin.site.register(Pizza, PizzaAdmin)
