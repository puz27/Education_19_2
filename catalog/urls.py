from django.urls import path
from catalog.views import index, contacts


urlpatterns = [
    path("", index, name="index_page"),
    path("contacts/", contacts, name="contacts_page")
]
