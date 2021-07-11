from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Movies
from genres.models import Genres
from artists.models import Artists

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genres
        fields = ("name",)
        labels = {
            'name': _('Name : '),            
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter Genre ', 'class': 'form-control'}),            
            }

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artists
        fields = ("first_name","last_name")
        labels = {
            'first_name': _('First Name : '), 
            'last_name': _('Last Name : '),            
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Enter First Name ', 'class': 'form-control'}), 
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Enter Last Name ', 'class': 'form-control'}),            
            }

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = ('name','genre_id','artist_id')
        labels = {
            'name': _('Name : '),
            'genre_id': _('Genre : '),
            'artist_id': _('Artist : '),
            'active': _('Is Active : '),
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter Movie Full name', 'class': 'form-control'}),
            'genre': forms.Select(
                attrs={'placeholder': 'Select Genre', 'class': 'form-control'}),
            'artist': forms.Select(
                
                attrs={'class': 'form-control'}),
            }



