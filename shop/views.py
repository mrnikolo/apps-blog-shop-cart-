from django.shortcuts import get_object_or_404, render
from .models import Product
from . import models
from cart.forms import CardAddProductForm

# Create your views here.
def shop(request):
    products = Product.objects.order_by('-create')
    context = {'products': products}
    return render(request, 'products.html', context)


def product(request, pk):
    product_detail = get_object_or_404(models.Product, id=pk)
    cart_add_product_form = CardAddProductForm()
    return render(request, "product.html", {'product_detail': product_detail,
                 'cart_add_product_form' : cart_add_product_form })
