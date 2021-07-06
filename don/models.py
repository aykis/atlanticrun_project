from django.db import models

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    ordre = models.IntegerField(unique=True)
    texte = models.TextField(default="<p>Votre paragraphe</p>", verbose_name="texte en html - <p>Paragraphe</p>")
    photo = models.ImageField(upload_to = 'db/index/photos')

    def __str__(self):
        return self.titre
