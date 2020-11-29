from django.shortcuts import render
from django.views import generic
from task.models import Task, ApplyTask
from raw_data.models import RawDataType, RawDataSeqFile
from submitter.models import Submitter
from django.shortcuts import get_object_or_404
from submitter.forms import UploadForm


# Create your views here.
def submitter_landing_view(request, *args, **kwargs):
    submitter = get_object_or_404(Submitter, pk=request.user.user_id)
    approved_tasks = ApplyTask.objects.filter(submitter=submitter, approved=1)
    pending_tasks = ApplyTask.objects.filter(submitter=submitter, approved=0)
    return render(request, "submitter_landing.html",
                  {"submitter": submitter, "approved_tasks": approved_tasks, "pending_tasks": pending_tasks, })


def submitter_file_upload(request, pk):
    task = get_object_or_404(Task, pk=pk)
    submitter = get_object_or_404(Submitter, pk=request.user.user_id)
    data_types = RawDataType.objects.filter(task=task)
    uploaded_files = RawDataSeqFile.objects.filter(raw_data_type__in=data_types, submitter=submitter)
    form = UploadForm(request.POST, request.FILES)
    # elements = RawDataSeqFile.objects.all()
    return render(request, "upload.html",
                  {"data_types": data_types, "form": form, "task": task, "uploaded_files": uploaded_files})


def submitted(request, pk):
    form = UploadForm(request.POST, request.FILES)
    raw_data_type = RawDataType.objects.get(pk=form.data['raw_data_type'])
    file = request.FILES['file']
    submitter = get_object_or_404(Submitter, pk=request.user.user_id)
    round = form.data['round']
    term_start = form.data['term_start']
    term_end = form.data['term_end']
    submitted = RawDataSeqFile.objects.create(submitter=submitter, file=file, raw_data_type=raw_data_type, round=round,
                                              term_start=term_start, term_end=term_end)
    submitted.save()

    return render(request, "submitted.html", )
