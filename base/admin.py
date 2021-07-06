from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest

# Register your models here.

from .models import *

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display=['nom', 'texte']

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False