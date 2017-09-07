from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recept', views.recept, name='recept'),
]