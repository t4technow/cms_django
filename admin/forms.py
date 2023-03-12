from django import forms
from post.models import Post, Category, Tag
from author.models import Author
from user.models import User
from django.contrib.auth.forms import AuthenticationForm

from tinymce.widgets import TinyMCE


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'username *', 'name': 'username', 'id': 'username', 'required' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Password *', 'name': 'password', 'id': 'password', 'required' : True}))
    
    class Meta:
        model = User
        fields = ('username','password')

class CreatePostForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'class': 'form-control'}))
    
    tags = forms.ModelMultipleChoiceField(
                queryset=Tag.objects.all(),
                widget=forms.CheckboxSelectMultiple
            )
    category = forms.ModelChoiceField(
                queryset=Category.objects.all()
            )
    
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'slug', 'body', 'excerpt', 'category', 'tags', 'visibility', 'allow_comments',)
        
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Post Title', 'name': 'post_title', 'id': 'post_title', 'required' : True}),
            # 'body' : forms.Textarea(attrs = {'rows': 28, 'class': 'form-control rt-form-control text-start', 'placeholder': 'Content', 'name': 'body', 'id': 'body', 'required' : True}),
            'excerpt' : forms.Textarea(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Short Description', 'name': 'excerpt', 'id': 'excerpt'}),
            'featured_image' : forms.FileInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Featured Image', 'name': 'featured_image', 'id': 'featured_image'}),
            'slug': forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'required': False})
        }
        
        
class CreatePageForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'body', 'excerpt', 'visibility',)
        
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Page Title', 'name': 'page_title', 'id': 'page_title', 'required' : True}),
            # 'body' : forms.Textarea(attrs = {'rows': 28, 'class': 'form-control rt-form-control text-start', 'placeholder': 'Content', 'name': 'body', 'id': 'body', 'required' : True}),
            'excerpt' : forms.Textarea(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Short Description', 'name': 'excerpt', 'id': 'excerpt'}),
            'featured_image' : forms.FileInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Featured Image', 'name': 'featured_image', 'id': 'featured_image'}),
            'slug': forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'required': False})
        }

class CategoryCreationForm(forms.ModelForm):
    
    class Meta:

        model = Category
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Category Title', 'name': 'category_title', 'id': 'category_title', 'required' : True}),
        }

class TagCreationForm(forms.ModelForm):
    
    class Meta:

        model = Tag
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Category Title', 'name': 'category_title', 'id': 'category_title', 'required' : True}),
        }
        
        
class AuthorCreationForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('user_id', 'name', 'personal_website', 'sample_link')

