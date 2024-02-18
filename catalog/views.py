from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Category, Product, Blog


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name},{phone},{message}')
    return render(request, 'catalog/contacts.html')


def main(request):
    return render(request, 'catalog/main.html')


class CategoryListView(ListView):
    """просмотр списка категорий"""
    model = Category


class ProductListView(ListView):
    """Просмотр списка продуктов"""
    model = Product


def product(request, pk):
    category = Category.objects.get(pk=pk)
    product_list = Product.objects.filter(category=category)
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/product.html', context)


class ProductDetailView(DetailView):
    """Просмотр продукта отдельно"""
    model = Product


class BlogListView(ListView):
    """Просмотр списка блогов"""
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    """просмотр блога отдельно"""
    model = Blog

    def get_object(self, queryset=None):
        """счётчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    """создание блога"""
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    """удалиение блога"""
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(UpdateView):
    """редактирование записи"""
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')

    def get_success_url(self):
        """перенаправление на старицу редактируемого объекта после конформации"""
        return reverse_lazy('catalog:view_blog', args=[self.kwargs.get("pk")])
