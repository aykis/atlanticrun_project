from django.db import models

# Create your models here.

class Question(models.Model):
    prenom = models.CharField(max_length=50, verbose_name="Prénom")
    nom = models.CharField(max_length=50, verbose_name="Nom")
    email = models.EmailField(verbose_name="E-mail")
    objet = models.CharField(max_length=100, verbose_name = "Objet")
    contenu = models.TextField(verbose_name = "Votre message")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date")

    def __str__(self):
        return "objet : {0} ; à {2} de {3} {4}\n {3}".format(
            self.objet, self.date.strftime("%Y-%m-%d %H:%M"),self.prenom, self.nom, self.contenu)