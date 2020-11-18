from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def admin_landing_view(request, *args, **kwargs):
    return render(request, "admin_landing.html", {})


def submitter_landing_view(request, *args, **kwargs):
    return render(request, "submitter_landing.html", {})


def rater_landing_view(request, *args, **kwargs):
    return render(request, "rater_landing.html", {})

