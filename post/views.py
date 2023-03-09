from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy

from .models import Category, Post, Tag, Comment
from django.db.models import Count, Q

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
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "post/category.html"
    
    def get_queryset(self):
        queryset = Category.objects.filter(post_category__content_type = 'post').annotate(no_of_posts = Count('post_category'))
        return queryset
    
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = "post/single-category.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug = self.object.slug)
        posts = Post.objects.filter(category = cat, content_type='post')
        context['posts'] = posts
        return context
    


class CommentCreateView(CreateView):
    model = Comment
    fields = '__all__'
    template_name = "post/comment.html"
    success_url = reverse_lazy('add_comment')