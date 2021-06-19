from django.shortcuts import render
import atlanticrun_project.base as base

# Create your views here.


def index(request):
    context = {
        'decompteur': base.decompteur(),
    }
    return render(request, 'envol/index.html', context)