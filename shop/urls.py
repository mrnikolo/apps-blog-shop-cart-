from django.urls import path
from .views import shop, product


app_name = 'shop'
urlpatterns = [

     path('', shop, name='shop'),

     path('product/<int:pk>/', product, name='product')
    
]