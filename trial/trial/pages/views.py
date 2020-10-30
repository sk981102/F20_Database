from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Temp landing login page </h1>")


def submitter_landing_view(request, *args, **kwargs):
    return HttpResponse("<h1> Submitter Landing Page </h1>")


def rater_landing_view(request, *args, **kwargs):
    return HttpResponse("<h1> Rater Landing Page </h1>")
