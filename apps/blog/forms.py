from django import forms
from django import forms
from apps.api.models import Post, Comment


class PostForm(forms.ModelForm):
    # text = forms.CharField(widget=forms.TextArea, label='Entry')

    class Meta:
        model = Post
        exclude = ['author', 'slug']


class CommentForm(forms.ModelForm):
    class Meta:
        mode = Comment
        exclude = ['post']
