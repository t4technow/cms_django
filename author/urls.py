from django.urls import path
from django.contrib.auth.views import LogoutView
from t4technow.common_views import *
from .views import *


urlpatterns = [
    path('', Dashboard.as_view(), name='author'),
    path('post/', PostListView.as_view(), name='author_posts'),
    path('post/create/', PostCreation.as_view(), name='author_post_create'),
    path('post/update/<pk>/', PostUpdateView.as_view(), name='author_post_update'),
    path('post/delete/<pk>/', PostDeleteView.as_view(), name='author_post_delete'),
    
        
    # Page Management
    path('page/', PageListView.as_view(), name='author_pages'),
    path('page/create/', PageCreateView.as_view(), name='author_page_create'),
    path('page/update/<slug:slug>/', PageUpdateView.as_view(), name='author_page_update'),
    path('page/delete/<slug:slug>/', PageDeleteView.as_view(), name='author_page_delete'),
    
    # path('category/', CategoryListView.as_view(), name='author_categories'),
    # path('category/<pk>/', CategoryDetailView.as_view(), name='author_category_details'),
    path('category/', CategoryCreateView.as_view(), name='author_categories'),
    path('category/update/<pk>/', CategoryUpdateView.as_view(), name='author_category_update'),
    path('category/update/<pk>/', CategoryDeleteView.as_view(), name='author_category_delete'),

    # path('tag/', TagListView.as_view(), name='author_tags'),
    # path('tag/<pk>/', TagDetailView.as_view(), name='author_tag_detail'),
    path('tag/', TagCreateView.as_view(), name='author_tags'),
    path('tag/update/<pk>/', TagUpdateView.as_view(), name='author_tag_update'),
    path('tag/update/<pk>/', TagDeleteView.as_view(), name='author_tag_delete'),

    # path('comments/', CommentListView.as_view(), name='author_comments'),
    # path('comments/delete/<pk>/', CommentDeleteView.as_view(), name='author_comment_delete'),

    # path('notifications/', NotificationListView.as_view(), name='author_notifications'),
    # path('notifications/<pk>/', NotificationDetailView.as_view(), name='author_notification_details'),
    # path('notifications/delete/<pk>/', NotificationDeleteView.as_view(), name='author_notification_delete'),
    
    path('profile/<pk>', Profile.as_view(), name='author_profile'),
    path('update/<pk>/', ProfileUpdateView.as_view(), name='author_profile_update'),
    
    path('logout/', LogoutView.as_view(), name='logout')
]