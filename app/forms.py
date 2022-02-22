from django.forms import ModelForm
from app.models import Filmes

class FilmesForm(ModelForm):
    class Meta:
        model = Filmes
        fields = ['nome', 'data', 'autor']