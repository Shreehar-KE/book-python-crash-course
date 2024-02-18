from django.shortcuts import render, redirect
from .models import Blog, Post
from .forms import BlogForm, PostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Home page for blognation"""
    posts = Post.objects.order_by('-date_added')
    context = {'recent_posts': [posts[0], posts[1]]}
    return render(request, 'blogs/index.html', context)


def blogs(request):
    """Page to list all blogs"""
    blogs = Blog.objects.order_by('name')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


def blog(request, blog_id):
    """Page to list all posts in a blog"""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)


@login_required
def new_blog(request):
    """renders a form page to create a new blog"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def new_post(request, blog_id):
    """renders a form page to create a new post"""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(request.user, blog.owner)
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)

    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(request.user, blog.owner)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'form': form, 'post': post, 'blog': blog}
    return render(request, 'blogs/edit_post.html', context)


def check_blog_owner(user, owner):
    if user != owner:
        raise Http404()
