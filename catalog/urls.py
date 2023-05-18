from django.urls import path
from catalog.views import index, contacts

urlpatterns = [
    path("", index, name="main"),
    path("contacts", contacts, name="contacts")
]
