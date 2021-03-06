"""eoart2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.http import HttpResponse

def hosted_image(request):
    image_data = open(os.path.join(settings.BASE_DIR, 'img/EDO.jpg'), "rb").read()
    return HttpResponse(image_data, content_type="image/png")

urlpatterns = [
    url(r'^events/', include('events.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include('contact.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^img/EDO.jpg', hosted_image, name='hosted_image'),
    url(r'^', include('art.urls')),
    url(r'^', TemplateView.as_view(template_name='base.html')),
]
