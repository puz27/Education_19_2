from django import forms
from django.forms import formset_factory, inlineformset_factory

from catalog.models import Product, Version
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):

    forbidden_words = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Select Category"

    def clean_name(self):
        name = str(self.cleaned_data["name"])
        for word in self.forbidden_words:
            if word in name:
                raise ValidationError("You can not create product with this name!")
        return name

    def clean_description(self):
        name = str(self.cleaned_data["description"])
        for word in self.forbidden_words:
            if word in name:
                raise ValidationError("You can not create product with this description!")
        return name

    class Meta:
        model = Product
        fields = ["name", "price", "category", "description", "image"]


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"

    # VersionFormSet = inlineformset_factory(Product, Version, can_delete=False, max_num=3)


        # AuthorFormSet = formset_factory(
        #     AuthorForm,
        #     extra=2,
        #     max_num=2,
        #     min_num=1
        # )

    # widgets = {
    #     "name": forms.TextInput(attrs={'class': 'form-input'}),
    #     "price": forms.TextInput(attrs={'class': 'form-input'}),
    #     "description": forms.Textarea(attrs={'cols': 100, 'rows': 5}),
    #
    # }


# class AppProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     slug = forms.SlugField(max_length=255, unique=True)
#     description = forms.CharField(max_length=100)
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#     price = forms.IntegerField(null=False)
#     image = forms.ImageField(null=False)


# class AppBlogForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     slug = forms.SlugField(max_length=255, unique=True)
#     description = forms.CharField(max_length=100)
#     is_published = forms.BooleanField()
#     image = forms.ImageField(null=False)
