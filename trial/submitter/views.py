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
    tuple_count = parsed_files.aggregate(Sum('total_tuple_num'))['total_tuple_num__sum'] or 0
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
            raw_data_type = RawDataType.objects.get(pk=form.data['raw_data_type'])
            file = request.FILES['file']
            submitter = Submitter.objects.get(pk=request.user.user_id)
            round = form.cleaned_data['round']
            term_start = form.cleaned_data['term_start']
            term_end = form.cleaned_data['term_end']
            submitted = RawDataSeqFile.objects.create(submitter=submitter, file=file, raw_data_type=raw_data_type, round=round,
                                                      term_start=term_start, term_end=term_end)
            submitted.save()

            random_rater = random.sample(list(Rater.objects.all()), 1)
            raw_data_type = RawDataType.objects.filter(type_name=random_assigned[0].raw_data_type).first()
            assigned_task = AssignedTask.objects.create(rater=random_rater, raw_data=submitted, task=task, rated=0)
            assigned_task.save()

            return render(request, "submitted.html", )
        else:
            task = get_object_or_404(Task, pk=pk)
            form = UploadForm(task, submitter, request.POST, request.FILES)
            return render(request, "upload.html", {"form": form, "task":task})
