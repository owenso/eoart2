from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EventPageView.as_view(), name='events'),
]
