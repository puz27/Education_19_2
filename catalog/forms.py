from django import forms
from catalog.models import Category


class AppProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    price = forms.IntegerField()
    # image = forms.ImageField()

