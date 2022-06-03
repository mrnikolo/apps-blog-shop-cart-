from django.contrib import admin
from .models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'update')
    list_filter = ('update',)
    search_fields = ('slug', 'body')
    prepopulated_fields = {'slug': ('body',)}

