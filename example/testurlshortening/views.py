from django.shortcuts import render
from django.http import HttpResponse
from django_url_shortener.utils import shorten_url

# Create your views here.

def testurl_withshortcode(request):
    created, message = shorten_url("https://github.com/rishav00a/django_url_shortener/issues","xyzw")
    if created:
        return HttpResponse("Short url created "+ message)
    else:
        return HttpResponse(message)


def testurl(request):
    created, message = shorten_url("https://github.com/rishav00a/django_url_shortener")
    if created:
        return HttpResponse("Short url created "+ message)
    else:
        return HttpResponse(message)