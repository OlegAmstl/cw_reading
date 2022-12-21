from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Article

class CreateArticle(forms.ModelForm):
    '''Форма написания новой статьи.'''

    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = (
            'title',
            'text'
        )