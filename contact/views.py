from .models import Question
from django.shortcuts import render
import atlanticrun_project.base as base
from .forms import QuestionForm

# Create your views here.

def contact(request):

    context = {'decompteur' : base.decompteur()}

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            """ prenom = form.cleaned_data["prenom"]
            nom = form.cleaned_data["nom"]
            objet = form.cleaned_data["objet"]
            contenu = form.cleaned_data["contenu"]
            try :
                Question.objects.create(prenom = prenom, nom = nom, objet = objet, contenu = contenu)
            except :
                pass """
            form.save()
        else:
            context['errors'] = form.errors.items()
    else :
        form = QuestionForm()


        context['form'] = form

    return render(request, 'contact/contact.html', context)