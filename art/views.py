from django.shortcuts import render
from django.views.generic import TemplateView  # Import TemplateView

# Create your views here.

class ArtPageView(TemplateView):
    template_name = "index.html"