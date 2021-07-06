from django.shortcuts import render
import base.base as base

# Create your views here.


def index(request):
    context = {
        'decompteur': base.decompteur(),
        'footer' : base.footer(),
    }
    return render(request, 'envol/index.html', context)