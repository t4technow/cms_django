from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('body',)
        
        widgets = {
            'body' : forms.Textarea(attrs = {'class': 'form-control text-area', 'name': 'comment', 'id': 'Comment', 'required' : True}),
        }