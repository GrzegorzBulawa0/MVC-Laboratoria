from django import forms

from .models import Film, Ocena

class FilmForm(forms.ModelForm):
    nowy_rezyser = forms.CharField(
        max_length=200,
        label="Reżyser"
    )

    class Meta:
        model = Film
        fields = ['text', 'nowy_rezyser']
        labels = {'text': ''}

    def clean_nowy_rezyser(self):
        nowy = (self.cleaned_data.get('nowy_rezyser') or '').strip()

        if not nowy:
            raise forms.ValidationError("Podaj reżysera.")

        return nowy
    
    
class OcenaForm(forms.ModelForm):
    class Meta:
        model = Ocena
        fields = ['text', 'rating']
        labels = {
            'text': 'Opinia',
            'rating': 'Ocena'
        }
        widgets = {'text': forms.Textarea(attrs={'cols':80}),
                   'rating': forms.Select(choices=[(i, f"{i}/10") for i in range(1, 11)])}