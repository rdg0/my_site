from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['text'].widget.attrs.update({'class': 'textarea'})
    class Meta:
        
        model = Comment
        fields = ('name', 'email', 'text',)

