from django.forms import ModelForm, TextInput
from django import forms
from .models import Question
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


#captcha : https://www.google.com/recaptcha/admin
class QuestionForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Question
        fields = ["prenom", "nom", "objet", "contenu", "captcha"]
        widgets = {
            'prenom': TextInput(attrs={'class': 'form-control', "placeholder": "Michel"}),
            'nom': TextInput(attrs={'class': 'form-control', "placeholder": "Dumas"}),
            'objet': TextInput(attrs={'class': 'form-control', "placeholder": "Objet"}),
            'contenu': forms.Textarea(attrs={'cols': 100, 'row': 15, "placeholder": "J'ai une question !"}),
            'captcha' : ReCaptchaField(widget=ReCaptchaWidget(), attrs={'style':'text-align:center;'}),
        }