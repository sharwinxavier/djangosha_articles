from django import forms
from . import models   # we need access to the article models, hence we are importing here

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']