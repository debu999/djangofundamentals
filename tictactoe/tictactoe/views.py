"""My first django app with views for Helloworld and other webpages"""
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello World! Here I come with django app.")

