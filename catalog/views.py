from django.shortcuts import render
from .models import Product, Contacts
from .forms import AppProductForm
from django.views.generic import ListView, DetailView, CreateView


# def index(request) -> render:
#     """Main page"""
#     items = Product.objects.all().order_by('-id')[:6]
#     content = {"Title": "Main Page", "main": "main", "items": items}
#     return render(request, "catalog/index.html", content)


class ShopHome(ListView):
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "items"
    #extra_context = {"Title": "Main Page"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main Page"
        return context

    def get_queryset(self):
        return Product.objects.all().order_by('-id')[:6]


# def contacts(request) -> render:
#     """Page with contacts from admin panel"""
#     content = {"Title": "Contacts Page", "main": "contacts"}
#     return render(request, "catalog/contacts.html", content)

class ShopContacts(ListView):
    model = Contacts
    template_name = "catalog/contacts.html"
    context_object_name = "info_contacts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Our contacts"
        return context

#
# def add_product(request) -> render:
#     """Page where user can add products to base"""
#     if request.method == "POST":
#         form = AppProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             image = form.cleaned_data.get("image")
#             description = form.cleaned_data.get("description")
#             price = form.cleaned_data.get("price")
#             category = form.cleaned_data.get("category")
#             obj = Product.objects.create(
#                                  name=name,
#                                  image=image,
#                                  description=description,
#                                  price=price,
#                                  category=category)
#             obj.save()
#             print(obj)
#     else:
#         form = AppProductForm()
#     content = {"form": form}
#     return render(request, 'catalog/add_product.html', content)


class ShopAddProduct(CreateView):
    model = Product
    template_name = "catalog/add_product.html"
    fields = ["name", "price", "category", "description", "image"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Add Product"
        return context


def products(request, page_id: int) -> render:
    """Show 10 products on page"""
    start_products_count = page_id * 10 - 10
    end_products_count = page_id * 10
    products = Product.objects.all().order_by('-id')[start_products_count:end_products_count]
    content = {"page_id": page_id, "products": products}
    return render(request, "catalog/products.html", content)


# def product_card(request, id) -> render:
#     show_card = Product.objects.get(pk=id)
#     content = {"id": id,
#                "name": show_card.name,
#                "price": show_card.price,
#                "description": show_card.description,
#                "image": show_card.image
#                }
#     return render(request, "catalog/product_card.html", content)


class ShopProductCard(DetailView):
    model = Product
    template_name = "catalog/product_card.html"
    context_object_name = "product"
    # slug_url_kwarg = "post_slug"
    pk_url_kwarg = "id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Product Information"
        return context
