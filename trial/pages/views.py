from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def submitter_landing_view(request, *args, **kwargs):
    return render(request, "list.html", {})


def rater_landing_view(request, *args, **kwargs):
    return render(request, "rater_landing.html", {})

