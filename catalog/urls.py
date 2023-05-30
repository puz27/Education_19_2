from django.urls import path
from catalog.views import ShopHome, ShopContacts, ShopProductCard, ShopAddProduct, ShopBlog, ShopBlogCard, ShopAddBlog


urlpatterns = [
    path("", ShopHome.as_view(), name="index_page"),
    path("contacts/", ShopContacts.as_view(), name="contacts_page"),
    path("add_product/", ShopAddProduct.as_view(), name="add_product"),
    path("product_card/<slug:product_slug>", ShopProductCard.as_view(), name="product_card"),
    path("blog/", ShopBlog.as_view(), name="blog"),
    path("blog_card/<slug:post_slug>", ShopBlogCard.as_view(), name="blog_card"),
    path("add_blog/", ShopAddBlog.as_view(), name="add_blog"),
]
