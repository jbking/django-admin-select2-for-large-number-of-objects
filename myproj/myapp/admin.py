from django.contrib import admin
from myapp.models import Category, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    autocomplete_fields = ["category"]
