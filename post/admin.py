from django.contrib import admin
from .models import Category, Post, Tag

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt",)
    prepopulated_fields = {"slug": ("title",)} 

admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 

admin.site.register(Tag, TagAdmin)