from django.contrib import admin
from .models import Category, Post, PostImage


class PostImageInline(admin.TabularInline):
    model = PostImage
    max_num = 10
    min_num = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, ]

# Register your models here.
admin.site.register(Category)