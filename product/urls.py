# urls.py in your product app

from django.urls import path
from .views import ProductListView, ProductDetailView, AddProductView, AddProductImagesView, category_view,selected_subcategories_view,CategoryListView

urlpatterns = [
    path('الرئيسية/', ProductListView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('add_product_images/<int:pk>/', AddProductImagesView.as_view(), name='add_product_images'),
    path('categories/', category_view, name='category_view'),
    path('selected_subcategories/', selected_subcategories_view, name='selected_subcategories'),
    path('category/<int:category_id>/', CategoryListView.as_view(), name='category_detail'),


]
