from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Texte(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField(default="<p>Votre paragraphe</p>", verbose_name="texte en html - <p>Paragraphe</p>")

    def __str__(self):
        return "{0} : {1}".format(self.titre, self.contenu)

class Partenaire(models.Model):
    nom = models.CharField(max_length=100)
    lien = models.URLField(verbose_name="lien - doit contenir http:// ou https://")
    logo = models.ImageField(upload_to = 'db/index/partenaires')
    ordre = models.IntegerField(unique=True)

    def __str__(self):
        return self.nom

class ImageCaroussel(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to = 'db/index/images_caroussel')
    ordre = models.IntegerField(verbose_name="Ordre - relatif et unique", unique=True)

    def __str__(self):
        return self.nom if self.nom != None else self.image.name


class Caroussel(models.Model):
    nom = models.CharField(max_length=100, blank=True, null=True)
    images = models.ManyToManyField(to=ImageCaroussel, related_name="caroussel")

    def __str__(self):
        return self.nom if self.nom != None else "Sans nom"


class OngletCourse(models.Model):
    nom_course = models.CharField(max_length=30)
    sous_titre_course = models.CharField(max_length=100)
    ordre = models.IntegerField(unique=True)
    logo = models.ImageField(upload_to = 'db/index/onglet/logo')
    caroussel = ForeignKey(to=Caroussel, null=True, on_delete=models.SET_NULL)
    texte = ForeignKey(to=Texte, null=True, blank=True, on_delete=models.SET_NULL)
    parcours = models.ImageField(upload_to = 'db/index/onglet/parcours')

    def __str__(self):
        return self.nom_course

