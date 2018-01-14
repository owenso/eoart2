from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                email = EmailMessage(
                    subject,
                    message,
                    'contactform@artbyessieo.com',
                    ['admin@artbyessieo.com'],
                    reply_to=[email]
                )
                email.send()
            except BadHeaderError:
                # return HttpResponse('Invalid header found.')
                return redirect('error')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def successView(request):
    return render(request, "success.html")

def errorView(request):
    return render(request, "error.html")
