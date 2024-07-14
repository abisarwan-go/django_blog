from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if not title:
            raise forms.ValidationError("Title is required.")
        if not content:
            raise forms.ValidationError("Content is required.")
        return cleaned_data
