from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

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


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:blog_list')
    """
     Пытался сделать в соотсветсвии с требованиями задания что бы редиректило на детальный просмотр того блога который
     редактировали но мне выдаёт оишбку  
     NoReverseMatch at /blog_edit/2/
     Reverse for 'catalog/view_blog/' not found. 'catalog/view_blog/' is not a valid view function or pattern name.
    """
    # def get_success_url(self):
    #     return reverse_lazy('view_blog/', kwargs={'pk': self.object.pk})
