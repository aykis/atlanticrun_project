from .models import *
from django.shortcuts import render
import base.base as base

# Create your views here.

def index(request):

    context = {
        'decompteur' : base.decompteur(),
        'footer' : base.footer(),
        'presentations' : Presentation.objects.all().order_by("ordre"),
    }
    return render(request, 'decouvrir/index.html', context)