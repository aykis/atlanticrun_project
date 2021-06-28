from .models import Inscription
from django.shortcuts import redirect, render
import atlanticrun_project.base as base
from .forms import InscriptionForm
from .models import DocumentsTelechargeable

# Create your views here.

def inscription(request):

    context = {'decompteur' : base.decompteur()}

    boutons = DocumentsTelechargeable.objects.all()
    context['boutons'] = boutons
    form = InscriptionForm()
    context['form'] = form

    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            context['errors'] = form.errors.items()
            context['form'] = form
            return render(request, 'inscription/inscription.html', context)
        return redirect("index:index")

        
    return render(request, 'inscription/inscription.html', context)