from django import forms
from .models import PembeliGo_Makanan

class PembeliForm(forms.ModelForm):
    class Meta:
        model =PembeliGo_Makanan
        fields ="__all__"