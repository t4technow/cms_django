from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.db.models import Count, Q
from .models import Category, Post, Comment

from .forms import CommentForm

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "post/home.html"
    
    def get_queryset(self):
        queryset = Post.objects.filter(content_type = 'post').order_by('-updated_at')[0:4]
        return queryset
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "post/single.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_post = self.object
        queryset = self.get_queryset()
                
        # Get the previous post 
        previous_post = queryset.filter(created_at__lt=current_post.created_at, content_type = 'post').order_by('-created_at').first()
        
        # Get the next post object
        next_post = queryset.filter(created_at__gt=current_post.created_at, content_type = 'post').order_by('created_at').first()
        
        context['previous_post'] = previous_post
        context['next_post'] = next_post
        
        # comments
        comments = Comment.objects.filter(parent = None, post_id = self.object.id).order_by('-created_at')
        
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            form.instance.post_id = post            
            form.instance.user_id = request.user
            comment.save()
            data = {
                'success': True,
                'comment': {
                    'body': comment.body,
                }
            }
        else:
            data = {'success': False, 'errors': form.errors}
            
        return JsonResponse(data)



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
