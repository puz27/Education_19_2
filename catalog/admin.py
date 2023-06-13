from django.contrib import admin
from .models import Product, Category, Contacts, Blog, Version


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


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "number", "is_active")
    list_editable = ("is_active",)



