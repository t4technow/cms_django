from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy

from .models import Category, Post, Tag, Comment

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "post/home.html"
    
    def get_queryset(self):
        queryset = Post.objects.filter(content_type = 'post')
        return queryset
    
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "post/single.html"


class CategoryListView(TemplateView):
    template_name = "post/category.html"
    
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = "post/single-category.html"


class CommentCreateView(CreateView):
    model = Comment
    fields = '__all__'
    template_name = "post/comment.html"
    success_url = reverse_lazy('add_comment')