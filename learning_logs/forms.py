from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Class for creation of user interface forms for users."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}