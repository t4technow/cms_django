from django.views.generic import DetailView, TemplateView

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse_lazy
from django.shortcuts import redirect

from t4technow.common_views import *

from .models import Author
from user.models import User


class Dashboard(TemplateView):
    template_name = "admin/home.html"
    # permission_required = 'user.is_author'
    extra_context = {'sidebar': True}
    
    def handle_no_permission(self):
        print(self.request.user.has_perms)
        print(self.request.user.has_perm('is_author'),'-----------------------------------------------------------------')
        print('permission denied')
        return redirect('home')



# # Post Management
class PostListView(PostListView):
    # permission_required = 'user.is_author'
    template_name = "admin/post/posts.html"
    
    def get_queryset(self):
        queryset = Post.objects.filter(content_type = 'post', author__user_id = self.request.user).order_by('-updated_at')
        return queryset
        
    def handle_no_permission(self):
        return redirect('user_login')
    
    
class PostCreateView(PostCreation):
    # permission_required = 'User.is_author'
    success_url = reverse_lazy('admin_posts')
    template_name = 'admin/post/create.html'
    
    def handle_no_permission(self):
        return redirect('admin_login')
    

class PostUpdateView(PostUpdateView):
    permission_required = 'User.is_author'
    success_url = reverse_lazy('admin_posts')
    
    def handle_no_permission(self):
        return redirect('admin_login')


# Page Management
class PageListView(PageListView):
    # permission_required = 'User.is_author'
    template_name = "admin/page/pages.html"
        
    def handle_no_permission(self):
        return redirect('admin_login')
    
    def get_queryset(self):
        queryset = Post.objects.filter(content_type = 'page', author__user_id = self.request.user).order_by('-updated_at')
        return queryset

class PageCreateView(PageCreateView):
    permission_required = 'User.is_author'
    success_url = reverse_lazy('admin_pages')
    
    def handle_no_permission(self):
        return redirect('admin_login')


# Author Management

class Profile(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = "author/profile.html"
