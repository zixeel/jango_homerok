from django.shortcuts import render
from django.views.generic import DetailView, ListView

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


class BlogDetailView(DetailView):
    """просмотр блога отдельно"""
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object