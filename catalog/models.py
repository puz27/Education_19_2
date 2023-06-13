from django.db import models
from catalog.utils import slugify


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="product_name")
    description = models.TextField(null=True, blank=True, verbose_name="product_description")
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="product_price")
    time_create = models.DateField(auto_now_add=True, verbose_name="creation_date")
    time_update = models.DateField(auto_now=True, verbose_name="update_date")
    slug = models.SlugField(max_length=255, verbose_name="product_slug", null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "product_name"
        verbose_name_plural = "products"
        ordering = ["time_create", "name"]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    description = models.TextField(null=True, blank=True, verbose_name="category_description")
    # time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category_name"
        verbose_name_plural = "categories"


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="user_contact_name")
    surname = models.CharField(max_length=100, verbose_name="surname_contact_name")
    email = models.CharField(max_length=100, verbose_name="user_email")
    feedback = models.CharField(max_length=100, verbose_name="user_feedback")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name="blog_name")
    slug = models.SlugField(max_length=255, verbose_name="blog_slug", null=False, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="blog_description")
    image = models.ImageField(upload_to="images")
    time_create = models.DateField(auto_now_add=True, verbose_name="creation_date")
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(verbose_name="counts_views", default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
        ordering = ["time_create", "name"]


class Version(models.Model):
    # product = models.ForeignKey("Product", on_delete=models.CASCADE)
    product = models.CharField(max_length=100, verbose_name="title_name")
    number = models.IntegerField()
    title = models.CharField(max_length=100, verbose_name="title_name")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "version"
        verbose_name_plural = "versions"

    def __str__(self):
        return self.title
