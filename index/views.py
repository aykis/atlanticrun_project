from typing import Text
from django.shortcuts import render
from django.shortcuts import get_object_or_404
import base.base as base
from .models import *

# Create your views here.

def index(request):

    context = {
        'decompteur' : base.decompteur(),
        'footer' : base.footer(),
        'lacourse' : get_object_or_404(Texte, titre="La course Atlantic Run"),
        'caroussel_principal' : get_object_or_404(Caroussel, pk=1).images.all(),
        'img_ref' : get_object_or_404(Caroussel, pk=1).images.filter(pk=1)[0].image,
        'partenaires' : Partenaire.objects.all().order_by("ordre"),
        'onglet_course' : OngletCourse.objects.all().order_by('ordre')
    }

    print("img_ref : " + context['img_ref'].__str__())

    return render(request, 'index/index.html', context)