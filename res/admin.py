from django.contrib import admin
from unicodedata import category

from .models import Category, Food, Chefs, Klents


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_display_links = ('name',)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name',)
    ordering = ('price',)
    list_display_links = ('price',)


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'instagram_link', 'twitter_link')
    search_fields = ('name',)
    ordering = ('first_name',)
    list_display_links = ('first_name',)

@admin.register(Klents)
class KlentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
