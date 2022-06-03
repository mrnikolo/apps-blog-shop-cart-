from django.shortcuts import render , get_object_or_404,redirect , reverse
from django.views.decorators.http import require_POST
from Shop.views import product
import cart  
from .cart import Cart
from Shop import models
from . import forms


# Create your views here.
@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=pk)
    form = forms.CardAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product,
                product_count=form_data['product_count'],
                update_count=form_data['update'])
    return redirect(reverse('cart:cart_detail'))


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_product_count_form'] = forms.CardAddProductForm(
            initial={'product_count': item['product_count'],
                     'update': True}
        )
    return render(request, 'cart/cart.html', {'cart': cart})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(models.Product, id=product_id)
    cart.removeCart(product)
    return redirect(reverse('cart:cart_detail'))

