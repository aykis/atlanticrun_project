from django.db import models

# Create your models here.

class Presentation(models.Model):
    titre = models.CharField(max_length=200)
    ordre = models.IntegerField(unique=True)
    texte = models.TextField(default="<p>Votre paragraphe</p>", verbose_name="texte en html")
    logo = models.ImageField(upload_to = 'db/decouvrir/logo')
    photo_1 = models.ImageField(upload_to = 'db/index/photos')
    legende_1 = models.CharField(max_length=300)
    photo_2 = models.ImageField(upload_to = 'db/index/photos')
    legende_2 = models.CharField(max_length=300)

    def __str__(self):
        return self.titre
