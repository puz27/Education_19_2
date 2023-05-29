from django.urls import path
from catalog.views import products, ShopHome, ShopContacts, ShopProductCard, ShopAddProduct


urlpatterns = [
    path("", ShopHome.as_view(), name="index_page"),
    path("contacts/", ShopContacts.as_view(), name="contacts_page"),
    path("add_product/", ShopAddProduct.as_view(), name="add_product"),
    path("products/<int:page_id>/", products, name="products"),
    path("product_card/<int:id>/", ShopProductCard.as_view(), name="product_card")
]
