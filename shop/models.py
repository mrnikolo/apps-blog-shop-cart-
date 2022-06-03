from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 )
    price = models.IntegerField()
    body = models.TextField()
    img = models.ImageField(upload_to='image/product/%y/%m/%d')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    # def snippited(self):
    #     return self.body[0:30] + '...'


    def geturl(self):
            return reverse( 'Shop:product' , args = [ self.id ] )


       



class Order(models.Model):
    customer = models.ForeignKey(User , on_delete=models.CASCADE)
    order_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null = True ,  on_delete=models.SET_NULL)
    product_price = models.DecimalField(max_digits=10 , decimal_places=0)
    product_count = models.PositiveBigIntegerField()
    product_cost = models.DecimalField(decimal_places=0 , max_digits=10)


    def __str__(self):
        return self.order


class Invoice(models.Model):
    order = models.ForeignKey(Order ,null = True ,  on_delete=models.SET_NULL)
    invoice_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.order


class Transaction(models.Model):

    STATUS_CHOICES = {
        ('pending' , 'Pending'),
        ('failed' , 'Failed'),
        ('completed','Completed')
    }
    invoice = models.ForeignKey(Invoice ,null = True ,  on_delete=models.SET_NULL)
    transaction_data = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10 , decimal_places=0)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES , default='pending')


    def __str__(self):
        return self.invoice




    