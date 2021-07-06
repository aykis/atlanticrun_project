from django.db import models

# Create your models here.


class Footer(models.Model):
    nom = models.CharField(max_length=100)
    texte = models.TextField()

    def __str__(self):
        return "{0} : {1}".format(self.nom, self.texte)