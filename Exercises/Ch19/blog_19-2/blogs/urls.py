"""Defining URL patterns for blogs"""
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page to list all blogs
    path('blogs/', views.blogs, name='blogs'),
    # Page to list all posts in a blog
    path('blog/<int:blog_id>', views.blog, name='blog'),
    # Page to add a New Blog
    path('new_blog/', views.new_blog, name='new_blog'),
    # Page to add a New Blog Post
    path('new_post/<int:blog_id>', views.new_post, name='new_post'),
    # Page to edit a Blog Post
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
]
