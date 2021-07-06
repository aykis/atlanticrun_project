from django.contrib import admin

# Register your models here.


from .models import *

@admin.register(Texte)
class TexteAdmin(admin.ModelAdmin):
    list_display=['titre', 'contenu', 'pk']
    ordering = ['pk']
    search_fields = ['contenu', 'titre']

@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display=['nom', 'ordre', 'lien']
    ordering = ['ordre']

@admin.register(Caroussel)
class CarousselAdmin(admin.ModelAdmin):
    list_display=['nom']

@admin.register(ImageCaroussel)
class ImageCarousselAdmin(admin.ModelAdmin):
    list_display=['ordre', 'image']
    ordering=['ordre']

@admin.register(OngletCourse)
class OngletCourseAdmin(admin.ModelAdmin):
    list_display=['nom_course', 'sous_titre_course', 'ordre']
    ordering = ['ordre']