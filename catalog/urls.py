from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ShopHome, ShopContacts, ShopProductCard, ShopAddProduct, ShopBlog, ShopBlogCard, ShopAddBlog,\
    ShopUpdateBlog, ShopDeleteBlog, ShopUpdateProduct, no_permissions

app_name = "catalog"

urlpatterns = [
    path("", ShopHome.as_view(), name="index_page"),
    path("contacts/", ShopContacts.as_view(), name="contacts_page"),
    path("add_product/", ShopAddProduct.as_view(), name="add_product"),
    path("update_product/<slug:update_slug>", ShopUpdateProduct.as_view(), name="update_product"),
    path("product_card/<slug:product_slug>", cache_page(60)(ShopProductCard.as_view()), name="product_card"),
    path("blog/", ShopBlog.as_view(), name="blog"),
    path("blog_card/<slug:post_slug>", ShopBlogCard.as_view(), name="blog_card"),
    path("add_blog/", ShopAddBlog.as_view(), name="add_blog"),
    path("update_blog/<slug:update_slug>", ShopUpdateBlog.as_view(), name="update_blog"),
    path("delete_blog/<slug:delete_slug>", ShopDeleteBlog.as_view(), name="delete_blog"),
    path("no_permission/", no_permissions, name="no_permission")
]
