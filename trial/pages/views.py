from django.http import HttpResponse
from django.shortcuts import render
from submitter.models import Submitter
from django.shortcuts import get_object_or_404
from task.models import ApplyTask
from raw_data.models import RawDataType

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def admin_landing_view(request, *args, **kwargs):
    return render(request, "admin_landing.html", {})

def rater_landing_view(request, *args, **kwargs):
    return render(request, "rater_landing.html", {})
