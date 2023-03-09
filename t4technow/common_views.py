from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.urls import reverse_lazy
from django.utils.text import slugify

from post.models import Post, Category, Tag
from author.models import Author
from user.models import User

from admin.forms import *
from user.forms import LoginForm

from django.core.paginator import Paginator

# Post Management
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 4
    extra_context = {'sidebar': True}
    
    def get_queryset(self):
        queryset = Post.objects.filter(content_type = 'post')
        return queryset
    

class PostCreation(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "admin/add.html"
    extra_context = {'page_title': 'new post'}
    
    
    def form_valid(self, form):
        title = form.cleaned_data['title']
        if not form.instance.slug:
            slug = slugify(title)
            form.instance.slug = slug
            
        author = Author.objects.get(user_id = self.request.user.id)
        form.instance.author = author
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = "admin/post/create.html"
    extra_context = {'page_title': 'Update Post : '}
    context_object_name = 'post'
    success_url = reverse_lazy('admin')


class PostDeleteView(DeleteView):
    model = Post
    template_name = "admin/confirm.html"
    success_url = reverse_lazy('admin')


# Page Management
class PageListView(ListView):
    model = Post
    template_name = "admin/pages.html"
    context_object_name = 'pages'
    extra_context = {'sidebar': True}
    
    
    def get_queryset(self):
        queryset = Post.objects.filter(content_type = 'page')
        return queryset


class PageCreateView(CreateView):
    model = Post
    fields = ['title', 'body', 'excerpt', 'author', 'visibility',]
    template_name = "admin/add.html"
    success_url = reverse_lazy('admin')

    def form_valid(self, form):
        
        title = form.cleaned_data['title']
        slug = slugify(title)
        form.instance.slug = slug
        
        form.instance.content_type = 'page'

        form.instance.allow_comments = 'no comments'
        
        return super().form_valid(form)


class PageUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = "admin/update.html"

    success_url = reverse_lazy('admin')


class PageDeleteView(DeleteView):
    model = Post
    template_name = "admin/confirm.html"
    success_url = reverse_lazy('admin')


# Category Management
# class CategoryListView(ListView):
#     model = Category
#     context_object_name = 'categories'
#     template_name = "admin/category/home.html"
#     extra_context = {'sidebar': True}
    

class CategoryListView(TemplateView):
    template_name = "admin/category/categories.html"
    extra_context = {'sidebar': True}



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreationForm
    template_name = "admin/add.html"
    success_url = reverse_lazy('admin')
    
    def form_valid(self, form):
        title = form.cleaned_data['title']
        slug = slugify(title)
        form.instance.slug = slug
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = "admin/update.html"

    success_url = reverse_lazy('admin')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "admin/confirm.html"
    success_url = reverse_lazy('admin')



# Tag Management
# class TagListView(ListView):
#     model = Tag
#     context_object_name = 'tags'
#     template_name = "admin/tags.html"
#     extra_context = {'sidebar': True}
    
    
class TagListView(TemplateView):
    template_name = "admin/tags/tags.html"
    extra_context = {'sidebar': True}



class TagCreateView(CreateView):
    model = Tag
    form_class = TagCreationForm
    template_name = "admin/add.html"
    success_url = reverse_lazy('admin')
    
    def form_valid(self, form):
        title = form.cleaned_data['title']
        slug = slugify(title)
        form.instance.slug = slug
        return super().form_valid(form)


class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    template_name = "admin/update.html"

    success_url = reverse_lazy('admin')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "admin/confirm.html"
    success_url = reverse_lazy('admin')


# Profile management
class Profile(TemplateView):
    template_name = "admin/author/profile.html"
    extra_context = {
        'sidebar': True,
        'title': 'profile'
        }
    


class ProfileUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = "admin/update.html"

    success_url = reverse_lazy('admin_profile')
    
    
# Notifications
class NotificationListView(ListView):
    model = Author
    context_object_name = 'notifications'
    
    opened = Author.objects.filter(request_status = True)
    declined = Author.objects.filter(request_status = True, is_approved = False)

    template_name = "admin/notifications/home.html"
    extra_context = {
        'sidebar': True,
        'opened': opened,
        'declined': declined,
        }
    
    
    def get_queryset(self):
        queryset = Author.objects.filter(request_status = False)
        return queryset



class NotificationDetailView(DetailView):
    model = Author
    context_object_name = 'notification'
    template_name = "admin/notification-single.html"
    
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        obj = Author.objects.get(id = id)
        
        obj.request_status = True
        obj.save()
        
        return super().get(request, args, kwargs)