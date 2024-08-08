from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album 
        fields = '__all__'
        labels = {
            'name': 'Nombre del Album',
            'year': 'Año',
            'gender': 'Género',
            'artist': 'Artista',
            'picture': 'Imagen'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),  
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class ArtistForm(forms.ModelForm):
    class Meta: 
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Nombre del Artista',
            'country': 'País'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }
