from django.shortcuts import render, redirect
from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


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


def new_blog(request):
    """Renders the form for adding a new blog"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def new_post(request, blog_id):
    """Renders the form for adding a new blog post"""
    blog = Blog.objects.get(id=blog_id)
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


def edit_post(request, post_id):
    """renders the form for editing a blog post"""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
