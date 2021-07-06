from django.contrib import admin

# Register your models here.


from .models import *

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=['titre', 'ordre']
