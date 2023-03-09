from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Home.as_view(), name="user_home"),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', UserCreateView.as_view(), name='user_registration'),
    path('become-author/', AuthorRequestView.as_view(), name='become_author'),
    path('profile/<pk>', Profile.as_view(), name='user_profile'),
    path('update/<pk>/', UserUpdateView.as_view(), name='update_user'),
    path('verify-email/', VerifyEmail.as_view(), name='verify_email'),
]