from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'No selected'

    class Meta:
        model = Woman
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length exceeds 200 characters!')

        return title

    # title = forms.CharField(max_length=255, label="Name", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Content')
    # is_published = forms.BooleanField(label='Post it?', required=False, initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categories', empty_label='Not selected')
