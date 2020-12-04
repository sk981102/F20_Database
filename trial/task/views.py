from django.shortcuts import render
from django.views import generic
from task.models import Task, ApplyTask
from submitter.models import Submitter
from django.shortcuts import get_object_or_404


def TaskDetailView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task': task})


def ListFunc(request):
    data = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': data})


def ViewContract(request, pk):
    return render(request, "contract.html", {'task_id': pk})


def Applied(request, task_id, submitter_id):
    try:
        task = get_object_or_404(Task, pk=task_id)
        submitter = get_object_or_404(Submitter, pk=submitter_id)
        applied = ApplyTask.objects.create(submitter=submitter, task=task, approved=0)
        applied.save()
        a=1
    except:
        a=0
    return render(request, "applied.html", {"a":a})


