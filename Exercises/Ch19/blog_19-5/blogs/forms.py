from django import forms
from .models import Blog, BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': 'Name of the Blog'}


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'text']
        labels = {
            'title': 'Enter the Post\'s Title',
            'author': 'Enter the Author\'s name',
            'text': ''}
        placeholder = {'text': 'enter'}
        widgets = {'text': forms.Textarea(
            attrs={'cols': 80, 'placeholder': 'Type your post here...'})}
