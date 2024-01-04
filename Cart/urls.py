from django.urls import path
from .views import add_to_cart, cart_detail,remove_from_cart
urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart_detail/', cart_detail, name='cart_detail'),
        path('remove_from_cart/<int:cart_product_id>/', remove_from_cart, name='remove_from_cart'),

]
