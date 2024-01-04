from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, Cart_Product, Item_product
from django.contrib import messages
from django.http import JsonResponse

def add_to_cart(request, product_id):
    product = get_object_or_404(Item_product, pk=product_id)
    user = request.user if request.user.is_authenticated else None

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(User=user)

    # Check if the product is already in the cart
    cart_product = Cart_Product.objects.filter(Cart=cart, Product=product).first()

    # Get the quantity from the form submission
    quantity = int(request.POST.get('cart_quantity', 1))

    if cart_product:
        # If the product is already in the cart, update the quantity
        cart_product.Quantity += quantity
        cart_product.save()
    else:
        # If the product is not in the cart, create a new cart product
        Cart_Product.objects.create(Cart=cart, Product=product, Quantity=quantity)
    
    success_message = f"تم إضافة المنتج إلي عربة التسوق"

    # Return a JSON response with the success message
    return JsonResponse({'message': success_message})

def cart_detail(request):
    user = request.user if request.user.is_authenticated else None
    cart = Cart.objects.filter(User=user).first()

    if cart:
        cart_products = Cart_Product.objects.filter(Cart=cart)

        # Calculate total price and quantity for each cart product
        total_price = 0
        total_quantity = 0

        for cart_product in cart_products:
            cart_product.total_price = cart_product.Product.price * cart_product.Quantity
            total_price += cart_product.total_price
            total_quantity += cart_product.Quantity

        # Update the cart's total price and quantity
        cart.Total_price = total_price
        cart.Total_quantity = total_quantity
        cart.save()

        # Count of items in the cart
        cart_items_count = cart_products.count()
    else:
        cart_products = []
        cart_items_count = 0

    context = {'cart': cart, 'cart_products': cart_products, 'cart_items_count': cart_items_count}
    return render(request, 'cart_detail.html', context)



def remove_from_cart(request, cart_product_id):
    cart_product = get_object_or_404(Cart_Product, pk=cart_product_id)

    # Delete the Cart_Product instance
    cart_product.delete()

    # Optionally, add a success message
    # messages.success(request, "Product removed from your cart.")

    return redirect('cart_detail')
