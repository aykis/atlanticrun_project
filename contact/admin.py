from django.contrib import admin

# Register your models here.


from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['prenom', 'nom', "email", 'objet', 'contenu', 'date']
    list_filter = ['objet', 'date']
    search_fields = ['objet', 'contenu', 'prenom', 'nom']
    #readonly_fields = ['objet', 'contenu', 'date', 'prenom', 'nom']

    
    def has_delete_permission(self, request, obj=None):
        return True