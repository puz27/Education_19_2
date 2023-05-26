from django.urls import path
from catalog.views import index, contacts, add_product


urlpatterns = [
    path("", index, name="index_page"),
    path("contacts/", contacts, name="contacts_page"),
    path("add_product/", add_product, name="add_product")
]
