from django import forms
from .models import Review, Product


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')

    def clean(self):
        cleaned_data = self.cleaned_data

        return cleaned_data
