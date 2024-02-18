from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """Representation of a Blog"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """returns the string representation of the blog"""
        return self.name


class Post(models.Model):
    """Representation of a Blog Post"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the string representation of the blog post"""
        return self.title
