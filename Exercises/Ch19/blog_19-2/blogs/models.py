from django.db import models


class Blog(models.Model):
    """Representation of a Blog"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """return the string representation of the blog"""
        return self.name


class BlogPost(models.Model):
    """Representation of a Blog Post"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the string representation of the blog post"""
        # if len(self.title) > 50:
        return self.title + ' - ' + self.author
