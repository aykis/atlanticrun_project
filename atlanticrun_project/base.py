from django.utils.translation import ngettext as _
import datetime

date = datetime.datetime(day=11, month=9, hour=14, year=2021)

def decompteur():

    jours = date.day-datetime.datetime.now().day
    if jours < 0:
        mois = date.month-datetime.datetime.now().month-1
        jours +=31

    else :
        mois = date.month-datetime.datetime.now().month
    heures = date.hour-datetime.datetime.now().hour

    if mois > 1 :
        txt = _(
            '%(mois)d mois %(jours)d jour',
            '%(mois)d mois %(jours)d jours',
            jours
        ) % {
            'mois': mois,
            'jours': jours,
        }
    elif mois<0:
        txt = _("l'évènement est passé !")

    elif jours > 6:
        txt = _(
            '%(jours)d jour',
            '%(jours)d jours',
            jours
        ) % { 'jours' : jours}
    elif jours < 1 and jours >=0:
        txt = _(
            '%(jours)d jour %(heures)d heure',
            '%(jours)d jour %(heures)d heures',
            heures
        ) % { 'jours' : jours}
    else:
        txt = _("l'évènement est passé !")

    return txt