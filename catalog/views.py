from django.shortcuts import render


def index(request):
    content = {"Title": "Main Page"}
    return render(request, "catalog/index.html", content)


def contacts(request):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    email = request.POST.get("email")
    feedback = request.POST.get("feedback")
    content = {"Title": "Contacts Page"}

    print(name, surname, email, feedback)
    return render(request, "catalog/contacts.html", content)
