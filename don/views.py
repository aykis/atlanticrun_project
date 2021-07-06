from django.shortcuts import render
import base.base as base
from .models import *

# Create your views here.

def index(request):

    context = {
        'decompteur' : base.decompteur(),
        'footer' : base.footer(),
        'articles' : Article.objects.all().order_by("ordre"),
    }
    return render(request, 'don/index.html', context)