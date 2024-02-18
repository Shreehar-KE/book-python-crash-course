"""Defining URL patterns for blogs"""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Blogs Page
    path('blogs/', views.blogs, name='blogs'),
    # Posts Page
    path('blog/<int:blog_id>', views.blog, name='blog'),
    # New Blog page
    path('new_blog/', views.new_blog, name='new_blog'),
    # New Post Page
    path('new_post/<int:blog_id>', views.new_post, name='new_post'),
    # Edit Post Page
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post')
]
