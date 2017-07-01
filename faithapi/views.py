from django.shortcuts import render
from django.conf.urls import url

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('ok')

def append_urls(urlpatterns):
    # Faith API:
    urlpatterns.append(url(r'^hello', hello, name='hello'));
