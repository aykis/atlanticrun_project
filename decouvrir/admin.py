from django.contrib import admin

# Register your models here.


from .models import *

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display=['titre', 'ordre']
