from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard.as_view(), name='admin'),
    
    path('login/', AdminLogin.as_view(), name='admin_login'),
    
    # Post Management
    path('post/', PostListView.as_view(), name='admin_posts'),
    path('post/create/', PostCreateView.as_view(), name='admin_post_create'),
    path('post/update/<slug:slug>/', PostUpdateView.as_view(), name='admin_post_update'),
    path('post/delete/<slug:slug>/', PostDeleteView.as_view(), name='admin_post_delete'),
    
    # Page Management
    path('page/', PageListView.as_view(), name='admin_pages'),
    path('page/create/', PageCreateView.as_view(), name='admin_page_create'),
    path('page/update/<slug:slug>/', PageUpdateView.as_view(), name='admin_page_update'),
    path('page/delete/<slug:slug>/', PageDeleteView.as_view(), name='admin_page_delete'),

    # Analytics
    # path('Analytics/', Analytics.as_view(), name='admin_analytics'),
    
    # Category Management
    path('category/', CategoryListView.as_view(), name='admin_categories'),
    path('category/create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('category/update/<slug:slug>/', CategoryUpdateView.as_view(), name='admin_category_update'),
    path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='admin_category_delete'),

    path('tag/', TagListView.as_view(), name='admin_tags'),
    path('tag/create/', TagCreateView.as_view(), name='admin_tag_create'),
    path('tag/update/<slug:slug>/', TagUpdateView.as_view(), name='admin_tag_update'),
    path('tag/delete/<slug:slug>/', TagDeleteView.as_view(), name='admin_tag_delete'),

    # path('comments/', CommentListView.as_view(), name='admin_comments'),
    # path('comments/delete/<pk>/', CommentDeleteView.as_view(), name='admin_comment_delete'),

    # Notifications
    path('notifications/', NotificationListView.as_view(), name='admin_notifications'),
    path('notifications/<pk>/', NotificationDetailView.as_view(), name='admin_notification_details'),
    # path('notifications/delete/<pk>/', NotificationDeleteView.as_view(), name='admin_notification_delete'),
    
    #author management
    path('author/', AuthorListView.as_view(), name='admin_authors'),
    path('author/create/', AuthorCreateView.as_view(), name='admin_author_create'),
    path('author/update/<pk>/', AuthorUpdateView.as_view(), name='admin_author_update'),
    path('author/block/<pk>/', BlockAuthor.as_view(), name='admin_block_author'),
    
    path('profile/', Profile.as_view(), name='admin_profile'),
    path('profile/update/<pk>/', ProfileUpdateView.as_view(), name='admin_profile_update'),
    
    path('logout/', AdminLogout.as_view(), name='admin_logout')
]