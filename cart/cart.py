from decimal import Decimal
# from itertools import product
from django.conf import settings
from Shop import models

class Cart:


    def __init__(self , request) :
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add (self , product , product_count = 1 , update_count = False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'product_count' : 0,
                                     'price' : str(product.price)}
        
        if update_count:
            self.cart[product_id]['product_count'] = product_count
        else:
            self.cart[product_id]['product_count'] += product_count

        self.saveCart()

    # def __iter__(self):
    #     product_ids = self.cart.keys()
    #     products = models.Product.objects.filter(id__in=product_ids)

    #     for product in products:
    #         self.cart[str(product.id)]['product'] = product


    #     for item in self.cart.values():
    #         item['price'] = Decimal(item['price'])
    #         item['total_price'] = item['price'] * item['total_price'] 
    #         yield item


    def __iter__(self):
        product_ids = self.cart.keys()
        products = models.Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product


        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['product_count']
            yield item

        # return self.cart.values()




    def saveCart(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def removeCart(self , product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.saveCart()

        