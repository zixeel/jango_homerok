from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, product, ProductListView, ProductDetailView, CategoryListView, \
    BlogListView, main, BlogDetailView, BlogCreateView, BlogUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', main, name='main'),

    path('product/', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/', product, name='product', ),
    path('view_product/<int:pk>', ProductDetailView.as_view(), name='view_product'),

    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('view_blog/<int:pk>', BlogDetailView.as_view(), name='view_blog'),
    path('blog_create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog_edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),

]
