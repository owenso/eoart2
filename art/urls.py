from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ArtPageView.as_view(), name='art')
]
