from django.shortcuts import render
from django.views.generic import TemplateView  # Import TemplateView

# Create your views here.


class EventPageView(TemplateView):
    template_name = "events.html"
