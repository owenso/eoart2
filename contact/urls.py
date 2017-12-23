from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ContactPageView.as_view(), name='contact'),
]
