from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, View
from django.contrib.auth.views import LoginView 
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import User
from author.models import Author

from .forms import LoginForm, UserCreationForm


# For Email Verification
from verify_email.email_handler import send_verification_email


class Home(TemplateView):
    template_name = "admin/dashboard.html"


class UserLogin(LoginView):
    success_url = reverse_lazy('home')
    form_class = LoginForm
    template_name = 'user/login.html'
    
    def get_success_url(self):
        return self.success_url
    

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('user_login')
    template_name = "user/register.html"
    
    def form_valid(self, form):
        send_verification_email(self.request, form)
        return redirect('/user/verify_email')


class VerifyEmail(TemplateView):
    template_name = "user/verify-email.html"


class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = "admin/update.html"
    success_url = reverse_lazy('admin')


class AuthorRequestView(CreateView):
    model = Author
    success_url = reverse_lazy('home')
    fields = ['name', 'personal_website', 'sample_link']
    template_name = "admin/add.html"
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)
    
    

class Profile(DetailView):
    model = User
    template_name = "user/profile.html"
