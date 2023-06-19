from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from .forms import ProductForm, VersionForm
from .models import Product, Contacts, Blog, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.services import sendmail


class TitleMixin(object):
    """Mixin for show title on pages."""
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = self.get_title()
        return context


class ShopHome(TitleMixin, ListView):
    """Main page. Show last 6 products."""
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "items"
    title = 'Main Page'

    def get_queryset(self):
        return Product.objects.all().order_by('-id')[:6]


class ShopContacts(TitleMixin, ListView):
    """Contacts."""
    model = Contacts
    template_name = "catalog/contacts.html"
    context_object_name = "info_contacts"
    title = 'Our contacts'


class ShopAddProduct(CreateView):
    """Add Product."""
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:product_card', args=(self.object.slug,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Product"
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == "POST":
            context["formset"] = SubjectFormset(self.request.POST)
        else:
            context["formset"] = SubjectFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        self.object.owner = self.request.user

        if formset.is_valid():
            # before add new version make other version - inactive
            ver = Version.objects.all()
            for i in ver:
                i.is_active = False
                i.save()

            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ShopUpdateProduct(UpdateView):
    """Update product."""
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    slug_url_kwarg = "update_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Product"
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == "POST":
            context["formset"] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = SubjectFormset(instance=self.object)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            # before add new version make other version - inactive
            ver = Version.objects.all()
            for i in ver:
                i.is_active = False
                i.save()
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:update_product', args=(self.object.slug,))


class ShopProductCard(DetailView):
    """Information about product."""
    model = Product
    template_name = "catalog/product_card.html"
    slug_url_kwarg = "product_slug"

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Product Information"
        context["product"] = self.get_object()
        product_version = self.get_object()
        context["product_version"] = product_version.active_version
        return context


class ShopBlog(TitleMixin, ListView):
    """Show all Blog that have True published status."""
    model = Blog
    template_name = "catalog/blog.html"
    context_object_name = "all_blogs"
    title = "Blog"

    def get_queryset(self):
        return Blog.objects.all().filter(is_published=True)


class ShopBlogCard(DetailView):
    """Information about blog."""
    model = Blog
    template_name = "catalog/blog_card.html"
    slug_url_kwarg = "post_slug"

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()

        if obj.view_count == 35:
            sendmail("n.avramenko87@yandex.ru", "Information about Blog", self.get_object())
        return obj

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Blog Information"
        context["blog"] = self.get_object()
        return context


class ShopAddBlog(TitleMixin, CreateView):
    """Add blog."""
    model = Blog
    template_name = "catalog/add_blog.html"
    fields = ["name", "description", "is_published", "image"]
    success_url = reverse_lazy("catalog:blog")
    title = "Add Blog"

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:blog_card', args=(self.object.slug,))


class ShopUpdateBlog(TitleMixin, UpdateView):
    """Update blog."""
    model = Blog
    template_name = "catalog/add_blog.html"
    fields = ["name", "slug", "description", "is_published", "image"]
    slug_url_kwarg = "update_slug"
    title = "Update Blog"

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:blog_card', args=(self.object.slug,))


class ShopDeleteBlog(TitleMixin, DeleteView):
    """Delete blog."""
    model = Blog
    template_name = "catalog/add_blog.html"
    fields = ["name", "description", "is_published", "image"]
    slug_url_kwarg = "delete_slug"
    success_url = reverse_lazy("catalog:blog")
    title = "Delete Blog"
