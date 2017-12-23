from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AboutPageView.as_view(), name='about'),
]
