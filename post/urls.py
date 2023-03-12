from django.urls import path
from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_details'),
    
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<slug:slug>', CategoryDetailView.as_view(), name='single_category'),
    
    # path('tags/', TagListView.as_view(), name='categories'),
    # path('tag/<slug:slug>', TagDetailsView.as_view(), name='tag_details'),
]