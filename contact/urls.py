from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.emailView, name='contact'),
    url('success/', views.successView, name='success'),
    url('error/', views.errorView, name='error')
]
