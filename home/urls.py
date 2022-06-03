from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('shop', views.ShopView.as_view(), name='shop'),
]