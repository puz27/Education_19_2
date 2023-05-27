from django.shortcuts import render
from .models import Product, Contacts
from .forms import AppProductForm


def index(request) -> render:
    """Main page"""
    items = Product.objects.all().order_by('-id')[:6]
    content = {"Title": "Main Page", "main": "main", "items": items}
    return render(request, "catalog/index.html", content)


def contacts(request) -> render:
    """Page with contacts from admin panel"""
    info_contacts = Contacts.objects.all()

    name = request.POST.get("name")
    surname = request.POST.get("surname")
    email = request.POST.get("email")
    feedback = request.POST.get("feedback")

    content = {"Title": "Contacts Page", "main": "contacts", "info_contacts": info_contacts}
    print(name, surname, email, feedback)

    return render(request, "catalog/contacts.html", content)


def add_product(request) -> render:
    """Page where user can add products to base"""
    if request.method == "POST":
        form = AppProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            image = form.cleaned_data.get("image")
            description = form.cleaned_data.get("description")
            price = form.cleaned_data.get("price")
            category = form.cleaned_data.get("category")
            obj = Product.objects.create(
                                 name=name,
                                 image=image,
                                 description=description,
                                 price=price,
                                 category=category)
            obj.save()
            print(obj)
    else:
        form = AppProductForm()
    content = {"form": form}
    return render(request, 'catalog/add_product.html', content)


def products(request, page_id: int) -> render:
    """Show 10 products on page"""
    start_products_count = page_id * 10 - 10
    end_products_count = page_id * 10
    products = Product.objects.all().order_by('-id')[start_products_count:end_products_count]
    content = {"page_id": page_id, "products": products}
    return render(request, "catalog/products.html", content)
