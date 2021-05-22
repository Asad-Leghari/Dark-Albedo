from django import template
from django.shortcuts import render
from django.http import HttpResponse

#below three are for contact form
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
###############################

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def skills(request):
    return render(request, 'base/skills.html')

def services(request):
    return render(request, 'base/services.html')

def contact(request):
    return render(request, 'base/contact.html')
    
def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['asadleghari537@gmail.com']
            )
        
        email.fail_silently=False
        email.send()
        
    return render(request, 'base/email_sent.html')
