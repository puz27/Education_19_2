from django.urls import reverse_lazy
from .models import Product, Contacts, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from catalog.services import sendmail


class ShopHome(ListView):
    """ Main page. Show last 6 products."""
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "items"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main Page"
        return context

    def get_queryset(self):
        return Product.objects.all().order_by('-id')[:6]


class ShopContacts(ListView):
    """Contacts"""
    model = Contacts
    template_name = "catalog/contacts.html"
    context_object_name = "info_contacts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Our contacts"
        return context


class ShopAddProduct(CreateView):
    """Add Product"""
    model = Product
    template_name = "catalog/add_product.html"
    fields = ["name", "slug", "price", "category",  "description", "image"]
    success_url = reverse_lazy("index_page")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Add Product"
        return context


class ShopProductCard(DetailView):
    """Information about product"""
    model = Product
    template_name = "catalog/product_card.html"
    slug_url_kwarg = "product_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Product Information"
        context["product"] = self.get_object()
        return context


class ShopBlog(ListView):
    """Show all Blog that have True published status"""
    model = Blog
    template_name = "catalog/blog.html"
    context_object_name = "all_blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Blog"
        return context

    def get_queryset(self):
        return Blog.objects.all().filter(is_published=True)


class ShopBlogCard(DetailView):
    """Information about blog"""
    model = Blog
    template_name = "catalog/blog_card.html"
    slug_url_kwarg = "post_slug"

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()

        if obj.view_count == 35:
            sendmail("n.avramenko87@yandex.ru", self.get_object())
        return obj

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Blog Information"
        context["blog"] = self.get_object()
        return context


class ShopAddBlog(CreateView):
    """Add blog"""
    model = Blog
    template_name = "catalog/add_blog.html"
    fields = ["name", "slug", "description", "is_published", "image"]
    success_url = reverse_lazy("blog")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Add Blog"
        return context


class ShopUpdateBlog(UpdateView):
    """Update blog"""
    model = Blog
    template_name = "catalog/add_blog.html"
    fields = ["name", "slug", "description", "is_published", "image"]
    slug_url_kwarg = "update_slug"

    success_url = reverse_lazy("blog")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Blog"
        return context


class ShopDeleteBlog(DeleteView):
    """Delete blog"""
    model = Blog
    template_name = "catalog/add_blog.html"
    fields = ["name", "slug", "description", "is_published", "image"]
    slug_url_kwarg = "delete_slug"
    success_url = reverse_lazy("blog")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Blog"
        return context






# def index(request) -> render:
#     """Main page"""
#     items = Product.objects.all().order_by('-id')[:6]
#     content = {"Title": "Main Page", "main": "main", "items": items}
#     return render(request, "catalog/index.html", content)

# def contacts(request) -> render:
#     """Page with contacts from admin panel"""
#     content = {"Title": "Contacts Page", "main": "contacts"}
#     return render(request, "catalog/contacts.html", content)


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


# def product_card(request, id) -> render:
#     show_card = Product.objects.get(pk=id)
#     content = {"id": id,
#                "name": show_card.name,
#                "price": show_card.price,
#                "description": show_card.description,
#                "image": show_card.image
#                }
#     return render(request, "catalog/product_card.html", content)
