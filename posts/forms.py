from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Post title ...'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Post body ...'}))

    class Meta:
        model = Post
        fields = ['title', 'body', 'publish', 'image']

