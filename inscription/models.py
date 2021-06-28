from django.db import models

# Create your models here.

class DocumentsTelechargeable(models.Model):
    text_bouton = models.CharField(max_length=100, verbose_name="Texte du bouton")
    fichier = models.FileField(upload_to='documents/')

    def __str__(self):
        return "{0} : {1}".format(self.text_bouton, self.fichier.name)

class TailleTShirt(models.Model):
    nom = models.CharField(max_length=4)

    def __str__(self):
        return self.nom

class Inscription(models.Model):
    prenom = models.CharField(max_length=50, verbose_name="Prénom *")
    nom = models.CharField(max_length=50, verbose_name="Nom *")
    email = models.EmailField(verbose_name="Adresse e-mail *")
    paiement = models.BooleanField(verbose_name="Paiement direct", default=False)
    certificat = models.FileField(verbose_name="Certificat médical", blank=True, null=True)
    taille_tshirt = models.ForeignKey(to = TailleTShirt, null=True, default=1, on_delete=models.SET_NULL, verbose_name="Taille du T-shirt *")

    def __str__(self):
        return "{0} {1}, taille {2}".format(self.prenom, self.nom, self.taille_tshirt)
