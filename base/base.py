from django.utils.translation import ngettext as _
from django.utils.translation import gettext
import datetime
from .models import *
from django.shortcuts import get_object_or_404

date = datetime.datetime(day=15, month=9, hour=14, year=2022)

def decompteur():

    jours = date-datetime.datetime.now()
    
    # if jours.days < 1:
    #     mois = date.days//30.3
    #     Nbjours = jours.days-mois*30.3

    # else :
    #     mois = date.month-datetime.datetime.now().month
    heures = date.hour-datetime.datetime.now().hour

    # if mois > 1 :
    #     txt = _(
    #         '%(mois)d mois %(jours)d jour',
    #         '%(mois)d mois %(jours)d jours',
    #         jours
    #     ) % {
    #         'mois': mois,
    #         'jours': jours,
    #     }
    # elif mois<0:
    #     txt = gettext("l'évènement est passé !")

    if jours.days > 6:
        txt = _(
            '%(jours)d jour',
            '%(jours)d jours',
            jours.days
        ) % { 'jours' : jours.days}
    elif jours.days <= 6 and jours.days >=0:
        txt = _(
            '%(jours)d jour %(heures)d heure',
            '%(jours)d jour %(heures)d heures',
            heures
        ) % { 'jours' : jours.days}
    else:
        txt = _("l'évènement est passé !")

    return txt

def footer():
    description = get_object_or_404(Footer, nom="description")
    site = get_object_or_404(Footer, nom="site")

    return {'description' : description.texte, "site" : site.texte}
