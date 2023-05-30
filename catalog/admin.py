from django.contrib import admin
from .models import Product, Category, Contacts, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    search_fields = ("name", "description")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "email")


@admin.register(Blog)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "is_published", "view_count")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("is_published",)




