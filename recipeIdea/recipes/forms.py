from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        labels = {
            'name': '',
            'body': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'Placeholder': 'Full Name'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'Placeholder': 'Comment'}),
        }

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content', 'status',)
        labels = {
            'title': '',
            'author': 'Author',
            'content': '',
            'status': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'Placeholder':"Recipe Title"}),
            'author': forms.Select(attrs={'class':'form-control', 'Placeholder':"Author"}),
            'content': forms.Textarea(attrs={'class':'form-control', 'Placeholder':"Recipe Ingredents and Instructions"}),
        }
