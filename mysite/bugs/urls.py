__author__ = 'eqiihuu'

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.base, name='base'),
    url(r'(?P<bug_id>[0-9]+)/', 'bugs.views.detail', name='detail'),
]