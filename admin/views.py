from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy

from django.shortcuts import redirect

from author.models import Author

from .forms import *

from t4technow.common_views import *

# Create your views here.
class AdminLogin(LoginView):
    success_url = reverse_lazy('admin_posts')
    form_class = LoginForm
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return self.success_url
    
    
class AdminLogout(LogoutView):
    success_url = reverse_lazy('admin')
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return self.success_url


class Dashboard(PermissionRequiredMixin, TemplateView):
    template_name = "admin/home.html"
    permission_required = 'User.is_superuser'
    extra_context = {'sidebar': True}
    
    
    def handle_no_permission(self):
        return redirect('admin_login')



# Post Management
class PostListView(PermissionRequiredMixin, PostListView):
    permission_required = 'User.is_superuser'
    template_name = "admin/post/posts.html"
        
    def handle_no_permission(self):
        return redirect('admin_login')
    
    def post(self, request):
        query = request.POST['search']
        queryset = Post.objects.filter(title__icontains = query)
        if queryset:
            extra_context = self.extra_context.copy()
            extra_context['filtered_users'] = queryset
        else:
            extra_context = {'NotFound': 'NotFound'}
        self.extra_context = extra_context
        
        return self.get(request)
    
    
class PostCreateView(PermissionRequiredMixin, PostCreation):
    permission_required = 'User.is_superuser'
    success_url = reverse_lazy('admin_posts')
    template_name = 'admin/post/create.html'
    
    def handle_no_permission(self):
        return redirect('admin_login')
    

class PostUpdateView(PermissionRequiredMixin, PostUpdateView):
    permission_required = 'User.is_superuser'
    success_url = reverse_lazy('admin_posts')
    
    def handle_no_permission(self):
        return redirect('admin_login')



# Page Management
class PageListView(PermissionRequiredMixin, PageListView):
    permission_required = 'User.is_superuser'
    template_name = "admin/page/pages.html"
        
    def handle_no_permission(self):
        return redirect('admin_login')
    

class PageCreateView(PageCreateView, PermissionRequiredMixin):
    permission_required = 'User.is_superuser'
    success_url = reverse_lazy('admin_pages')
    
    def handle_no_permission(self):
        return redirect('admin_login')


# Author Management
class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = "admin/author/home.html"
    extra_context = {'sidebar': True}
    
    def get_queryset(self):
        queryset = Author.objects.filter(is_approved = True)
        return queryset
    
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreationForm
    template_name = "admin/add.html"
    success_url = reverse_lazy('admin_authors')
    
    def form_valid(self, form):
        form.instance.is_approved = True
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'
    template_name = "admin/update.html"

    success_url = reverse_lazy('admin_authors')

class BlockAuthor(UpdateView):
    model = Author
    fields = ['name',]
    template_name = "admin/update.html"

    success_url = reverse_lazy('admin_authors')
    
    def form_valid(self, form):
        form.instance.is_blocked = True
        return super().form_valid(form)