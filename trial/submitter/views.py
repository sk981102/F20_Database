import csv
import string

from django.shortcuts import render
from django.views import generic
from task.models import Task, ApplyTask
from raw_data.models import RawDataType, RawDataSeqFile
from submitter.models import Submitter
from parsed_data.models import ParsedData
from rater.models import Rater,AssignedTask
from rater.views import calculate_auto_score
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from submitter.forms import UploadForm
from django.http import HttpResponse
import numpy as np
import pandas as pd
import random
# Create your views here.
def submitter_landing_view(request, *args, **kwargs):
    submitter = get_object_or_404(Submitter, pk=request.user.user_id)
    approved_tasks = ApplyTask.objects.filter(submitter=submitter, approved=1)
    pending_tasks = ApplyTask.objects.filter(submitter=submitter, approved=0)
    return render(request, "submitter_landing.html",
                  {"submitter": submitter, "approved_tasks": approved_tasks, "pending_tasks": pending_tasks, })


def list_uploaded_file(request, pk):
    task = get_object_or_404(Task, pk=pk)
    submitter = get_object_or_404(Submitter, pk=request.user.user_id)
    data_types = RawDataType.objects.filter(task=task).distinct()
    uploaded_files = RawDataSeqFile.objects.filter(raw_data_type__in=data_types, submitter=submitter).order_by('round')
    count = uploaded_files.count()
    assigned_files = AssignedTask.objects.filter(raw_data__in = uploaded_files)
    parsed_files = ParsedData.objects.filter(submitter=submitter).distinct()
    tuple_count = np.sum(ParsedData.objects.filter(task=pk, pass_or_not=1,submitter=submitter).values_list('total_tuple_num', flat=True))
    request.session['taskid'] = pk

    return render(request, "submitter_uploaded.html", 
                  {"count":count, "tuple_count":tuple_count, "data_types": data_types, "task": task, "uploaded_files": uploaded_files, "assigned_files":assigned_files, "parsed_files":parsed_files})


def upload_new_file(request, pk):
    task = get_object_or_404(Task, pk=pk)
    submitter = Submitter.objects.get(pk=request.user.user_id)
    form = UploadForm(task, submitter)
    return render(request, "upload.html", {"form": form, "task":task})


def submitted(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        submitter = Submitter.objects.get(pk=request.user.user_id)
        form = UploadForm(task, submitter, request.POST, request.FILES)

        if form.is_valid():
            file1 = request.FILES['file']

            if is_csv(file1):
                raw_data_type = RawDataType.objects.get(pk=form.data['raw_data_type'])
                submitter = Submitter.objects.get(pk=request.user.user_id)
                round = form.cleaned_data['round']
                term_start = form.cleaned_data['term_start']
                term_end = form.cleaned_data['term_end']
                submitted = RawDataSeqFile.objects.create(submitter=submitter, file=file1, raw_data_type=raw_data_type,
                                                          round=round,
                                                          term_start=term_start, term_end=term_end)
                submitted.save()
                if len(Rater.objects.all())>0:
                    while True:
                        random_rater = random.sample(list(Rater.objects.all()), 1)
                        if len(AssignedTask.objects.filter(rater=random_rater[0], rated=0)) < 1:
                            if not AssignedTask.objects.filter(rater=random_rater[0], raw_data=submitted).exists():
                                print("loop broken")
                                break

                    assigned_task = AssignedTask.objects.create(rater=random_rater[0],
                                                                raw_data=submitted, task=task)
                    assigned_task.save()


                return render(request, "submitted.html", )
            else:
                form = UploadForm(task, submitter, request.POST, request.FILES)
                return render(request,"submit_fail.html",{"form": form})
        else:
            task = get_object_or_404(Task, pk=pk)
            form = UploadForm(task, submitter, request.POST, request.FILES)
            return render(request, "upload.html", {"form": form, "task":task})


def is_csv(infile):
    try:
       a=pd.read_csv(infile.open())
       return True
    except:
        return False