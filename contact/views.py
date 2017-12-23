from django.shortcuts import render
from django.views.generic import TemplateView  # Import TemplateView

# Create your views here.


class ContactPageView(TemplateView):
    template_name = "contact.html"
