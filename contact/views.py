from atlanticrun_project.settings import MAIL_ASF
import os
from django.utils import html
from .models import Question
from django.shortcuts import render
import base.base as base
from .forms import QuestionForm

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from email.mime.image import MIMEImage


# Create your views here.

def contact(request):

    context = {'decompteur' : base.decompteur(),
        'footer' : base.footer()}

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

            data = form.cleaned_data

            plaintext = get_template('mail/mail.txt')
            htmly     = get_template('mail/mail.html')


            context_mail_client = { 'elements': form, "titre" : "Voici votre message !"}
            subject_client = '[AtlanticRun][Contact] {0}'.format(data.get("objet"))
            from_email, to = 'noreply@localhost', data.get("email")

            context_mail_asf = { 'elements': form, "titre" : "Nouveau message"}
            subject_asf = '[Contact] {0} {1} : {2}'.format(data.get("prenom"), data.get("nom"), data.get("objet"))

            text_content = plaintext.render(context_mail_client)
            html_content = htmly.render(context_mail_client)

            msg_client = EmailMultiAlternatives(subject_client, text_content, from_email, [to])
            msg_client.attach_alternative(html_content, "text/html")
            
            with open(os.path.join('static/images/', 'logo_course.png'), 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', '<logo_course.png>')
                img.add_header('Content-Disposition', 'inline', filename='logo_course.png')
            msg_client.attach(img)
            msg_client.send()

            text_content = plaintext.render(context_mail_asf)
            html_content = htmly.render(context_mail_asf)

            msg_asf = EmailMultiAlternatives(subject_asf, text_content, from_email, [MAIL_ASF], reply_to=[to])
            msg_asf.attach_alternative(html_content, "text/html")


            msg_asf.attach(img)
            msg_asf.send()

        else:
            context['errors'] = form.errors.items()
    else :
        form = QuestionForm()

    context['form'] = form

    return render(request, 'contact/contact.html', context)