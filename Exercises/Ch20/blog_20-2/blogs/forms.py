from django import forms
from .models import Blog, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']
        labels = {'name': 'Enter the blog\'s name'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':''})}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Enter the post\'s title', 'content': ''}
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'placeholder': 'Type your post here...'}),
            'title':forms.TextInput(attrs={'placeholder':''})
            }
