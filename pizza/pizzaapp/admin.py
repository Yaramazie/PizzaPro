from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget

from .models import *


class PizzaAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Pizza
        fields = '__all__'


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']


class SizesAdmin(admin.ModelAdmin):
    list_display = ['title']


class DoughAdmin(admin.ModelAdmin):
    list_display = ['title']


class PizzaAdmin(admin.ModelAdmin):
    form = PizzaAdminForm
    list_display = ['title', 'category', 'size', 'dough', 'price_22sm', 'price_26sm', 'price_32sm', 'get_photo']
    list_display_links = ['title', 'category', 'size', 'dough', 'price_22sm', 'price_26sm', 'price_32sm']
    search_fields = ('title', 'category', 'size', 'dough')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = 'Photo'


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Sizes, SizesAdmin)
admin.site.register(Dough, DoughAdmin)
admin.site.register(Pizza, PizzaAdmin)
