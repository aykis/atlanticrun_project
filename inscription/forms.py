from django.forms import ModelForm, TextInput, EmailInput, FileInput
from django.forms.widgets import ChoiceWidget
from .models import *
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class InscriptionForm(ModelForm):
    class Meta:
        model = Inscription
        fields = ["prenom", "nom", "email", "taille_tshirt", "paiement", "certificat"]
        widgets = {
            'prenom': TextInput(attrs={'class': 'form-control', "placeholder": "Michel"}),
            'nom': TextInput(attrs={'class': 'form-control', "placeholder": "Dumas"}),
            'email': EmailInput(attrs={'class': 'form-control', "placeholder": "michel.dumas@imt-atlantique.fr"}),
            'certificat': FileInput(attrs={'class': 'form-control'}),
        }