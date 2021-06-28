from django.contrib import admin
from import_export.admin import ExportActionMixin
from import_export import fields
from import_export.widgets import ForeignKeyWidget


# Register your models here.


from .models import *

@admin.register(Inscription)
class InscriptionAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display=['prenom', 'nom', 'email', 'paiement', 'certificat', 'taille_tshirt']
    list_filter = ['paiement', 'taille_tshirt', 'paiement', 'certificat']
    search_fields = ['prenom', 'nom', 'email']
    widgets={
        'taille__tshirt' : ForeignKeyWidget(TailleTShirt, 'nom'),
    }
    #readonly_fields = ['objet', 'contenu', 'date', 'prenom', 'nom']

    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TailleTShirt)
class TailleTShirtAdmin(admin.ModelAdmin):
    list_display=['nom']

    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(DocumentsTelechargeable)
class DocumentsTelechargeableAdmin(admin.ModelAdmin):
    list_display=['text_bouton']
    #readonly_fields = ['objet', 'contenu', 'date', 'prenom', 'nom']

    
    def has_delete_permission(self, request, obj=None):
        return True