from django import forms
from catalog.models import Category


class AppProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=255, unique=True)
    description = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    price = forms.IntegerField(null=False)
    image = forms.ImageField(null=False)


class AppBlogForm(forms.Form):
    name = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=255, unique=True)
    description = forms.CharField(max_length=100)
    is_published = forms.BooleanField()
    image = forms.ImageField(null=False)
