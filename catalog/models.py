from django.db import models
from django.utils import timezone
from config import settings


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="product_name")
    description = models.TextField(null=True, blank=True, verbose_name="product_description")
    image = models.ImageField(upload_to="media")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="product_price")
    time_create = models.DateField(auto_now_add=True, verbose_name="product_create")
    time_update = models.DateField(auto_now=True, verbose_name="product_update")


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    description = models.TextField(null=True, blank=True, verbose_name="category_description")
    # time_create = models.DateField(auto_now_add=True)


