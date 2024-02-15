from django.shortcuts import render, redirect
from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Render the home page for blognation"""
    return render(request, 'blogs/index.html')


def blogs(request):
    """Renders the list of blogs in blognation"""
    blogs = Blog.objects.order_by('name')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


def blog(request, blog_id):
    """Renders the list of posts in a blog"""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)


@login_required
def new_blog(request):
    """Renders the form for adding a new blog"""
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
    """Renders the form for adding a new blog post"""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(request.user, blog.owner)
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """renders the form for editing a blog post"""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(request.user, blog.owner)
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


def check_blog_owner(user, owner):
    if user != owner:
        raise Http404
