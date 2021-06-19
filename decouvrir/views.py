from django.shortcuts import render
import atlanticrun_project.base as base

# Create your views here.

def index(request):

    context = {
        'decompteur' : base.decompteur(),
    }
    return render(request, 'decouvrir/index.html', context)