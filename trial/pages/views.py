from django.http import HttpResponse
from django.shortcuts import render
from submitter.models import Submitter
from django.shortcuts import get_object_or_404


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def admin_landing_view(request, *args, **kwargs):
    return render(request, "admin_landing.html", {})

def submitter_landing_view(request, *args, **kwargs):
    submitter = get_object_or_404(Submitter, pk=request.user.user_id)
    return render(request, "submitter_landing.html", {"submitter": submitter})

def rater_landing_view(request, *args, **kwargs):
    return render(request, "rater_landing.html", {})

