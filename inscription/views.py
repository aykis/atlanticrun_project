from .models import *
from django.shortcuts import redirect, render
import base.base as base
from .forms import *
import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from email.mime.image import MIMEImage
from atlanticrun_project.settings import MAIL_ASF

# Create your views here.

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY

def paiement(self, request, *args, **kwargs):
    course_id = self.kwargs["pk"]
    course = Inscription.objects.get(id=course_id)
    YOUR_DOMAIN = "atlanticrun.imt-atlantique.fr"

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'eur',
                    'unit_amount': course.prix_en_centimes,
                    'product_data': {
                        'name': course.nom
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": course.id
        },
        mode='payment',
        success_url = YOUR_DOMAIN + '/success/',
        cancel_url = YOUR_DOMAIN + '/cancel/',
    )
    return JsonResponse({
        'id': checkout_session.id
    })


from django.views.generic import TemplateView

def SuccessView(TemplateView):
    template_name = "success.html"

def CancelView(TemplateView):
    template_name = "cancel.html"

def inscription(request):

    context = {'decompteur' : base.decompteur(),
        'footer' : base.footer(),}

    boutons = DocumentsTelechargeable.objects.all()
    context['boutons'] = boutons
    form = InscriptionForm()
    context['form'] = form

    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)


            data = form.cleaned_data
            form['taille_tshirt'].value = str(data["taille_tshirt"])
            form['course'].value = str(data["course"])
            form['paiement'].value = "Paiement validé" if data["paiement"] else "Pas encore encaissé"
            form["certificat"].value = "Aucun certificat donné" if data["certificat"] == None else "Un document a été remis"


            plaintext = get_template('mail/mail.txt')
            htmly     = get_template('mail/mail.html')


            context_mail_client = { 'elements': form, "titre" : "Votre inscription a bien été prise en compte !"}
            context_mail_asf = { 'elements': form, "titre" : "Nouvelle inscription"}

            subject_client = '[AtlanticRun] : Inscription à la course !'
            subject_asf = '[Inscription] {0} {1}'.format(data.get("prenom"), data.get("nom"))
            from_email, to = 'noreply@localhost', data.get("email")

            text_content = plaintext.render(context_mail_client)
            html_content = htmly.render(context_mail_client)
            msg_client = EmailMultiAlternatives(subject_client, text_content, from_email, [to])
            msg_client.attach_alternative(html_content, "text/html")

            text_content = plaintext.render(context_mail_asf)
            html_content = htmly.render(context_mail_asf)
            msg_asf = EmailMultiAlternatives(subject_asf, text_content, from_email, [MAIL_ASF], reply_to=[data.get("email")])
            msg_asf.attach_alternative(html_content, "text/html")

            
            with open(os.path.join('static/images/', 'logo_course.png'), 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<logo_course.png>')
                img.add_header('Content-Disposition', 'inline', filename='logo_course.png')
            msg_client.attach(img)
            msg_client.send()

            msg_asf.attach(img)
            msg_asf.send()



        else:
            context['errors'] = form.errors.items()
            context['form'] = form
            return render(request, 'inscription/inscription.html', context)
        return redirect("index:index")

        
    return render(request, 'inscription/inscription.html', context)