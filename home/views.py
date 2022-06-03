from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')

    def post(self, request):
        pass

class BlogView(View):
    def get(self, request):
        return render(request, 'blog/blog.html')

    def post(self, request):
        pass

class ShopView(View):
    def get(self, request):
        return render(request, 'shop/shop.html')

    def post(self, request):
        pass


