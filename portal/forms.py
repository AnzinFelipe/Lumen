from django import forms
from portal.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'subtitulo', 'texto', 'autor', 'tema')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o titulo da matéria'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o subtitulo da matéria'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insira o texto da matéria'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o nome do autor'}),
            'tema': forms.Select(attrs={'class': 'form-control'}),
        }