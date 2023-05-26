from django.shortcuts import render
from .models import Product, Contacts


def index(request):
    items = Product.objects.all().order_by('-id')[:6]
    content = {"Title": "Main Page", "main": "main", "items": items}
    return render(request, "catalog/index.html", content)


def contacts(request):
    info_contacts = Contacts.objects.all()

    name = request.POST.get("name")
    surname = request.POST.get("surname")
    email = request.POST.get("email")
    feedback = request.POST.get("feedback")

    content = {"Title": "Contacts Page", "main": "contacts", "info_contacts": info_contacts}
    print(name, surname, email, feedback)

    return render(request, "catalog/contacts.html", content)
