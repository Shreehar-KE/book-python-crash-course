from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Enter the Topic'}
        widgets = {'text': forms.TextInput(
            attrs={'placeholder': ''}
        )}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(
            attrs={'cols': 80, 'placeholder': 'Type your content here'})}
