from .models import Poster,Film
from django import forms


class MyFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ('image','explanation_img')