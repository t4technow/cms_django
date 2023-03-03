from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

        
class UserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Password *', 'name': 'password', 'id': 'password', 'required' : True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Confirm Password *', 'name': 'confirm_password', 'id': 'confirm_password', 'required' : True}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
        widgets = {
            'first_name' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'First Name *', 'name': 'first_name', 'id': 'first_name', 'required' : True}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Last Name *', 'name': 'last_name', 'id': 'last_name', 'required' : True}),
            'username' : forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'username *', 'name': 'username', 'id': 'username', 'required' : True}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Email *', 'name': 'email', 'id': 'email', 'required' : True}),
        }


# class UpdateForm(forms.ModelForm):
    
    
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username')
        
#         widgets = {
#             'first_name' : forms.TextInput(attrs = {'class': 'form-control form-control-lg', 'required' : True}),
#             'last_name' : forms.TextInput(attrs = {'class': 'form-control form-control-lg', 'required' : True}),
#             'username' : forms.TextInput(attrs = {'class': 'form-control form-control-lg'}),
#             'email' : forms.EmailInput(attrs = {'class': 'form-control form-control-lg'}),
#         }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'username *', 'name': 'username', 'id': 'username', 'required' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control rt-form-control text-start', 'placeholder': 'Password *', 'name': 'password', 'id': 'password', 'required' : True}))
    
    class Meta:
        model = User
        fields = ('username','password')